class script(object):
    START_TXT = """𝙷𝙴𝙻𝙾 {},
𝙼𝚈 𝙽𝙰𝙼𝙴 𝙸𝚂 <a href=https://t.me/{}>{}</a>, 𝙸 𝙲𝙰𝙽 𝙿𝚁𝙾𝚅𝙸𝙳𝙴 𝙼𝙾𝚅𝙸𝙴𝚂, 𝙹𝚄𝚂𝚃 𝙰𝙳𝙳 𝙼𝙴 𝚃𝙾 𝚈𝙾𝚄𝚁 𝙶𝚁𝙾𝚄𝙿 𝙰𝙽𝙳 𝙴𝙽𝙹𝙾𝚈 😍"""
    HELP_TXT = """𝙷𝙴𝚈 {}
𝙷𝙴𝚁𝙴 𝙸𝚂 𝚃𝙷𝙴 𝙷𝙴𝙻𝙿 𝙵𝙾𝚁 𝙼𝚈 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂."""
    ABOUT_TXT = """✯ 𝙼𝚈 𝙽𝙰𝙼𝙴: {}
✯ 𝙲𝚁𝙴𝙰𝚃𝙾𝚁: <a href=https://t.me/REX_BOTZ>𝚃𝚎𝚊𝚖 𝚁𝚎𝚡 𝚋𝚘𝚝𝚜</a>
✯ 𝙻𝙸𝙱𝚁𝙰𝚁𝚈: 𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼
✯ 𝙻𝙰𝙽𝙶𝚄𝙰𝙶𝙴: 𝙿𝚈𝚃𝙷𝙾𝙽 𝟹
✯ 𝙳𝙰𝚃𝙰 𝙱𝙰𝚂𝙴: 𝙼𝙾𝙽𝙶𝙾 𝙳𝙱
✯ 𝙱𝙾𝚃 𝚂𝙴𝚁𝚅𝙴𝚁: 𝙷𝙴𝚁𝙾𝙺𝚄
✯ 𝙱𝚄𝙸𝙻𝙳 𝚂𝚃𝙰𝚃𝚄𝚂: v1.0.1 [ 𝙱𝙴𝚃𝙰 ]"""
    SOURCE_TXT = """<b>NOTE:</b>
- 𝙴𝙼𝙸𝙻𝙸𝙰 𝙲𝙻𝙰𝚁𝙺𝙴 𝙸𝚂 𝙽𝙾𝚃 𝙰𝙽 𝙾𝙿𝙴𝙽 𝚂𝙾𝚄𝚁𝙲𝙴 𝙿𝚁𝙾𝙹𝙴𝙲𝚃. 
- 𝙲𝙾𝙽𝚃𝙰𝙲𝚃 𝙾𝚄𝚁 𝙳𝙴𝚅𝚂 𝙾𝙽𝙻𝚈 𝙵𝙾𝚁 𝚁𝙴𝙿𝙾𝚁𝚃𝙸𝙽𝙶 𝙱𝚄𝙶𝚂.

<b>DEVS:</b>
- <a href=https://t.me/REX_BOTZ>𝚃𝚎𝚊𝚖 𝚁𝚎𝚡 𝚋𝚘𝚝𝚜</a>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and EvaMaria will respond whenever a keyword is found the message

<b>NOTE:</b>
1. 𝚎𝚟𝚊 𝚖𝚊𝚛𝚒𝚊 𝚜𝚑𝚘𝚞𝚕𝚍 𝚑𝚊𝚟𝚎 𝚊𝚍𝚖𝚒𝚗 𝚙𝚛𝚒𝚟𝚒𝚕𝚕𝚊𝚐𝚎..
2. 𝚘𝚗𝚕𝚢 𝚊𝚍𝚖𝚒𝚗𝚜 𝚌𝚊𝚗 𝚊𝚍𝚍 𝚏𝚒𝚕𝚝𝚎𝚛𝚜 𝚒𝚗 𝚊 𝚌𝚑𝚊𝚝.
3. 𝚊𝚕𝚎𝚛𝚝 𝚋𝚞𝚝𝚝𝚘𝚗𝚜 𝚑𝚊𝚟𝚎 𝚊 𝚕𝚒𝚖𝚒𝚝 𝚘𝚏 64 𝚌𝚑𝚊𝚛𝚊𝚌𝚝𝚎𝚛𝚜.

<b>Commands and Usage:</b>
• /filter - <code>𝙰𝙳𝙳 𝙰 𝙵𝙸𝙻𝚃𝙴𝚁 𝙸𝙽 𝙲𝙷𝙰𝚃</code>
• /filters - <code>𝙻𝙸𝚂𝚃 𝙰𝙻𝙻 𝚃𝙷𝙴 𝙵𝙸𝙻𝚃𝙴𝚁𝚂 𝙾𝙵 𝙰 𝙲𝙷𝙰𝚃</code>
• /del - <code>𝙳𝙴𝙻𝙴𝚃𝙴 𝙰 𝚂𝙿𝙴𝙲𝙸𝙵𝙸𝙲 𝙵𝙸𝙻𝚃𝙴𝚁 𝙸𝙽 𝙲𝙷𝙰𝚃</code>
• /delall - <code>𝙳𝙴𝙻𝙴𝚃𝙴 𝚃𝙷𝙴 𝚆𝙷𝙾𝙻𝙴 𝙵𝙸𝙻𝚃𝙴𝚁𝚂 𝙸𝙽 𝙰 𝙲𝙷𝙰𝚃 (𝙲𝙷𝙰𝚃 𝙾𝚆𝙽𝙴𝚁 𝙾𝙽𝙻𝚈)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- 𝙴𝙼𝙸𝙻𝙸𝙰 𝙲𝙻𝙰𝚁𝙺𝙴 𝚂𝚄𝙿𝙿𝙾𝚁𝚃𝚂 𝙱𝙾𝚃𝙷 𝚄𝚁𝙻 𝙰𝙽𝙳 𝙰𝙻𝙴𝚁𝚃 𝙸𝙽𝙻𝙸𝙽𝙴 𝙱𝚄𝚃𝚃𝙾𝙽𝚂

<b>NOTE:</b>
1. 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼 𝚆𝙸𝙻𝙻 𝙽𝙾𝚃 𝙰𝙻𝙻𝙾𝚆𝚂 𝚈𝙾𝚄 𝚃𝙾 𝚂𝙴𝙽𝙳 𝙱𝚄𝚃𝚃𝙾𝙽𝚂 𝚆𝙸𝚃𝙷𝙾𝚄𝚃 𝙰𝙽𝚈 𝙲𝙾𝙽𝚃𝙴𝙽𝚃, 𝚂𝙾 𝙲𝙾𝙽𝚃𝙴𝙽𝚃 𝙸𝚂 𝙼𝙰𝙽𝙳𝙰𝚃𝙾𝚁𝚈.
2. 𝙴𝙼𝙸𝙻𝙸𝙰 𝙲𝙻𝙰𝚁𝙺𝙴 𝚂𝚄𝙿𝙿𝙾𝚁𝚃𝚂 𝙱𝚄𝚃𝚃𝙾𝙽𝚂 𝚆𝙸𝚃𝙷 𝙰𝙽𝚈 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼 𝙼𝙴𝙳𝙸𝙰 𝚃𝚈𝙿𝙴.
3. 𝙱𝚄𝚃𝚃𝙾𝙽𝚂 𝚂𝙷𝙾𝚄𝙻𝙳 𝙱𝙴 𝙿𝚁𝙾𝙿𝙴𝚁𝙻𝚈 𝙿𝙰𝚁𝚂𝙴𝙳 𝙰𝚂 𝙼𝙰𝚁𝙺𝙳𝙾𝚆𝙽 𝙵𝙾𝚁𝙼𝙰𝚃.

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/EmiliaClarkeRexBot))</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    FUN_TXT = """Help: <b>𝖥𝗎𝗇 𝖬𝗈𝖽𝗎𝗅𝖾𝗌</b> 
    
