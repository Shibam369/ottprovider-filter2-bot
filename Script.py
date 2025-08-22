import os
class script(object):
    START_TXT = """<b>𝖧𝖾𝗅𝗅𝗈, {} {} !</b>👋\n
𝖭𝗂𝖼𝖾 𝖳𝗈 𝖬𝖾𝖾𝗍 𝖸𝗈𝗎, 𝖬𝗒 𝖣𝖾𝖺𝗋 𝖥𝗋𝗂𝖾𝗇𝖽! 🫂\n
𝖨'𝗆 𝖯𝗈𝗐𝖾𝗋𝖿𝗎𝗅 𝖡𝗈𝗍, 𝖸𝗈𝗎 𝖢𝖺𝗇 𝖴𝗌𝖾 𝖬𝖾 𝖠𝗌 A 𝖠𝗎𝗍𝗈-𝖿𝗂𝗅𝗍𝖾𝗋 !! 𝖨 𝖢𝖺𝗇 𝖯𝗋𝗈𝗏𝗂𝖽𝖾 𝖸𝗈𝗎 𝖬𝗈𝗏𝗂𝖾𝗌, 𝖶𝖾𝖻 𝖲𝖾𝗋𝗂𝖾𝗌 𝖠𝗇𝖽 𝖳𝖵 𝖲𝗁𝗈𝗐𝗌 !\n
<blockquote>𝘕𝘰𝘵𝘦: 𝘈𝘭𝘭 𝘵𝘩𝘦 𝘧𝘪𝘭𝘦𝘴 𝘪𝘯 𝘵𝘩𝘪𝘴 𝘣𝘰𝘵 𝘢𝘳𝘦 𝘧𝘳𝘦𝘦𝘭𝘺 𝘢𝘷𝘢𝘪𝘭𝘢𝘣𝘭𝘦 𝘰𝘯 𝘵𝘩𝘦 𝘪𝘯𝘵𝘦𝘳𝘯𝘦𝘵 𝘰𝘳 𝘱𝘰𝘴𝘵𝘦𝘥 𝘣𝘺 𝘴𝘰𝘮𝘦𝘣𝘰𝘥𝘺 𝘦𝘭𝘴𝘦. 𝘛𝘩𝘪𝘴 𝘣𝘰𝘵 𝘪𝘴 𝘪𝘯𝘥𝘦𝘹𝘪𝘯𝘨 𝘧𝘪𝘭𝘦𝘴 𝘸𝘩𝘪𝘤𝘩 𝘢𝘳𝘦 𝘢𝘭𝘳𝘦𝘢𝘥𝘺 𝘶𝘱𝘭𝘰𝘢𝘥𝘦𝘥 𝘰𝘯 𝘵𝘦𝘭𝘦𝘨𝘳𝘢𝘮 𝘧𝘰𝘳 𝘦𝘢𝘴𝘦 𝘰𝘧 𝘴𝘦𝘢𝘳𝘤𝘩𝘪𝘯𝘨. </blockquote>\n
<b><blockquote>♨️ 𝖯𝗈𝗐𝖾𝗋𝖾𝖽 𝖡𝗒  »  「 @OTTProvider 」</blockquote>
</b>"""
    
    HELP_TXT = """<b>ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴜᴛᴛᴏɴꜱ ʙᴇʟᴏᴡ ᴛᴏ ɢᴇᴛ ᴅᴏᴄᴜᴍᴇɴᴛᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ꜱᴘᴇᴄɪꜰɪᴄ ᴍᴏᴅᴜʟᴇꜱ..</b>"""
    
    TELE_TXT = """<b>/telegraph - sᴇɴᴅ ᴍᴇ ᴘɪᴄᴛᴜʀᴇ ᴏʀ ᴠɪᴅᴇᴏ ᴜɴᴅᴇʀ (5ᴍʙ)

ɴᴏᴛᴇ - ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴡᴏʀᴋ ɪɴ ʙᴏᴛʜ ɢʀᴏᴜᴘs ᴀɴᴅ ʙᴏᴛ ᴘᴍ</b>"""
    FSUB_TXT = """<b>• ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀɴᴅ ᴍᴀᴋᴇ ᴍᴇ ᴀɴ ᴀᴅᴍɪɴ 😗
• ᴍᴀᴋᴇ ᴍᴇ ᴀɴ ᴀᴅᴍɪɴ ɪɴ ʏᴏᴜʀ ᴛᴀʀɢᴇᴛ ғᴏʀᴄᴇ sᴜʙsᴄʀɪʙᴇ ᴄʜᴀɴɴᴇʟ ᴏʀ Gʀᴏᴜᴘ  😉
• sᴇɴᴅ /fsub ʏᴏᴜʀ_ᴛᴀʀɢᴇᴛ_ᴄʜᴀᴛ_ɪᴅ
ᴇx: <code>/fsub -100xxxxxx</code>

ɴᴏᴡ ɪᴛ's ᴅᴏɴᴇ.ɪ ᴡɪʟʟ ᴄᴏᴍᴘᴇʟ ʏᴏᴜʀ ᴜsᴇʀs ᴛᴏ ᴊᴏɪɴ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ/ɢʀᴏᴜᴘ, ᴀɴᴅ I ᴡɪʟʟ ɴᴏᴛ ᴘʀᴏᴠɪᴅᴇ ᴀɴʏ ғɪʟᴇs ᴜɴᴛɪʟ ʏᴏᴜʀ ᴜsᴇʀs ᴊᴏɪɴ ʏᴏᴜʀ ᴛᴀʀɢᴇᴛ ᴄʜᴀɴɴᴇʟ.

ᴛᴏ ᴅɪsᴀʙʟᴇ ғsᴜʙ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ, sɪᴍᴘʟʏ sᴇɴᴅ <code>/del_fsub</code>

ᴛᴏ ᴄʜᴇᴄᴋ ɪғ ғsᴜʙ ɪs ᴄᴏɴɴᴇᴄᴛᴇᴅ ᴏʀ ɴᴏᴛ, ᴜsᴇ <code>/show_fsub</code></b>"""

    FORCESUB_TEXT="""𝖲𝗈𝗋𝗋𝗒 𝖡𝖺𝖻𝖾𝗌 😔

𝖸𝗈𝗎 𝖭𝖾𝖾𝖽 𝖳𝗈 𝖩𝗈𝗂𝗇 𝖬𝗒 𝖢𝗁𝖺𝗇𝗇𝖾𝗅 𝖳𝗈 𝖴𝗌𝖾 𝖬𝖾 !!

𝖢𝗅𝗂𝖼𝗄 𝖳𝗁𝖾 𝖡𝗎𝗍𝗍𝗈𝗇 𝖡𝖾𝗅𝗈𝗐 𝖳𝗈 𝖩𝗈𝗂𝗇 👇"""
    
    TTS_TXT="""
<b>• sᴇɴᴅ /tts ᴛᴏ ᴜsᴇ ᴛʜɪs ғᴇᴀᴛᴜʀᴇ</b>"""

    DISCLAIMER_TXT = """
<b>ᴛʜɪꜱ ɪꜱ ᴀɴ ᴏᴘᴇɴ ꜱᴏᴜʀᴄᴇ ᴘʀᴏᴊᴇᴄᴛ.

ᴀʟʟ ᴛʜᴇ ꜰɪʟᴇꜱ ɪɴ ᴛʜɪꜱ ʙᴏᴛ ᴀʀᴇ ꜰʀᴇᴇʟʏ ᴀᴠᴀɪʟᴀʙʟᴇ ᴏɴ ᴛʜᴇ ɪɴᴛᴇʀɴᴇᴛ ᴏʀ ᴘᴏꜱᴛᴇᴅ ʙʏ ꜱᴏᴍᴇʙᴏᴅʏ ᴇʟꜱᴇ. ᴊᴜꜱᴛ ꜰᴏʀ ᴇᴀꜱʏ ꜱᴇᴀʀᴄʜɪɴɢ ᴛʜɪꜱ ʙᴏᴛ ɪꜱ ɪɴᴅᴇxɪɴɢ ꜰɪʟᴇꜱ ᴡʜɪᴄʜ ᴀʀᴇ ᴀʟʀᴇᴀᴅʏ ᴜᴘʟᴏᴀᴅᴇᴅ ᴏɴ ᴛᴇʟᴇɢʀᴀᴍ. ᴡᴇ ʀᴇꜱᴘᴇᴄᴛ ᴀʟʟ ᴛʜᴇ ᴄᴏᴘʏʀɪɢʜᴛ ʟᴀᴡꜱ ᴀɴᴅ ᴡᴏʀᴋꜱ ɪɴ ᴄᴏᴍᴘʟɪᴀɴᴄᴇ ᴡɪᴛʜ ᴅᴍᴄᴀ ᴀɴᴅ ᴇᴜᴄᴅ. ɪꜰ ᴀɴʏᴛʜɪɴɢ ɪꜱ ᴀɢᴀɪɴꜱᴛ ʟᴀᴡ ᴘʟᴇᴀꜱᴇ ᴄᴏɴᴛᴀᴄᴛ ᴍᴇ ꜱᴏ ᴛʜᴀᴛ ɪᴛ ᴄᴀɴ ʙᴇ ʀᴇᴍᴏᴠᴇᴅ ᴀꜱᴀᴘ. ɪᴛ ɪꜱ ꜰᴏʀʙɪʙʙᴇɴ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ, ꜱᴛʀᴇᴀᴍ, ʀᴇᴘʀᴏᴅᴜᴄᴇ, ꜱʜᴀʀᴇ ᴏʀ ᴄᴏɴꜱᴜᴍᴇ ᴄᴏɴᴛᴇɴᴛ ᴡɪᴛʜᴏᴜᴛ ᴇxᴘʟɪᴄɪᴛ ᴘᴇʀᴍɪꜱꜱɪᴏɴ ꜰʀᴏᴍ ᴛʜᴇ ᴄᴏɴᴛᴇɴᴛ ᴄʀᴇᴀᴛᴏʀ ᴏʀ ʟᴇɢᴀʟ ᴄᴏᴘʏʀɪɢʜᴛ ʜᴏʟᴅᴇʀ. ɪꜰ ʏᴏᴜ ʙᴇʟɪᴇᴠᴇ ᴛʜɪꜱ ʙᴏᴛ ɪꜱ ᴠɪᴏʟᴀᴛɪɴɢ ʏᴏᴜʀ ɪɴᴛᴇʟʟᴇᴄᴛᴜᴀʟ ᴘʀᴏᴘᴇʀᴛʏ, ᴄᴏɴᴛᴀᴄᴛ ᴛʜᴇ ʀᴇꜱᴘᴇᴄᴛɪᴠᴇ ᴄʜᴀɴɴᴇʟꜱ ꜰᴏʀ ʀᴇᴍᴏᴠᴀʟ. ᴛʜᴇ ʙᴏᴛ ᴅᴏᴇꜱ ɴᴏᴛ ᴏᴡɴ ᴀɴʏ ᴏꜰ ᴛʜᴇꜱᴇ ᴄᴏɴᴛᴇɴᴛꜱ, ɪᴛ ᴏɴʟʏ ɪɴᴅᴇx ᴛʜᴇ ꜰɪʟᴇꜱ ꜰʀᴏᴍ ᴛᴇʟᴇɢʀᴀᴍ. 

<blockquote>🌿 ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ : OTTProvider</blockquote>"""
    

    ABOUT_TEXT = """𝖧𝖾𝗒 𝖡𝖺𝖻𝗒𝖦𝗂𝗋𝗅 😘 {},
    
○ 𝖬𝗒 𝖭𝖺𝗆𝖾 : 𝖮𝖳𝖳𝖯𝗋𝗈𝗏𝗂𝖽𝖾𝗋 𝖲𝖾𝖺𝗋𝖼𝗁 𝖡𝗈𝗍
○ 𝖬𝗒 𝖮𝗐𝗇𝖾𝗋 : 𝖲𝗁𝗂𝖻𝖺𝗆 & 𝖠𝗇𝗌𝗁𝗎
○ 𝖬𝗒 𝖡𝖾𝗌𝗍 𝖥𝗋𝗂𝖾𝗇𝖽 : <a href='tg://settings'>𝖳𝗁𝗂𝗌 𝖯𝖾𝗋𝗌𝗈𝗇</a>
○ 𝖬𝗒 𝖢𝗁𝖺𝗇𝗇𝖾𝗅 : <a href='https://t.me/OTTProvider'>@𝖮𝖳𝖳𝖯𝗋𝗈𝗏𝗂𝖽𝖾𝗋</a>"""    
    
    SUPPORT_GRP_MOVIE_TEXT = '''<b>ʜᴇʏ {}

ɪ ғᴏᴜɴᴅ {} ʀᴇsᴜʟᴛs 🎁,
ʙᴜᴛ ɪ ᴄᴀɴ'ᴛ sᴇɴᴅ ʜᴇʀᴇ 🤞🏻
ᴘʟᴇᴀsᴇ ᴊᴏɪɴ ᴏᴜʀ ʀᴇǫᴜᴇsᴛ ɢʀᴏᴜᴘ ᴛᴏ ɢᴇᴛ ✨</b>'''

    CHANNELS = """
<u>ᴏᴜʀ ᴀʟʟ ɢʀᴏᴜᴘꜱ ᴀɴᴅ ᴄʜᴀɴɴᴇʟꜱ</u> 

▫ ᴀʟʟ ʟᴀᴛᴇꜱᴛ ᴀɴᴅ ᴏʟᴅ ᴍᴏᴠɪᴇꜱ & ꜱᴇʀɪᴇꜱ.
▫ ᴀʟʟ ʟᴀɴɢᴜᴀɢᴇꜱ ᴍᴏᴠɪᴇꜱ ᴀᴠᴀɪʟᴀʙʟᴇ.
▫ ᴀʟᴡᴀʏꜱ ᴀᴅᴍɪɴ ꜱᴜᴘᴘᴏʀᴛ.
▫ 𝟸𝟺x𝟽 ꜱᴇʀᴠɪᴄᴇꜱ ᴀᴠᴀɪʟᴀʙʟᴇ."""

    LOGO = """

BOT WORKING PROPERLY 🔥"""
    
    RESTART_TXT = """
<b>𝖡𝗈𝗍 𝖱𝖾𝗌𝗍𝖺𝗋𝗍𝖾𝖽 !</b>

📅 𝖣𝖺𝗍𝖾 : <code>{}</code>
⏰ 𝖳𝗂𝗆𝖾 : <code>{}</code>
🌐 𝖳𝗂𝗆𝖾𝗓𝗈𝗇𝖾 : <code>Asia/Kolkata</code>
🛠️ 𝖡𝗎𝗂𝗅𝖽 𝖲𝗍𝖺𝗍𝗎𝗌 : <code>𝗏2.7.3 [ 𝖲𝗍𝖺𝖻𝗅𝖾 ]</code></b>"""
        
    
    STATUS_TXT = """<blockquote><b>👥  𝖴𝗌𝖾𝗋𝗌  𝖣𝖺𝗍𝖺𝖻𝖺𝗌𝖾 ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ </b></blockquote>
›  𝖳𝗈𝗍𝖺𝗅 𝖴𝗌𝖾𝗋𝗌: <code>{}</code>
›  𝖳𝗈𝗍𝖺𝗅 𝖢𝗁𝖺𝗍𝗌: <code>{}</code>
›  𝖴𝗌𝖾𝖽 𝖲𝗍𝗈𝗋𝖺𝗀𝖾: <code>{} / {}</code>

<blockquote><b>📁  𝖥𝗂𝗅𝖾  𝖣𝖺𝗍𝖺𝖻𝖺𝗌𝖾  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎  </b></blockquote>
›  𝖳𝗈𝗍𝖺𝗅 𝖥𝗂𝗅𝖾𝗌: <code>{}</code>
›  𝖴𝗌𝖾𝖽 𝖲𝗍𝗈𝗋𝖺𝗀𝖾: <code>{} / {}</code>

<blockquote><b>📊  𝖡𝗈𝗍 𝖲𝗍𝖺𝗍𝗌  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ </b></blockquote>
» 𝖴𝗉𝗍𝗂𝗆𝖾 - <code>{}</code>
» 𝖱𝖠𝖬  - <code>{}%</code>
» 𝖢𝖯𝖴 - <code>{}%</code>"""

    NEW_USER_TXT = """#NewUser {}

𝖨𝖽 - <code>{}</code>
𝖭𝖺𝗆𝖾 - {}"""

    NEW_GROUP_TXT = """#New_Group {}

Group name - {}
Id - <code>{}</code>
Group username - @{}
Group link - {}
Total members - <code>{}</code>
User - {}"""

    REQUEST_TXT = """<b>📜 ᴜꜱᴇʀ - {}
📇 ɪᴅ - <code>{}</code>

🎁 ʀᴇǫᴜᴇꜱᴛ ᴍꜱɢ - <code>{}</code></b>"""  
   
    IMDB_TEMPLATE_TXT = """
<b>ʜᴇʏ {message.from_user.mention}, ʜᴇʀᴇ ɪꜱ ᴛʜᴇ ʀᴇꜱᴜʟᴛꜱ ꜰᴏʀ ʏᴏᴜʀ ǫᴜᴇʀʏ {search}.

🍿 Title: {title}
🎃 Genres: {genres}
📆 Year: {release_date}
⭐ Rating: {rating} / 10</b>
"""

    FILE_CAPTION = """`{file_name}`\n\n<blockquote>#𝙊𝙏𝙏𝙋𝙧𝙤𝙫𝙞𝙙𝙚𝙧 – 𝘔𝘰𝘴𝘵 𝘛𝘳𝘶𝘴𝘵𝘦𝘥 𝘗𝘳𝘦𝘮𝘪𝘶𝘮 𝘔𝘰𝘷𝘪𝘦𝘴 𝘈𝘯𝘥 𝘞𝘦𝘣 𝘚𝘦𝘳𝘪𝘦𝘴 𝘌𝘯𝘵𝘦𝘳𝘵𝘢𝘪𝘯𝘮𝘦𝘯𝘵 𝘕𝘦𝘵𝘸𝘰𝘳𝘬 𝘖𝘯 𝘛𝘦𝘭𝘦𝘨𝘳𝘢𝘮.</blockquote>\n\n<b><i>⏤͟͞𝗝⌡𝗼𝗶𝗻 𝗣𝗿𝗲𝗺𝗶𝘂𝗺  – </i>「 @OTTProvider 」</b>"""
    

    ALRT_TXT = """𝖳𝗁𝗂𝗌 𝗂𝗌 𝗇𝗈𝗍 𝗒𝗈𝗎𝗋 𝗆𝗈𝗏𝗂𝖾 𝗋𝖾𝗊𝗎𝖾𝗌𝗍,
𝖱𝖾𝗊𝗎𝖾𝗌𝗍 𝗒𝗈𝗎𝗋𝗌..."""

    OLD_ALRT_TXT = """𝖸ou are using one of my old messages, please send the request again."""

    NO_RESULT_TXT = """𝖬𝗈𝗏𝗂𝖾 𝗇𝗈𝗍 𝖿𝗈𝗎𝗇𝖽 𝗂𝗇 𝖽𝖺𝗍𝖺𝖻𝖺𝗌𝖾... 𝖯𝗅𝖾𝖺𝗌𝖾 𝖼𝗈𝗇𝗍𝖺𝖼𝗍 𝗈𝗎𝗋 𝖺𝖽𝗆𝗂𝗇 😔\n\n‼ <b><i>𝖱𝖾𝗉𝗈𝗋𝗍 𝗍𝗈 𝖺𝖽𝗆𝗂𝗇 ▶ @OTTProviderSupportBot</i></b>"""
    
    I_CUDNT = """𝖲𝗈𝗋𝗋𝗒, 𝗇𝗈 𝖿𝗂𝗅𝖾𝗌 𝗐𝖾𝗋𝖾 𝖿𝗈𝗎𝗇𝖽 𝖿𝗈𝗋 𝗒𝗈𝗎𝗋 𝗋𝖾𝗊𝗎𝖾𝗌𝗍 {} 😕
𝖢𝗁𝖾𝖼𝗄 𝗒𝗈𝗎𝗋 𝗌𝗉𝖾𝗅𝗅𝗂𝗇𝗀 𝗂𝗇 𝖦𝗈𝗈𝗀𝗅𝖾 𝖺𝗇𝖽 𝗍𝗋𝗒 𝖺𝗀𝖺𝗂𝗇 😃\n\n‼ <b><i>𝖱𝖾𝗉𝗈𝗋𝗍 𝗍𝗈 𝖺𝖽𝗆𝗂𝗇 ▶ @OTTProviderSupportBot</i></b>"""

    I_CUD_NT = """𝖲𝗈𝗋𝗋𝗒, 𝗇𝗈 𝖿𝗂𝗅𝖾𝗌 𝗐𝖾𝗋𝖾 𝖿𝗈𝗎𝗇𝖽 𝖿𝗈𝗋 𝗒𝗈𝗎𝗋 𝗋𝖾𝗊𝗎𝖾𝗌𝗍 {} 😕
𝖢𝗁𝖾𝖼𝗄 𝗒𝗈𝗎𝗋 𝗌𝗉𝖾𝗅𝗅𝗂𝗇𝗀 𝗂𝗇 𝖦𝗈𝗈𝗀𝗅𝖾 𝖺𝗇𝖽 𝗍𝗋𝗒 𝖺𝗀𝖺𝗂𝗇 😃\n\n‼ <b><i>𝖱𝖾𝗉𝗈𝗋𝗍 𝗍𝗈 𝖺𝖽𝗆𝗂𝗇 ▶ @OTTProviderSupportBot</i></b>"""
    
    CUDNT_FND = """𝖨 𝖼𝗈𝗎𝗅𝖽𝗇'𝗍 𝖿𝗂𝗇𝖽 𝖺𝗇𝗒𝗍𝗁𝗂𝗇𝗀 𝗋𝖾𝗅𝖺𝗍𝖾𝖽 𝗍𝗈 {}
𝖣𝗂𝖽 𝗒𝗈𝗎 𝗆𝖾𝖺𝗇 𝖺𝗇𝗒 𝗈𝗇𝖾 𝗈𝖿 𝗍𝗁𝖾𝗌𝖾 ?\n\n‼ <b><i>𝖱𝖾𝗉𝗈𝗋𝗍 𝗍𝗈 𝖺𝖽𝗆𝗂𝗇 ▶ @OTTProviderSupportBot</i></b>"""
    
    FONT_TXT= """<b>ʏᴏᴜ ᴄᴀɴ ᴜsᴇ ᴛʜɪs ᴍᴏᴅᴇ ᴛᴏ ᴄʜᴀɴɢᴇ ʏᴏᴜʀ ꜰᴏɴᴛs sᴛʏʟᴇ, ᴊᴜsᴛ sᴇɴᴅ ᴍᴇ ʟɪᴋᴇ ᴛʜɪs ꜰᴏʀᴍᴀᴛ

<code>/font hi how are you</code></b>"""
    
    PLAN_TEXT = """<b><u>𝗣𝗥𝗘𝗠𝗜𝗨𝗠  𝗦𝗨𝗕𝗦𝗖𝗥𝗜𝗣𝗧𝗜𝗢𝗡  𝗣𝗟𝗔𝗡𝗦</u></b> 🔥


⭕️ <b><u>𝖯𝗋𝖾𝖿𝖾𝗋𝗋𝖾𝖽 𝖯𝗅𝖺𝗇𝗌</u></b>  ‎👇 ‎ ‎ ‎ ‎ ‎ ‎ ‎

<blockquote>〇   01 𝖣𝖺𝗒      ➜                     <b> ₹5/- ‎ ‎ ‎ ‎ ‌‎  ‎ ‎ ‎ ‎ </b>  </blockquote>
<blockquote>〇   01 𝖬𝗈𝗇𝗍𝗁  ➜     <s>₹50/-</s>     <b>₹30/- ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ </b></blockquote>
<blockquote>〇   03 𝖬𝗈𝗇𝗍𝗁  ➜   <s>₹150/-</s>     <b>₹80/- ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ </b>  </blockquote>
<blockquote><b>〇   06 𝖬𝗈𝗇𝗍𝗁  ➜   <s>₹250/-</s>   ₹150/-  😱 ‌‎ ‎ ‎  ‎  </b></blockquote>

⭕️ <b><u>𝖥𝖾𝖺𝗍𝗎𝗋𝖾𝗌</u></b> ‎ ‎ ‎ ‎👇 ‎ ‎ ‎ ‎ ‎ ‎  ‎ 

<blockquote>〇  𝖭𝗈  𝖭𝖾𝖾𝖽  𝖳𝗈  𝖵𝖾𝗋𝗂𝖿𝗒    ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎          ‎ ‎ ‎        </blockquote>
<blockquote>〇  𝖣𝗂𝗋𝖾𝖼𝗍  𝖵𝗂𝖽𝖾𝗈  𝖥𝗂𝗅𝖾𝗌  ‎ ‌‎    ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎         ‎ ‎ ‎         </blockquote>
<blockquote>〇  𝖠𝖽-𝖥𝗋𝖾𝖾  𝖤𝗑𝗉𝖾𝗋𝗂𝖾𝗇𝖼𝖾    ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎          ‎ ‎ ‎            </blockquote>
<blockquote>〇  𝖴𝗇𝗅𝗂𝗆𝗂𝗍𝖾𝖽  𝖱𝖾𝗊𝗎𝖾𝗌𝗍/𝖲𝖾𝖺𝗋𝖼𝗁‎ ‎ ‎ ‎ ‎  ‌‌‎  ‎ ‎  ‎ ‎</blockquote>
<blockquote>〇  𝖠𝖽𝗆𝗂𝗇  𝖲𝗎𝗉𝗉𝗈𝗋𝗍  🗿      ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎     ‎ ‎ ‎ ‎     </blockquote>


<b>👑 𝖶𝖺𝗇𝖺 𝖡𝗎𝗒 𝖲𝗎𝖻𝗌𝖼𝗋𝗂𝗉𝗍𝗂𝗈𝗇... ?</b>

<b>🧑‍💻 𝖢𝗈𝗇𝗍𝖺𝖼𝗍  👉 @LordShibam  
🧑‍💻 𝖢𝗈𝗇𝗍𝖺𝖼𝗍  👉 @LordShibam</b>"""
    
    VERIFICATION_TEXT = """👋 Hey {} {},

🚫 𝖸𝗈𝗎 𝖠𝗋𝖾 𝖭𝗈𝗍 𝖵𝖾𝗋𝗂𝖿𝗂𝖾𝖽 𝖳𝗈𝖽𝖺𝗒 😐

𝖵𝖾𝗋𝗂𝖿𝗒 & 𝖦𝖾𝗍 𝖴𝗇𝗅𝗂𝗆𝗂𝗍𝖾𝖽 𝖠𝖼𝖼𝖾𝗌𝗌 𝖥𝗈𝗋 1 𝖣𝖺𝗒.

#𝖵𝖾𝗋𝗂𝖿𝗂𝖼𝖺𝗍𝗂𝗈𝗇:- 1/3 ✓

<blockquote>𝖨𝖿 𝖸𝗈𝗎 𝖠𝗋𝖾 𝖧𝖺𝗏𝗂𝗇𝗀 𝖠𝗇𝗒 𝖯𝗋𝗈𝖻𝗅𝖾𝗆𝗌 𝖶𝗂𝗍𝗁 𝖵𝖾𝗋𝗂𝖿𝗂𝖼𝖺𝗍𝗂𝗈𝗇, 𝖳𝗁𝖾𝗇 𝖢𝗈𝗇𝗍𝖺𝖼𝗍 @OTTProviderSupportBot 𝖠𝗇𝖽 𝖠𝗌𝗄 𝖥𝗈𝗋 𝖧𝖾𝗅𝗉.</blockquote>

<blockquote>𝗕𝘂𝘆 𝗣𝗿𝗲𝗺𝗶𝘂𝗺 𝗧𝗼 𝗥𝗲𝗺𝗼𝘃𝗲 𝗔𝗱𝘀 🔥</blockquote>"""

    VERIFY_COMPLETE_TEXT = """<b>👋 𝖧𝖾𝗒 {},

𝖸𝗈𝗎 𝖧𝖺𝗏𝖾 𝖢𝗈𝗆𝗉𝗅𝖾𝗍𝖾𝖽 𝖳𝗁𝖾 1𝗌𝗍 𝖵𝖾𝗋𝗂𝖿𝗂𝖼𝖺𝗍𝗂𝗈𝗇 ✓

𝖭𝗈𝗐 𝖸𝗈𝗎 𝖧𝖺𝗏𝖾 𝖴𝗇𝗅𝗂𝗆𝗂𝗍𝖾𝖽 𝖠𝖼𝖼𝖾𝗌𝗌 𝖥𝗈𝗋 𝖭𝖾𝗑𝗍 <code>{}</code></b>"""

    SECOND_VERIFICATION_TEXT = """👋 Hey {} {},

🚫 𝖸𝗈𝗎 𝖠𝗋𝖾 𝖭𝗈𝗍 𝖵𝖾𝗋𝗂𝖿𝗂𝖾𝖽 𝖳𝗈𝖽𝖺𝗒 😐

𝖵𝖾𝗋𝗂𝖿𝗒 & 𝖦𝖾𝗍 𝖴𝗇𝗅𝗂𝗆𝗂𝗍𝖾𝖽 𝖠𝖼𝖼𝖾𝗌𝗌 𝖥𝗈𝗋 1 𝖣𝖺𝗒.

#𝖵𝖾𝗋𝗂𝖿𝗂𝖼𝖺𝗍𝗂𝗈𝗇:- 2/3 ✓

<blockquote>𝖨𝖿 𝖸𝗈𝗎 𝖠𝗋𝖾 𝖧𝖺𝗏𝗂𝗇𝗀 𝖠𝗇𝗒 𝖯𝗋𝗈𝖻𝗅𝖾𝗆𝗌 𝖶𝗂𝗍𝗁 𝖵𝖾𝗋𝗂𝖿𝗂𝖼𝖺𝗍𝗂𝗈𝗇, 𝖳𝗁𝖾𝗇 𝖢𝗈𝗇𝗍𝖺𝖼𝗍 @OTTProviderSupportBot 𝖠𝗇𝖽 𝖠𝗌𝗄 𝖥𝗈𝗋 𝖧𝖾𝗅𝗉.</blockquote>

<blockquote>𝗕𝘂𝘆 𝗣𝗿𝗲𝗺𝗶𝘂𝗺 𝗧𝗼 𝗥𝗲𝗺𝗼𝘃𝗲 𝗔𝗱𝘀 🔥</blockquote>"""

    SECOND_VERIFY_COMPLETE_TEXT = """<b>👋 𝖧𝖾𝗒 {},

𝖸𝗈𝗎 𝖧𝖺𝗏𝖾 𝖢𝗈𝗆𝗉𝗅𝖾𝗍𝖾𝖽 𝖳𝗁𝖾 2𝗇𝖽 𝖵𝖾𝗋𝗂𝖿𝗂𝖼𝖺𝗍𝗂𝗈𝗇 ✓

𝖭𝗈𝗐 𝖸𝗈𝗎 𝖧𝖺𝗏𝖾 𝖴𝗇𝗅𝗂𝗆𝗂𝗍𝖾𝖽 𝖠𝖼𝖼𝖾𝗌𝗌 𝖥𝗈𝗋 𝖭𝖾𝗑𝗍 <code>{}</code></b>"""

    THIRDT_VERIFICATION_TEXT = """👋 Hey {} {},

🚫 𝖸𝗈𝗎 𝖠𝗋𝖾 𝖭𝗈𝗍 𝖵𝖾𝗋𝗂𝖿𝗂𝖾𝖽 𝖳𝗈𝖽𝖺𝗒 😐

𝖵𝖾𝗋𝗂𝖿𝗒 & 𝖦𝖾𝗍 𝖴𝗇𝗅𝗂𝗆𝗂𝗍𝖾𝖽 𝖠𝖼𝖼𝖾𝗌𝗌 𝖥𝗈𝗋 1 𝖣𝖺𝗒.

#𝖵𝖾𝗋𝗂𝖿𝗂𝖼𝖺𝗍𝗂𝗈𝗇:- 3/3 ✓

<blockquote>𝖨𝖿 𝖸𝗈𝗎 𝖠𝗋𝖾 𝖧𝖺𝗏𝗂𝗇𝗀 𝖠𝗇𝗒 𝖯𝗋𝗈𝖻𝗅𝖾𝗆𝗌 𝖶𝗂𝗍𝗁 𝖵𝖾𝗋𝗂𝖿𝗂𝖼𝖺𝗍𝗂𝗈𝗇, 𝖳𝗁𝖾𝗇 𝖢𝗈𝗇𝗍𝖺𝖼𝗍 @OTTProviderSupportBot 𝖠𝗇𝖽 𝖠𝗌𝗄 𝖥𝗈𝗋 𝖧𝖾𝗅𝗉.</blockquote>

<blockquote>𝗕𝘂𝘆 𝗣𝗿𝗲𝗺𝗶𝘂𝗺 𝗧𝗼 𝗥𝗲𝗺𝗼𝘃𝗲 𝗔𝗱𝘀 🔥</blockquote></b>"""

    THIRDT_VERIFY_COMPLETE_TEXT= """<b>👋 𝖧𝖾𝗒 {},

𝖸𝗈𝗎 𝖧𝖺𝗏𝖾 𝖢𝗈𝗆𝗉𝗅𝖾𝗍𝖾𝖽 𝖳𝗁𝖾 3𝗋𝖽 𝖵𝖾𝗋𝗂𝖿𝗂𝖼𝖺𝗍𝗂𝗈𝗇 ✓

𝖭𝗈𝗐 𝖸𝗈𝗎 𝖧𝖺𝗏𝖾 𝖴𝗇𝗅𝗂𝗆𝗂𝗍𝖾𝖽 𝖠𝖼𝖼𝖾𝗌𝗌 𝖥𝗈𝗋 𝖭𝖾𝗑𝗍 <code>{}</code></b>"""

    VERIFIED_LOG_TEXT = """<b><u>🔥 𝖴𝗌𝖾𝗋 𝖵𝖾𝗋𝗂𝖿𝗂𝖾𝖽 𝖲𝗎𝖼𝖼𝖾𝗌𝗌𝖿𝗎𝗅𝗅𝗒</u>

⚡️ 𝖭𝖺𝗆𝖾  :- {} [ <code>{}</code> ] 
📆 𝖣𝖺𝗍𝖾 :- <code>{} </code></b>

#𝖵𝖾𝗋𝗂𝖿𝗂𝖾𝖽_{}_𝖢𝗈𝗆𝗉𝗅𝖾𝗍𝖾𝖽"""


    MOVIES_UPDATE_TXT = """<b>#𝑵𝒆𝒘_𝑭𝒊𝒍𝒆_𝑨𝒅𝒅𝒆𝒅 ✅
**🍿 Title:** {title}
**🎃 Genres:** {genres}
**📆 Year:** {year}
**⭐ Rating:** {rating} / 10
</b>"""

    PREPLANS_TXT = """<b><u>𝗣𝗥𝗘𝗠𝗜𝗨𝗠  𝗦𝗨𝗕𝗦𝗖𝗥𝗜𝗣𝗧𝗜𝗢𝗡  𝗣𝗟𝗔𝗡𝗦</u></b> 🔥


⭕️ <b><u>𝖯𝗋𝖾𝖿𝖾𝗋𝗋𝖾𝖽 𝖯𝗅𝖺𝗇𝗌</u></b>  ‎👇 ‎ ‎ ‎ ‎ ‎ ‎ ‎

<blockquote>〇   01 𝖣𝖺𝗒      ➜                     <b> ₹5/- ‎ ‎ ‎ ‎ ‌‎  ‎ ‎ ‎ ‎ </b>  </blockquote>
<blockquote>〇   01 𝖬𝗈𝗇𝗍𝗁  ➜     <s>₹50/-</s>     <b>₹30/- ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ </b></blockquote>
<blockquote>〇   03 𝖬𝗈𝗇𝗍𝗁  ➜   <s>₹150/-</s>     <b>₹80/- ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ </b>  </blockquote>
<blockquote><b>〇   06 𝖬𝗈𝗇𝗍𝗁  ➜   <s>₹250/-</s>   ₹150/-  😱 ‌‎ ‎ ‎  ‎  </b></blockquote>

⭕️ <b><u>𝖥𝖾𝖺𝗍𝗎𝗋𝖾𝗌</u></b> ‎ ‎ ‎ ‎👇 ‎ ‎ ‎ ‎ ‎ ‎  ‎ 

<blockquote>〇  𝖭𝗈  𝖭𝖾𝖾𝖽  𝖳𝗈  𝖵𝖾𝗋𝗂𝖿𝗒    ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎          ‎ ‎ ‎        </blockquote>
<blockquote>〇  𝖣𝗂𝗋𝖾𝖼𝗍  𝖵𝗂𝖽𝖾𝗈  𝖥𝗂𝗅𝖾𝗌  ‎ ‌‎    ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎         ‎ ‎ ‎         </blockquote>
<blockquote>〇  𝖠𝖽-𝖥𝗋𝖾𝖾  𝖤𝗑𝗉𝖾𝗋𝗂𝖾𝗇𝖼𝖾    ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎          ‎ ‎ ‎            </blockquote>
<blockquote>〇  𝖴𝗇𝗅𝗂𝗆𝗂𝗍𝖾𝖽  𝖱𝖾𝗊𝗎𝖾𝗌𝗍/𝖲𝖾𝖺𝗋𝖼𝗁‎ ‎ ‎ ‎ ‎  ‌‌‎  ‎ ‎  ‎ ‎</blockquote>
<blockquote>〇  𝖠𝖽𝗆𝗂𝗇  𝖲𝗎𝗉𝗉𝗈𝗋𝗍  🗿      ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎     ‎ ‎ ‎ ‎     </blockquote>


<b>👑 𝖶𝖺𝗇𝖺 𝖡𝗎𝗒 𝖲𝗎𝖻𝗌𝖼𝗋𝗂𝗉𝗍𝗂𝗈𝗇... ?</b>

<b>🧑‍💻 𝖢𝗈𝗇𝗍𝖺𝖼𝗍  👉 @LordShibam  
🧑‍💻 𝖢𝗈𝗇𝗍𝖺𝖼𝗍  👉 @LordShibam</b>"""    

    PREPLANSS_TXT = """<b><u>𝗣𝗥𝗘𝗠𝗜𝗨𝗠  𝗦𝗨𝗕𝗦𝗖𝗥𝗜𝗣𝗧𝗜𝗢𝗡  𝗣𝗟𝗔𝗡𝗦</u></b> 🔥


⭕️ <b><u>𝖯𝗋𝖾𝖿𝖾𝗋𝗋𝖾𝖽 𝖯𝗅𝖺𝗇𝗌</u></b>  ‎👇 ‎ ‎ ‎ ‎ ‎ ‎ ‎

<blockquote>〇   01 𝖣𝖺𝗒      ➜                     <b> ₹5/- ‎ ‎ ‎ ‎ ‌‎  ‎ ‎ ‎ ‎ </b>  </blockquote>
<blockquote>〇   01 𝖬𝗈𝗇𝗍𝗁  ➜     <s>₹50/-</s>     <b>₹30/- ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ </b></blockquote>
<blockquote>〇   03 𝖬𝗈𝗇𝗍𝗁  ➜   <s>₹150/-</s>     <b>₹80/- ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ </b>  </blockquote>
<blockquote><b>〇   06 𝖬𝗈𝗇𝗍𝗁  ➜   <s>₹250/-</s>   ₹150/-  😱 ‌‎ ‎ ‎  ‎  </b></blockquote>

⭕️ <b><u>𝖥𝖾𝖺𝗍𝗎𝗋𝖾𝗌</u></b> ‎ ‎ ‎ ‎👇 ‎ ‎ ‎ ‎ ‎ ‎  ‎ 

<blockquote>〇  𝖭𝗈  𝖭𝖾𝖾𝖽  𝖳𝗈  𝖵𝖾𝗋𝗂𝖿𝗒    ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎          ‎ ‎ ‎        </blockquote>
<blockquote>〇  𝖣𝗂𝗋𝖾𝖼𝗍  𝖵𝗂𝖽𝖾𝗈  𝖥𝗂𝗅𝖾𝗌  ‎ ‌‎    ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎         ‎ ‎ ‎         </blockquote>
<blockquote>〇  𝖠𝖽-𝖥𝗋𝖾𝖾  𝖤𝗑𝗉𝖾𝗋𝗂𝖾𝗇𝖼𝖾    ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎          ‎ ‎ ‎            </blockquote>
<blockquote>〇  𝖴𝗇𝗅𝗂𝗆𝗂𝗍𝖾𝖽  𝖱𝖾𝗊𝗎𝖾𝗌𝗍/𝖲𝖾𝖺𝗋𝖼𝗁‎ ‎ ‎ ‎ ‎  ‌‌‎  ‎ ‎  ‎ ‎</blockquote>
<blockquote>〇  𝖠𝖽𝗆𝗂𝗇  𝖲𝗎𝗉𝗉𝗈𝗋𝗍  🗿      ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎     ‎ ‎ ‎ ‎     </blockquote>


<b>👑 𝖶𝖺𝗇𝖺 𝖡𝗎𝗒 𝖲𝗎𝖻𝗌𝖼𝗋𝗂𝗉𝗍𝗂𝗈𝗇... ?</b>

<b>🧑‍💻 𝖢𝗈𝗇𝗍𝖺𝖼𝗍  👉 @LordShibam  
🧑‍💻 𝖢𝗈𝗇𝗍𝖺𝖼𝗍  👉 @LordShibam</b>"""

    OTHER_TXT = """<b><u>𝗣𝗥𝗘𝗠𝗜𝗨𝗠  𝗦𝗨𝗕𝗦𝗖𝗥𝗜𝗣𝗧𝗜𝗢𝗡  𝗣𝗟𝗔𝗡𝗦</u></b> 🔥


⭕️ <b><u>𝖯𝗋𝖾𝖿𝖾𝗋𝗋𝖾𝖽 𝖯𝗅𝖺𝗇𝗌</u></b>  ‎👇 ‎ ‎ ‎ ‎ ‎ ‎ ‎

<blockquote>〇   01 𝖣𝖺𝗒      ➜                     <b> ₹5/- ‎ ‎ ‎ ‎ ‌‎  ‎ ‎ ‎ ‎ </b>  </blockquote>
<blockquote>〇   01 𝖬𝗈𝗇𝗍𝗁  ➜     <s>₹50/-</s>     <b>₹30/- ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ </b></blockquote>
<blockquote>〇   03 𝖬𝗈𝗇𝗍𝗁  ➜   <s>₹150/-</s>     <b>₹80/- ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ </b>  </blockquote>
<blockquote><b>〇   06 𝖬𝗈𝗇𝗍𝗁  ➜   <s>₹250/-</s>   ₹150/-  😱 ‌‎ ‎ ‎  ‎  </b></blockquote>

⭕️ <b><u>𝖥𝖾𝖺𝗍𝗎𝗋𝖾𝗌</u></b> ‎ ‎ ‎ ‎👇 ‎ ‎ ‎ ‎ ‎ ‎  ‎ 

<blockquote>〇  𝖭𝗈  𝖭𝖾𝖾𝖽  𝖳𝗈  𝖵𝖾𝗋𝗂𝖿𝗒    ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎          ‎ ‎ ‎        </blockquote>
<blockquote>〇  𝖣𝗂𝗋𝖾𝖼𝗍  𝖵𝗂𝖽𝖾𝗈  𝖥𝗂𝗅𝖾𝗌  ‎ ‌‎    ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎         ‎ ‎ ‎         </blockquote>
<blockquote>〇  𝖠𝖽-𝖥𝗋𝖾𝖾  𝖤𝗑𝗉𝖾𝗋𝗂𝖾𝗇𝖼𝖾    ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎          ‎ ‎ ‎            </blockquote>
<blockquote>〇  𝖴𝗇𝗅𝗂𝗆𝗂𝗍𝖾𝖽  𝖱𝖾𝗊𝗎𝖾𝗌𝗍/𝖲𝖾𝖺𝗋𝖼𝗁‎ ‎ ‎ ‎ ‎  ‌‌‎  ‎ ‎  ‎ ‎</blockquote>
<blockquote>〇  𝖠𝖽𝗆𝗂𝗇  𝖲𝗎𝗉𝗉𝗈𝗋𝗍  🗿      ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎     ‎ ‎ ‎ ‎     </blockquote>


<b>👑 𝖶𝖺𝗇𝖺 𝖡𝗎𝗒 𝖲𝗎𝖻𝗌𝖼𝗋𝗂𝗉𝗍𝗂𝗈𝗇... ?</b>

<b>🧑‍💻 𝖢𝗈𝗇𝗍𝖺𝖼𝗍  👉 @LordShibam  
🧑‍💻 𝖢𝗈𝗇𝗍𝖺𝖼𝗍  👉 @LordShibam</b>"""

    FREE_TXT = """<b><u>𝗣𝗥𝗘𝗠𝗜𝗨𝗠  𝗦𝗨𝗕𝗦𝗖𝗥𝗜𝗣𝗧𝗜𝗢𝗡  𝗣𝗟𝗔𝗡𝗦</u></b> 🔥


⭕️ <b><u>𝖯𝗋𝖾𝖿𝖾𝗋𝗋𝖾𝖽 𝖯𝗅𝖺𝗇𝗌</u></b>  ‎👇 ‎ ‎ ‎ ‎ ‎ ‎ ‎

<blockquote>〇   01 𝖣𝖺𝗒      ➜                     <b> ₹5/- ‎ ‎ ‎ ‎ ‌‎  ‎ ‎ ‎ ‎ </b>  </blockquote>
<blockquote>〇   01 𝖬𝗈𝗇𝗍𝗁  ➜     <s>₹50/-</s>     <b>₹30/- ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ </b></blockquote>
<blockquote>〇   03 𝖬𝗈𝗇𝗍𝗁  ➜   <s>₹150/-</s>     <b>₹80/- ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ </b>  </blockquote>
<blockquote><b>〇   06 𝖬𝗈𝗇𝗍𝗁  ➜   <s>₹250/-</s>   ₹150/-  😱 ‌‎ ‎ ‎  ‎  </b></blockquote>

⭕️ <b><u>𝖥𝖾𝖺𝗍𝗎𝗋𝖾𝗌</u></b> ‎ ‎ ‎ ‎👇 ‎ ‎ ‎ ‎ ‎ ‎  ‎ 

<blockquote>〇  𝖭𝗈  𝖭𝖾𝖾𝖽  𝖳𝗈  𝖵𝖾𝗋𝗂𝖿𝗒    ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎          ‎ ‎ ‎        </blockquote>
<blockquote>〇  𝖣𝗂𝗋𝖾𝖼𝗍  𝖵𝗂𝖽𝖾𝗈  𝖥𝗂𝗅𝖾𝗌  ‎ ‌‎    ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎         ‎ ‎ ‎         </blockquote>
<blockquote>〇  𝖠𝖽-𝖥𝗋𝖾𝖾  𝖤𝗑𝗉𝖾𝗋𝗂𝖾𝗇𝖼𝖾    ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎          ‎ ‎ ‎            </blockquote>
<blockquote>〇  𝖴𝗇𝗅𝗂𝗆𝗂𝗍𝖾𝖽  𝖱𝖾𝗊𝗎𝖾𝗌𝗍/𝖲𝖾𝖺𝗋𝖼𝗁‎ ‎ ‎ ‎ ‎  ‌‌‎  ‎ ‎  ‎ ‎</blockquote>
<blockquote>〇  𝖠𝖽𝗆𝗂𝗇  𝖲𝗎𝗉𝗉𝗈𝗋𝗍  🗿      ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎     ‎ ‎ ‎ ‎     </blockquote>


<b>👑 𝖶𝖺𝗇𝖺 𝖡𝗎𝗒 𝖲𝗎𝖻𝗌𝖼𝗋𝗂𝗉𝗍𝗂𝗈𝗇... ?</b>

<b>🧑‍💻 𝖢𝗈𝗇𝗍𝖺𝖼𝗍  👉 @LordShibam  
🧑‍💻 𝖢𝗈𝗇𝗍𝖺𝖼𝗍  👉 @LordShibam</b>"""

    ADMIN_CMD_TXT = """<b><blockquote>
-------------User Premium------------
➩ /add_premium {user ID} {Times} - Add a premium user
➩ /remove_premium {user ID} - Remove a premium user
➩ /add_redeem - Generate a redeem code
➩ /premium_users - List all premium users
➩ /refresh - Refresh free trial for users
-------------Update Channel----------
➩ /set_muc {channel ID} - Set the movies update channel
--------------PM Search--------------
➩ /pm_search_on - Enable PM search
➩ /pm_search_off - Disable PM search
--------------Verify ID--------------
➩ /verify_id - Generate a verification ID for group use only
--------------Set Ads----------------
➩ /set_ads {ads name}}#{Times}#{photo URL} - <a href="https://t.me/Jisshu_developer/11">Explain</a>
➩ /del_ads - Delete ads
-------------Top Trending------------
➩ /setlist {Mirzapur, Money Heist} - <a href=https://t.me/Jisshu_developer/10>Explain</a>
➩ /clearlist - Clear all lists
</blockquote></b>"""

    ADMIN_CMD_TXT2 = """<b><blockquote>
--------------Index File--------------
➩ /index - Index all files
--------------Leave Link--------------
➩ /leave {group ID} - Leave the specified group
-------------Send Message-------------
➩ /send {user-name} - Use this command as a reply to any message
----------------Ban User---------------
➩ /ban {user-name} - Ban user 
➩ /unban {user-name} - Unban user
--------------Broadcast--------------
➩ /broadcast - Broadcast a message to all users
➩ /grp_broadcast - Broadcast a message to all connected groups

</blockquote></b>"""
    
    GROUP_TEXT = """<b><blockquote>
 --------------Set Verify-------------
/set_verify {{website link}} {{website api}}
/set_verify_2 {{website link}} {{website api}}
/set_verify_3 {{website link}} {{website api}}
-------------Set Verify Time-----------
/set_time_2 {{seconds}} Sᴇᴛ ᴛʜᴇ sᴇᴄᴏɴᴅ ᴠᴇʀɪғɪᴄᴀᴛɪᴏɴ ᴛɪᴍᴇ
/set_time_3 {{seconds}} Sᴇᴛ ᴛʜᴇ ᴛʜɪʀᴅ ᴠᴇʀɪғɪᴄᴀᴛɪᴏɴ ᴛɪᴍᴇ
--------------Verify On Off------------
/verifyoff {{verify.off code}} - off verification <a href="https://t.me/IM_JISSHU">Cᴏɴᴛᴀᴄᴛ</a> ᴛʜᴇ ʙᴏᴛ ᴀᴅᴍɪɴ ғᴏʀ ᴀ ᴠᴇʀɪғʏ.ᴏғғ ᴄᴏᴅᴇ
/verifyon - on verification 
------------Set File Caption-----------
/set_caption - set coustom file caption 
-----------Set Imdb Template-----------
/set_template - set IMDb template <a href="https://t.me/Jisshu_developer/8">Example</a>
--------------Set Tutorial-------------
/set_tutorial - set verification tutorial 
-------------Set Log Channel-----------
--> ᴀᴅᴅ ʟᴏɢ ᴄʜᴀɴɴᴇʟ ʙʏ ᴛʜɪs ꜰᴏʀᴍᴀᴛ & ᴍᴀᴋᴇ sᴜʀᴇ ʙᴏᴛ ɪs ᴀᴅᴍɪɴ ɪɴ ʏᴏᴜʀ ʟᴏɢ ᴄʜᴀɴɴᴇʟ 👇

/set_log {{log channel id}}
---------------------------------------
ʏᴏᴜ ᴄᴀɴ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴀʟʟ ᴅᴇᴛᴀɪʟs 
ʙʏ /details ᴄᴏᴍᴍᴀɴᴅ
</blockquote>
Aᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀɴᴅ ᴍᴀᴋᴇ ᴍᴇ ᴀᴅᴍɪɴ ᴀɴᴅ ᴜsᴇ ᴀʟʟ ғᴇᴀᴛᴜʀᴇs😇</b>"""

    SOURCE_TXT = """<b>
NOTE:
- Create Your Bot ◉› :<blockquote><a href="https://youtu.be/mWCsVUOKuoI?si=7qVkoBfDxMCXt-ms">𝗝𝗶𝘀𝘀𝗵𝘂-𝗙𝗶𝗹𝘁𝗲𝗿-𝗕𝗼𝘁</a></blockquote>

developer : Mr.Jisshu
</b>""" 
    GROUP_C_TEXT = """<b><blockquote>
 --------------Set Verify-------------
/set_verify {website link} {website api}
/set_verify_2 {website link} {website api}
/set_verify_3 {website link} {website api}
-------------Set Verify Time-----------
/set_time_2 {seconds} Sᴇᴛ ᴛʜᴇ sᴇᴄᴏɴᴅ ᴠᴇʀɪғɪᴄᴀᴛɪᴏɴ ᴛɪᴍᴇ
/set_time_3 {seconds} Sᴇᴛ ᴛʜᴇ ᴛʜɪʀᴅ ᴠᴇʀɪғɪᴄᴀᴛɪᴏɴ ᴛɪᴍᴇ
--------------Verify On Off------------
/verifyoff {verify.off code} - off verification <a href="https://t.me/IM_JISSHU">Cᴏɴᴛᴀᴄᴛ</a> ᴛʜᴇ ʙᴏᴛ ᴀᴅᴍɪɴ ғᴏʀ ᴀ ᴠᴇʀɪғʏ.ᴏғғ ᴄᴏᴅᴇ
/verifyon - on verification 
------------Set File Caption-----------
/set_caption - set coustom file caption 
-----------Set Imdb Template-----------
/set_template - set IMDb template <a href="https://t.me/Jisshu_developer/8">Example</a>
--------------Set Tutorial-------------
/set_tutorial - set verification tutorial 
-------------Set Log Channel-----------
--> ᴀᴅᴅ ʟᴏɢ ᴄʜᴀɴɴᴇʟ ʙʏ ᴛʜɪs ꜰᴏʀᴍᴀᴛ & ᴍᴀᴋᴇ sᴜʀᴇ ʙᴏᴛ ɪs ᴀᴅᴍɪɴ ɪɴ ʏᴏᴜʀ ʟᴏɢ ᴄʜᴀɴɴᴇʟ 👇

/set_log {log channel id}
---------------------------------------
ʏᴏᴜ ᴄᴀɴ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴀʟʟ ᴅᴇᴛᴀɪʟs 
ʙʏ /details ᴄᴏᴍᴍᴀɴᴅ
</blockquote>
Iғ ʏᴏᴜ ʜᴀᴠᴇ ᴀɴʏ ᴅᴏᴜʙᴛs ᴘʟᴇᴀsᴇ <a href="https://t.me/IM_JISSHU">ᴄᴏɴᴛᴀᴄᴛ</a> ᴍʏ <a href="https://t.me/IM_JISSHU">ᴀᴅᴍɪɴ</a></b>"""


