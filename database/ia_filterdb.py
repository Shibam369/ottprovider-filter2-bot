import logging
import re
import base64
from os import environ
from struct import pack
from pyrogram.file_id import FileId
from pymongo.errors import DuplicateKeyError
from umongo import Instance, Document, fields
from motor.motor_asyncio import AsyncIOMotorClient
from marshmallow.exceptions import ValidationError
from info import DATABASE_NAME, COLLECTION_NAME, MAX_BTN, FIRST_DB_URI, SECOND_DB_URI, THIRD_DB_URI

# ========================
# DB Connections
# ========================
client1 = AsyncIOMotorClient(environ.get("FIRST_DB_URI"))
db1 = client1[DATABASE_NAME]
instance1 = Instance.from_db(db1)

client2 = AsyncIOMotorClient(environ.get("SECOND_DB_URI"))
db2 = client2[DATABASE_NAME]
instance2 = Instance.from_db(db2)

client3 = AsyncIOMotorClient(environ.get("THIRD_DB_URI"))
db3 = client3[DATABASE_NAME]
instance3 = Instance.from_db(db3)

# ========================
# Media Models
# ========================
# Base class for shared fields
class BaseMedia:
    file_id = fields.StrField(attribute='_id')
    file_ref = fields.StrField(allow_none=True)
    file_name = fields.StrField(required=True)
    file_size = fields.IntField(required=True)
    mime_type = fields.StrField(allow_none=True)
    caption = fields.StrField(allow_none=True)
    file_type = fields.StrField(allow_none=True)

# DB-specific documents
@instance1.register
class MediaDB1(Document, BaseMedia):
    class Meta:
        collection_name = COLLECTION_NAME
        indexes = ['file_name']

@instance2.register
class MediaDB2(Document, BaseMedia):
    class Meta:
        collection_name = COLLECTION_NAME
        indexes = ['file_name']

@instance3.register
class MediaDB3(Document, BaseMedia):
    class Meta:
        collection_name = COLLECTION_NAME
        indexes = ['file_name']

# ========================
# DB Size Helpers
# ========================
async def get_files_db1_size():
    return (await db1.command("dbstats"))['dataSize']

async def get_files_db2_size():
    return (await db2.command("dbstats"))['dataSize']

async def get_files_db3_size():
    return (await db3.command("dbstats"))['dataSize']

# ========================
# File Save Function (Auto-rotate DBs)
# ========================
async def save_file(media):
    """
    Save file in DB1 -> DB2 -> DB3 automatically based on available space.
    """
    file_id, file_ref = unpack_new_file_id(media.file_id)
    file_name = re.sub(r"(_|\-|\.|\+)", " ", str(media.file_name))

    # Try DB1, then DB2, then DB3
    for Model, db_func in [(MediaDB1, get_files_db1_size),
                           (MediaDB2, get_files_db2_size),
                           (MediaDB3, get_files_db3_size)]:
        try:
            if (await db_func()) < 480 * 1024 * 1024 * 1024:  # ~480GB limit, adjust if needed
                try:
                    file = Model(
                        file_id=file_id,
                        file_ref=file_ref,
                        file_name=file_name,
                        file_size=media.file_size,
                        mime_type=media.mime_type,
                        caption=media.caption.html if media.caption else None,
                        file_type=media.mime_type.split('/')[0] if media.mime_type else None
                    )
                except ValidationError:
                    logging.error("Error occurred while saving file in database")
                    return 'err'

                try:
                    await file.commit()
                except DuplicateKeyError:
                    logging.info(f'{getattr(media, "file_name", "NO_FILE")} already saved')
                    return 'dup'
                else:
                    logging.info(f'{getattr(media, "file_name", "NO_FILE")} saved successfully in {Model.__name__}')
                    return 'suc'
        except Exception as e:
            logging.warning(f"Error checking {Model.__name__} size: {e}")
            continue
    logging.error("All DBs are full or unavailable")
    return 'err'

# ========================
# Search & Query Functions (Merged All DBs)
# ========================
async def get_search_results(query, max_results=MAX_BTN, offset=0, lang=None):
    """
    Search across DB1 + DB2 + DB3 and return merged results.
    """
    query = query.strip()
    if not query:
        raw_pattern = '.'
    elif ' ' not in query:
        raw_pattern = r'(\b|[\.\+\-_])' + query + r'(\b|[\.\+\-_])'
    else:
        raw_pattern = query.replace(' ', r'.*[\s\.\+\-_]')

    try:
        regex = re.compile(raw_pattern, flags=re.IGNORECASE)
    except re.error:
        regex = query

    filter_q = {'file_name': regex}

    results = []
    total_results = 0
    for Model in [MediaDB1, MediaDB2, MediaDB3]:
        cursor = Model.find(filter_q).sort('$natural', -1)
        model_results = await cursor.to_list(length=max_results * 3)
        if lang:
            model_results = [f for f in model_results if lang in f.file_name.lower()]
        results.extend(model_results)
        total_results += await Model.count_documents(filter_q)

    # Sort by newest (if id available)
    results.sort(key=lambda x: getattr(x.id, "generation_time", 0), reverse=True)

    files = results[offset: offset + max_results]
    next_offset = offset + max_results
    if next_offset >= total_results:
        next_offset = ''

    return files, next_offset, total_results

async def get_bad_files(query, file_type=None):
    query = query.strip()
    if not query:
        raw_pattern = '.'
    elif ' ' not in query:
        raw_pattern = r'(\b|[\.\+\-_])' + query + r'(\b|[\.\+\-_])'
    else:
        raw_pattern = query.replace(' ', r'.*[\s\.\+\-_]')

    try:
        regex = re.compile(raw_pattern, flags=re.IGNORECASE)
    except re.error:
        return [], 0

    filter_q = {'file_name': regex}
    if file_type:
        filter_q['file_type'] = file_type

    results = []
    total_results = 0
    for Model in [MediaDB1, MediaDB2, MediaDB3]:
        total_results += await Model.count_documents(filter_q)
        cursor = Model.find(filter_q).sort('$natural', -1)
        results.extend(await cursor.to_list(length=total_results))

    return results, total_results

async def get_file_details(file_id):
    filter_q = {'file_id': file_id}
    for Model in [MediaDB1, MediaDB2, MediaDB3]:
        cursor = Model.find(filter_q)
        filedetails = await cursor.to_list(length=1)
        if filedetails:
            return filedetails
    return []

# ========================
# Encode / Decode Helpers
# ========================
def encode_file_id(s: bytes) -> str:
    r = b""
    n = 0
    for i in s + bytes([22]) + bytes([4]):
        if i == 0:
            n += 1
        else:
            if n:
                r += b"\x00" + bytes([n])
                n = 0
            r += bytes([i])
    return base64.urlsafe_b64encode(r).decode().rstrip("=")

def encode_file_ref(file_ref: bytes) -> str:
    return base64.urlsafe_b64encode(file_ref).decode().rstrip("=")

def unpack_new_file_id(new_file_id):
    """Return file_id, file_ref"""
    decoded = FileId.decode(new_file_id)
    file_id = encode_file_id(
        pack(
            "<iiqq",
            int(decoded.file_type),
            decoded.dc_id,
            decoded.media_id,
            decoded.access_hash
        )
    )
    file_ref = encode_file_ref(decoded.file_reference)
    return file_id, file_ref


Media = (MediaDB1, MediaDB2, MediaDB3)