<b>🎲 Nothing But Fun Stuffs</b>
1. /dice - 𝖱𝗈𝗅𝗅 𝗍𝗁𝖾 𝖽𝗂𝖼𝖾
2. /Throw - 𝖳𝗈 𝗍𝗁𝗋𝗈𝗐 𝖺 𝖽𝖺𝗋𝗍
4. /Goal - 𝖳𝗈 𝗀𝗈𝖺𝗅 

@Rex_Botz"""
    TELEGRAPH_TXT = """Help: <b>Telegraph Uploader</b>
    
<b>This Feature help to Upload Media Files To Telegraph Below 5MB</b>
1.Send any Media File Below 5MB.
2.Then Reply /telegraph or /tgraph or /tgmedia to the Media File.
3.That's it now you will get link.

<b>Note :</b>
This Feature May Be slow Due to Overload. So Please Wait Until you get your Link."""
    FILTER_TXT = """Help: <b>Choose Type of Filter that you need</b>"""
    FSTORE_TXT = """Help: <b>New File Store Feature</b>
    
<b>This Feature Helps you to Store your File</b>
1.Send Me any Media File.
2.The Reply /link To get sharable Link of That File Then Share the link.

<b>Note :</b>
This is Permanent File Store Feature."""
    QRCODE_TXT = """Help: 𝙽𝙴𝚆 𝚀𝚁𝙲𝙾𝙳𝙴 𝙶𝙴𝙽𝙴𝚁𝙰𝚃𝙾𝚁 𝙵𝙴𝙰𝚃𝚄𝚁𝙴

