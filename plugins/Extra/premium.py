from datetime import timedelta
import pytz
import datetime, time
from Script import script 
from info import ADMINS, LOG_CHANNEL
from utils import get_seconds
from database.users_chats_db import db 
from pyrogram import Client, filters 
from pyrogram.errors.exceptions.bad_request_400 import MessageTooLong
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(filters.command("add_premium"))
async def give_premium_cmd_handler(client, message):
    user_id = message.from_user.id
    if user_id not in ADMINS:
        await message.reply("ʏᴏᴜ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴀɴʏ ᴘᴇʀᴍɪꜱꜱɪᴏɴ ᴛᴏ ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ.")
        return
    if len(message.command) == 3:
        user_id = int(message.command[1])  # Convert the user_id to integer
        user = await client.get_users(user_id)
        time = message.command[2]        
        seconds = await get_seconds(time)
        if seconds > 0:
            expiry_time = datetime.datetime.now() + datetime.timedelta(seconds=seconds)
            user_data = {"id": user_id, "expiry_time": expiry_time} 
            await db.update_user(user_data)  # Use the update_user method to update or insert user data
            await message.reply_text(f"ᴘʀᴇᴍɪᴜᴍ ᴀᴅᴅᴇᴅ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ᴛᴏ ᴛʜᴇ ᴜꜱᴇʀꜱ.\n👤 ᴜꜱᴇʀ ɴᴀᴍᴇ : {user.mention}\n⚡ ᴜꜱᴇʀ ɪᴅ : {user.id}\n⏰ ᴘʀᴇᴍɪᴜᴍ ᴀᴄᴄᴇꜱꜱ : {time}")
            time_zone = datetime.datetime.now(pytz.timezone("Asia/Kolkata"))
            current_time = time_zone.strftime("%d-%m-%Y\n›  𝖩𝗈𝗂𝗇𝗂𝗇𝗀 𝖣𝖺𝗍𝖾 : %I:%M:%S %p")            
            expiry = expiry_time   
            expiry_str_in_ist = expiry.astimezone(pytz.timezone("Asia/Kolkata")).strftime("%d-%m-%Y\n›  𝖤𝗑𝗉𝗂𝗋𝗒 𝖳𝗂𝗆𝖾 : %I:%M:%S %p")  
            await client.send_message(
                chat_id=user_id,
                text=f"<b>𝖯𝗋𝖾𝗆𝗂𝗎𝗆 𝖲𝗎𝖻𝗌𝖼𝗋𝗂𝗉𝗍𝗂𝗈𝗇 𝖠𝖼𝗍𝗂𝗏𝖺𝗍𝖾𝖽</b> ✅\n\n〇 𝖣𝗎𝗋𝖺𝗍𝗂𝗈𝗇  :  {time} \n\n›  𝖩𝗈𝗂𝗇𝗂𝗇𝗀 𝖣𝖺𝗍𝖾 : {current_time}\n\n›  𝖤𝗑𝗉𝗂𝗋𝗒 𝖣𝖺𝗍𝖾 : {expiry_str_in_ist}\n\n𝖤𝗇𝗃𝗈𝗒 𝗍𝗁𝖾 𝖺𝖽-𝖿𝗋𝖾𝖾 𝖾𝗑𝗉𝖾𝗋𝗂𝖾𝗇𝖼𝖾 𝖿𝗋𝗈𝗆 𝗇𝗈𝗐 🔥",                
            )
            #user = await client.get_users(user_id)
            await client.send_message(LOG_CHANNEL, text=f"#Added_Premium\n\n👤 ᴜꜱᴇʀ : {user.mention}\n⚡ ᴜꜱᴇʀ ɪᴅ : {user.id}\n⏰ ᴘʀᴇᴍɪᴜᴍ ᴀᴄᴄᴇꜱꜱ : {time}\n\n⏳ ᴊᴏɪɴɪɴɢ ᴅᴀᴛᴇ : {current_time}\n\n⌛️ ᴇxᴘɪʀʏ ᴅᴀᴛᴇ : {expiry_str_in_ist}", disable_web_page_preview=True)
                
        else:
            await message.reply_text("Invalid time format. Please use '1day for days', '1hour for hours', or '1min for minutes', or '1month for months' or '1year for year'")
    else:
        await message.reply_text("Usage: /add_premium user_id time \n\nExample /add_premium 1252789 10day \n\n(e.g. for time units '1day for days', '1hour for hours', or '1min for minutes', or '1month for months' or '1year for year')")