𝚃𝙷𝙸𝚂 𝙵𝙴𝙰𝚃𝚄𝚁𝙴 𝙷𝙴𝙻𝙿𝚂 𝚈𝙾𝚄 𝚃𝙾 𝙲𝙾𝙽𝚅𝙴𝚁𝚃 𝙰𝙽𝚈 𝚃𝙴𝚇𝚃 𝙾𝚁 𝙻𝙸𝙽𝙺 𝙸𝙽𝚃𝙾 𝚀𝚁𝙲𝙾𝙳𝙴.
1.𝙲𝚕𝚒𝚌𝚔 𝙾𝚗 /qrcode 

2.𝚂𝚎𝚗𝚍 𝚖𝚎 𝚊𝚗𝚢 𝚝𝚎𝚡𝚝 𝚘𝚛 𝚕𝚒𝚗𝚔 𝙸 𝚠𝚒𝚕𝚕 𝚌𝚘𝚗𝚟𝚎𝚛𝚝 𝚒𝚗𝚝𝚘 𝚀𝚁𝙲𝙾𝙳𝙴"""
    CARBON_TXT = """Help: 𝙲𝙰𝚁𝙱𝙾𝙽 𝙶𝙴𝙽𝙴𝚁𝙰𝚃𝙾𝚁
    
𝚃𝙷𝙸𝚂 𝙵𝙴𝙰𝚃𝚄𝚁𝙴 𝙷𝙴𝙻𝙿𝚂 𝚈𝙾𝚄 𝚃𝙾 𝙲𝙾𝙽𝚅𝙴𝚁𝚃 𝙰𝙽𝚈 𝙲𝙾𝙳𝙴𝚂 𝙾𝚁 𝚃𝙴𝚇𝚃 𝙸𝙽𝚃𝙾 𝙲𝙰𝚁𝙱𝙾𝙽 𝙸𝙼𝙰𝙶𝙴.
1.𝙲𝚕𝚒𝚌𝚔 𝚘𝚗 /carbon 

2.𝚂𝚎𝚗𝚍 𝚖𝚎 𝚊𝚗𝚢 𝚝𝚎𝚡𝚝 𝚘𝚛 𝚊𝚗𝚢 𝚌𝚘𝚍𝚒𝚗𝚐𝚜 𝚒 𝚠𝚒𝚕𝚕 𝚐𝚎𝚗𝚎𝚛𝚊𝚝𝚎 𝚒𝚝 𝚒𝚗𝚝𝚘 𝚌𝚊𝚛𝚋𝚘𝚗 𝚒𝚖𝚊𝚐𝚎"""
    PIN_TXT = """Help: 𝙿𝙸𝙽 𝙾𝚁 𝚄𝙽𝙿𝙸𝙽 𝙼𝙴𝚂𝚂𝙰𝙶𝙴
    
𝚃𝙷𝙸𝚂 𝙵𝙴𝙰𝚃𝚄𝚁𝙴 𝙷𝙴𝙻𝙿𝚂 𝚈𝙾𝚄 𝚃𝙾 𝙿𝙸𝙽 𝙾𝚁 𝚄𝙽𝙿𝙸𝙽 𝙰𝙽𝚈 𝙼𝙴𝚂𝚂𝙰𝙶𝙴 𝙸𝙽 𝙶𝚁𝙾𝚄𝙿.
1.𝚃𝚘 𝙿𝚒𝚗 𝚊 𝙼𝚎𝚜𝚜𝚊𝚐𝚎 𝚛𝚎𝚙𝚕𝚢 /pin 𝚝𝚘 𝚝𝚑𝚎 𝚖𝚎𝚜𝚜𝚊𝚐𝚎 𝚢𝚘𝚞 𝚗𝚎𝚎𝚍 𝚝𝚘 𝚙𝚒𝚗

2.𝚃𝚘 𝚄𝚗𝚙𝚒𝚗 𝚊 𝙼𝚎𝚜𝚜𝚊𝚐𝚎 𝚛𝚎𝚙𝚕𝚢 /unpin 𝚝𝚘 𝚝𝚑𝚎 𝚖𝚎𝚜𝚜𝚊𝚐𝚎 𝚢𝚘𝚞 𝚗𝚎𝚎𝚍 𝚝𝚘 𝚞𝚗𝚙𝚒𝚗"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. 𝙼𝚊𝚔𝚎 𝚖𝚎 𝚝𝚑𝚎 𝚊𝚍𝚖𝚒𝚗 𝚘𝚏 𝚢𝚘𝚞𝚛 𝚌𝚑𝚊𝚗𝚗𝚎𝚕 𝚒𝚏 𝚒𝚝'𝚜 𝚙𝚛𝚒𝚟𝚊𝚝𝚎.
2. 𝙼𝚊𝚔𝚎 𝚜𝚞𝚛𝚎 𝚝𝚑𝚊𝚝 𝚢𝚘𝚞𝚛 𝚌𝚑𝚊𝚗𝚗𝚎𝚕 𝚍𝚘𝚎𝚜 𝚗𝚘𝚝 𝚌𝚘𝚗𝚝𝚊𝚒𝚗𝚜 𝚌𝚊𝚖 𝚛𝚒𝚙, 𝚙𝚘𝚛𝚗 𝚊𝚗𝚍 𝚏𝚊𝚔𝚎 𝚏𝚒𝚕𝚎𝚜.
3. 𝙵𝚘𝚛𝚠𝚊𝚛𝚍 𝚝𝚑𝚎 𝚕𝚊𝚜𝚝 𝚖𝚎𝚜𝚜𝚊𝚐𝚎 𝚝𝚘 𝚖𝚎 𝚠𝚒𝚝𝚑 𝚚𝚞𝚘𝚝𝚎𝚜.
   𝙸'𝚕𝚕 𝚊𝚍𝚍 𝚊𝚕𝚕 𝚝𝚑𝚎 𝚏𝚒𝚕𝚎𝚜 𝚒𝚗 𝚝𝚑𝚊𝚝 𝚌𝚑𝚊𝚗𝚗𝚎𝚕 𝚝𝚘 𝚖𝚢 𝚍𝚋.."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. 𝙾𝙽𝙻𝚈 𝙰𝙳𝙼𝙸𝙽𝚂 𝙲𝙰𝙽 𝙰𝙳𝙳 𝙰 𝙲𝙾𝙽𝙽𝙴𝙲𝚃𝙸𝙾𝙽.
2. 𝚂𝙴𝙽𝙳 <code>/connect</code> 𝙵𝙾𝚁 𝙲𝙾𝙽𝙽𝙴𝙲𝚃𝙸𝙽𝙶 𝙼𝙴 𝚃𝙾 𝚄𝚁 𝙿𝙼

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
𝚃𝙷𝙴𝚂𝙴 𝙰𝚁𝙴 𝚃𝙷𝙴 𝙴𝚇𝚃𝚁𝙰 𝙵𝙴𝙰𝚃𝚄𝚁𝙴𝚂 𝙾𝙵 𝙴𝙼𝙸𝙻𝙸𝙰 𝙲𝙻𝙰𝚁𝙺𝙴

<b>Commands and Usage:</b>
• /id - <code>get id of a specifed user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """ 
█▀ ▀█▀ ▄▀█ ▀█▀ █▀
▄█ ░█░ █▀█ ░█░ ▄█
★ 𝚃𝙾𝚃𝙰𝙻 𝙵𝙸𝙻𝙴𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝚄𝚂𝙴𝚁𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝙲𝙷𝙰𝚃𝚂: <code>{}</code>
★ 𝚄𝚂𝙴𝙳 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱
★ 𝙵𝚁𝙴𝙴 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""

    COVID_TXT = """<b> Covid 19 Information </b>
To know the Covid info send <code> /covid india </code>"""
    
    JSON_TXT = """<b> Json imformation </b>
To know the json info of the message do reply and give command as /json
"""

    PURGE_TXT = """ <b> Purge module </b>
To delete a message. Reply /purge to a message where to start purging from 
 """
    GTRANS_TXT = """ <b> Google Translator </b>
To translate a text to your required language by replying /tr language 
 """