@Client.on_message(filters.command("myplan"))
async def check_plans_cmd(client, message):
    user = message.from_user.mention
    user_id  = message.from_user.id
    if await db.has_premium_access(user_id):         
        remaining_time = await db.check_remaining_uasge(user_id)             
        days = remaining_time.days
        hours, remainder = divmod(remaining_time.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        formatted_remaining_time = f"{days} ᴅᴀʏꜱ, {hours} ʜᴏᴜʀꜱ, {minutes} ᴍɪɴᴜᴛᴇꜱ, {seconds} ꜱᴇᴄᴏɴᴅꜱ"
        expiry_time = remaining_time + datetime.datetime.now()
        expiry_date = expiry_time.astimezone(pytz.timezone("Asia/Kolkata")).strftime("%d-%m-%Y")
        expiry_time = expiry_time.astimezone(pytz.timezone("Asia/Kolkata")).strftime("%I:%M:%S %p")  # Format time in IST (12-hour format)
        await message.reply_text(f"𝖤𝗇𝗃𝗈𝗒 𝗍𝗁𝖾 𝖺𝖽-𝖿𝗋𝖾𝖾 𝖾𝗑𝗉𝖾𝗋𝗂𝖾𝗇𝖼𝖾 𝖿𝗋𝗈𝗆 𝗇𝗈𝗐 🔥\n\n›  𝖴𝗌𝖾𝗋𝗇𝖺𝗆𝖾 : {user}\n ›  𝖴𝗌𝖾𝗋 𝖨𝖣: <code>{user_id}</code>\n›  𝖤𝗑𝗉𝗂𝗋𝗒 𝖣𝖺𝗍𝖾 : {expiry_date}\n›  𝖤𝗑𝗉𝗂𝗋𝗒 𝖳𝗂𝗆𝖾 : {expiry_time}\n›  𝖱𝖾𝗆𝖺𝗂𝗇𝗂𝗇𝗀 𝖳𝗂𝗆𝖾 : {formatted_remaining_time}")
    else:
        btn = [ 
            [InlineKeyboardButton("⏳ 5-𝖬𝗂𝗇 𝖥𝗋𝖾𝖾 𝖳𝗋𝗂𝖺𝗅 ⏳", callback_data="give_trial")],
            [InlineKeyboardButton("✨ 𝖡𝗎𝗒 P𝗋𝖾𝗆𝗂𝗎𝗆 : 𝖱𝖾𝗆𝗈𝗏𝖾 𝖠𝖽𝗌 ✨", callback_data="broze")],
        ]
        reply_markup = InlineKeyboardMarkup(btn)
        await message.reply_text(f"You Don’t Have Any Premium Subscription...\nIf You Want To Buy Premium, Click On The Button Below",reply_markup=reply_markup)


@Client.on_message(filters.command("remove_premium"))
async def remove_premium(client, message):
    user_id = message.from_user.id
    if user_id not in ADMINS:
        await message.reply_text("ʏᴏᴜ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴀɴʏ ᴘᴇʀᴍɪꜱꜱɪᴏɴ ᴛᴏ ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ.")
        return
    if len(message.command) == 2:
        user_id = int(message.command[1])  # Convert the user_id to integer
        user = await client.get_users(user_id)
        if await db.remove_premium_access(user_id):
            await message.reply_text("ᴜꜱᴇʀ ʀᴇᴍᴏᴠᴇᴅ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ !")
            await client.send_message(
                chat_id=user_id,
                text=f"𝖧𝖾𝗒 {user.mention},\n\nYour premium plan has expired.\n\n𝖨𝖿 𝗒𝗈𝗎 𝗐𝖺𝗇𝗍 𝗍𝗈 𝖻𝗎𝗒 𝗉𝗋𝖾𝗆𝗂𝗎𝗆 𝖺𝗀𝖺𝗂𝗇, 𝖼𝗅𝗂𝖼𝗄 𝗈𝗇 /plan 𝗍𝗈 𝖼𝗁𝖾𝖼𝗄 𝗈𝗎𝗍 𝗈𝗍𝗁𝖾𝗋 𝖺𝗏𝖺𝗂𝗅𝖺𝖻𝗅𝖾 𝗉𝗅𝖺𝗇𝗌."
            )
        else:
            await message.reply_text("ᴜɴᴀʙʟᴇ ᴛᴏ ʀᴇᴍᴏᴠᴇ ᴜꜱᴇʀ !\nᴀʀᴇ ʏᴏᴜ ꜱᴜʀᴇ, ɪᴛ ᴡᴀꜱ ᴀ ᴘʀᴇᴍɪᴜᴍ ᴜꜱᴇʀ ɪᴅ ?")
    else:
        await message.reply_text("ᴜꜱᴀɢᴇ : /remove_premium user_id") 
      

@Client.on_message(filters.command("premium_users"))
async def premium_users_info(client, message):
    user_id = message.from_user.id
    if user_id not in ADMINS:
        await message.reply("ʏᴏᴜ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴀɴʏ ᴘᴇʀᴍɪꜱꜱɪᴏɴ ᴛᴏ ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ.")
        return

    count = await db.all_premium_users()
    await message.reply(f"👥 ᴛᴏᴛᴀʟ ᴘʀᴇᴍɪᴜᴍ ᴜꜱᴇʀꜱ - {count}\n\n<i>ᴘʟᴇᴀꜱᴇ ᴡᴀɪᴛ, ꜰᴇᴛᴄʜɪɴɢ ꜰᴜʟʟ ɪɴꜰᴏ ᴏꜰ ᴘʀᴇᴍɪᴜᴍ ᴜꜱᴇʀꜱ</i>")

    users = await db.get_all_users()
    new = "📝 <u>ᴘʀᴇᴍɪᴜᴍ ᴜꜱᴇʀꜱ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ</u> :\n\n"
    user_count = 1
    async for user in users:
        data = await db.get_user(user['id'])
        if data and data.get("expiry_time"):
            expiry = data.get("expiry_time")
            expiry_ist = expiry.astimezone(pytz.timezone("Asia/Kolkata"))
            current_time = datetime.datetime.now(pytz.timezone("Asia/Kolkata"))
            
            if current_time > expiry_ist:
                await db.remove_premium_access(user['id'])  # Remove premium access if expired
                continue  # Skip the user if their expiry time has passed
                
            expiry_str_in_ist = expiry_ist.strftime("%d-%m-%Y")
            expiry_time_in_ist = expiry_ist.strftime("%I:%M:%S %p")
            time_left = expiry_ist - current_time
            
            days = time_left.days
            hours, remainder = divmod(time_left.seconds, 3600)
            minutes, seconds = divmod(remainder, 60)
            time_left_str = f"{days} ᴅᴀʏꜱ, {hours} ʜᴏᴜʀꜱ, {minutes} ᴍɪɴᴜᴛᴇꜱ, {seconds} ꜱᴇᴄᴏɴᴅꜱ"
            
            new += f"{user_count}. {(await client.get_users(user['id'])).mention}\n👤 ᴜꜱᴇʀ ɪᴅ : <code>{user['id']}</code>\n⏱️ ᴇxᴘɪʀᴇᴅ ᴅᴀᴛᴇ : {expiry_str_in_ist}\n⏱️ ᴇxᴘɪʀᴇᴅ ᴛɪᴍᴇ : {expiry_time_in_ist}\n⏳ ʀᴇᴍᴀɪɴɪɴɢ ᴛɪᴍᴇ : {time_left_str}\n\n"
            user_count += 1
        else:
            pass
    
    try:
        await message.reply(new)
    except MessageTooLong:
        with open('premium_users_info.txt', 'w+') as outfile:
            outfile.write(new)
        await message.reply_document('premium_users_info.txt', caption="Premium Users Information:")

# Free Trail Remove ( Give Credit To - NBBotz )
@Client.on_message(filters.command("refresh"))
async def reset_trial(client, message):
    user_id = message.from_user.id
    if user_id not in ADMINS:
        await message.reply("ʏᴏᴜ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴀɴʏ ᴘᴇʀᴍɪꜱꜱɪᴏɴ ᴛᴏ ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ.")
        return

    try:
        if len(message.command) > 1:
            target_user_id = int(message.command[1])
            updated_count = await db.reset_free_trial(target_user_id)
            message_text = f"ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ʀᴇꜱᴇᴛ ꜰʀᴇᴇ ᴛʀᴀɪʟ ꜰᴏʀ ᴜꜱᴇʀꜱ {target_user_id}." if updated_count else f"ᴜꜱᴇʀ {target_user_id} ɴᴏᴛ ꜰᴏᴜɴᴅ ᴏʀ ᴅᴏɴ'ᴛ ᴄʟᴀɪᴍ ꜰʀᴇᴇ ᴛʀᴀɪʟ ʏᴇᴛ."
        else:
            updated_count = await db.reset_free_trial()
            message_text = f"ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ʀᴇꜱᴇᴛ ꜰʀᴇᴇ ᴛʀᴀɪʟ ꜰᴏʀ {updated_count} ᴜꜱᴇʀꜱ."

        await message.reply_text(message_text)
    except Exception as e:
        await message.reply_text(f"An error occurred: {e}")
       

@Client.on_message(filters.command("plan"))
async def plan(client, message):
    user_id = message.from_user.id 
    users = message.from_user.mention 
    btn = [[
	
        InlineKeyboardButton('🧑‍💻  𝖢𝗈𝗇𝗍𝖺𝖼𝗍  𝖠𝖽𝗆𝗂𝗇  🧑‍💻', url='https://t.me/LordShibam')],[InlineKeyboardButton("✘  𝖢𝗅𝗈𝗌𝖾  ✘", callback_data="close_data")
    ]]
    await message.reply_photo(photo="https://graph.org/vTelegraphBot-07-28-35", caption=script.PREPLANS_TXT.format(message.from_user.mention), reply_markup=InlineKeyboardMarkup(btn))
    
