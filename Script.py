import os

class script(object):
    HELP_TXT = """ •••[( 𝘎𝘦𝘵 𝘏𝘦𝘭𝘱 )]•••

    ❗ 𝗔𝗹𝗲𝗿𝘁 ❗
    • Aᴅᴅ ᴛʜɪs ʙᴏᴛ ɪɴ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ᴡɪᴛʜ ғᴜʟʟ ᴀᴅᴍɪɴ ʀɪɢʜᴛs.
    • Usᴇ ᴄᴏᴍᴍᴀɴᴅ ɢɪᴠᴇ ʙᴇʟᴏᴡ ɪɴ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ.
    • Tʜᴇsᴇ ᴄᴏᴍᴍᴀɴᴅ ᴏɴʟʏ ᴡᴏʀᴋ ɪɴ ᴄʜᴀɴɴᴇʟ.
    • Kᴇᴇᴘ ғɪʟᴇ ᴡɪᴛʜᴏᴜᴛ ғᴏʀᴡᴀʀᴅ ᴛᴀɢ.

     » cᴏᴍᴍᴀɴᴅ
     
    •> /set - Sᴇᴛ Nᴇᴡ Cᴀᴘᴛɪᴏɴ Iɴ ʏᴏᴜʀ Cʜᴀɴɴᴇʟ
    •> /del - Dᴇʟᴇᴛᴇ Yᴏᴜʀ Cᴀᴘᴛɪᴏɴ
    •> /view - Vɪᴇᴡ Yᴏᴜʀ Cᴀᴘᴛɪᴏɴ
    •> /cmd - ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ɪɴ ᴄʜᴀɴɴᴇʟ ᴛᴏ Gᴇᴛ ᴀ ʟɪsᴛ ᴏғ ᴀᴠᴀɪʟᴀʙʟᴇ ʙᴏᴛ ᴄᴏᴍᴍᴀɴᴅs
    •> /placeholder - ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ɪɴ ᴄʜᴀɴɴᴇʟ ᴛᴏ Vɪᴇᴡ ᴀ ʟɪsᴛ ᴏғ ᴀᴠᴀɪʟᴀʙʟᴇ ᴘʟᴀᴄᴇʜᴏʟᴅᴇʀs ᴀɴᴅ ᴛʜᴇɪʀ ᴜsᴀɢᴇ ɪɴ ᴄᴀᴘᴛɪᴏɴs

 » vᴀʀɪᴀʙʟᴇs

`{file_name}` = Oʀɪɢɪɴᴀʟ Fɪʟᴇ Nᴀᴍᴇ.
`{file_caption}` = Rᴇᴀʟ Cᴀᴘᴛɪᴏɴ Oғ Fɪʟᴇ.
`{file_size}` = Oʀɪɢɪɴᴀʟ Fɪʟᴇ Sɪᴢᴇ.
`{language}` = Lᴀɴɢᴜᴀɢᴇ Oғ Fɪʟᴇ Nᴀᴍᴇ.
`{subtitle}` = Sᴜʙᴛɪᴛʟᴇ ғʀᴏᴍ ғɪʟᴇ ɴᴀᴍᴇ.
`{duration}` = ᴅᴜʀᴀᴛɪᴏɴ ғʀᴏᴍ ᴠɪᴅᴇᴏ.
`{year}` = ʏᴇᴀʀ ғʀᴏᴍ ғɪʟᴇ ɴᴀᴍᴇ.
`{wish}` = ᴀᴅᴅ ᴡɪsʜ ᴛᴏ ᴠɪᴅᴇᴏ.

Eg:- <code>/set
{file_name}

⚙️ Size » {file_size}

╔═════ ᴊᴏɪɴ ᴡɪᴛʜ ᴜs ════╗
💥 𝙅𝙊𝙄𝙉 :- ᴄʜᴀɴɴᴇʟ ʟɪɴᴋ 
💥 𝙅𝙊𝙄𝙉 :- ᴄʜᴀɴɴᴇʟ ʟɪɴᴋ
╚═════ ᴊᴏɪɴ ᴡɪᴛʜ ᴜs ════╝
"""
    
    HTML_TAGS_TXT = """🔰 ᴀʙᴏᴜᴛ ᴄᴀᴘᴛɪᴏɴ ғᴏɴᴛ

    ➢ Bold Text
    ☞ <code>&lt;b&gt;{filename}&lt;/b&gt;</code>

    ➢ Spoiler Text
    ☞ <code>&lt;spoiler&gt;{filename}&lt;/spoiler&gt;</code>

    ➢ Block Quote Text
    ☞ <code>&lt;blockquote&gt;{filename}&lt;/blockquote&gt;</code>

    ➢ Italic Text
    ☞ <code>&lt;i&gt;{filename}&lt;/i&gt;</code>

    ➢ Underline Text
    ☞ <code>&lt;u&gt;{filename}&lt;/u&gt;</code>

    ➢ Strike Text
    ☞ <code>&lt;s&gt;{filename}&lt;/s&gt;</code>

    ➢ Mono Text
    ☞ <code>&lt;code&gt;{filename}&lt;/code&gt;</code>

    ➢ Pre Text
    ☞ <code>&lt;pre&gt;{filename}&lt;/pre&gt;</code>

    ➢ Hyperlink Text
    ☞ <code>&lt;a href="https://t.me/RxBotz"&gt;{filename}&lt;/a&gt;</code>"""

    # Updated ABOUT text
ABOUT_TXT = """<b>╔════❰ ᴀᴜᴛᴏ ᴄᴀᴘᴛɪᴏɴ ʙᴏᴛ ❱═❍⊱❁
║╭━━━━━━━━━━━━━━━➣
║┣⪼📃ʙᴏᴛ : <a href='https://t.me/RxAutoCaptionBot'>ᴀᴜᴛᴏ Cᴀᴘᴛɪᴏɴ ✨</a>
║┣⪼👦Cʀᴇᴀᴛᴏʀ : <a href='https://t.me/RxBotz'>ʀ'x ʙᴏᴛᴢ ⚠️</a>
║┣⪼🤖Uᴘᴅᴀᴛᴇ : <a href='https://t.me/RxBotz'>ʀ'x ʙᴏᴛᴢ™</a>
║┣⪼📡Hᴏsᴛᴇᴅ ᴏɴ : ʜᴇʀᴏᴋᴜ 
║┣⪼🗣️Lᴀɴɢᴜᴀɢᴇ : Pʏᴛʜᴏɴ3
║┣⪼📚Lɪʙʀᴀʀʏ : Pʏʀᴏɢʀᴀᴍ 2.11.6
║┣⪼🗒️Vᴇʀsɪᴏɴ : 2.0.8 [ᴍᴏsᴛ sᴛᴀʙʟᴇ]
║╰━━━━━━━━━━━━━━━➣
╚══════════════════❍⊱❁</b>"""

# Static Text for HTML Tags
html_tags_text = """🔰 Usᴇ ᴛʜɪs ʜᴛᴍʟ ᴛᴀɢs
➢ Bold Text
☞ <code>&lt;b&gt;{filename}&lt;/b&gt;</code>

➢ Spoiler Text
☞ <code>&lt;spoiler&gt;{filename}&lt;/spoiler&gt;</code>

➢ Block Quote Text
☞ <code>&lt;blockquote&gt;{filename}&lt;/blockquote&gt;</code>

➢ Italic Text
☞ <code>&lt;i&gt;{filename}&lt;/i&gt;</code>

➢ Underline Text
☞ <code>&lt;u&gt;{filename}&lt;/u&gt;</code>

➢ Strike Text
☞ <code>&lt;s&gt;{filename}&lt;/s&gt;</code>

➢ Mono Text
☞ <code>&lt;code&gt;{filename}&lt;/code&gt;</code>

➢ Pre Text
☞ <code>&lt;pre&gt;{filename}&lt;/pre&gt;</code>

➢ Hyperlink Text
☞ <code>&lt;a href="https://t.me/RxBotz"&gt;{filename}&lt;/a&gt;</code>"""

# Static Text for Placeholders
placeholders_text = """
<b>Aᴠᴀɪʟᴀʙʟᴇ Cᴀᴘᴛɪᴏɴ Pʟᴀᴄᴇʜᴏʟᴅᴇʀs:</b>

➢ <code>{file_name}</code> - Tʜᴇ ɴᴀᴍᴇ ᴏғ ᴛʜᴇ ғɪʟᴇ (ᴇ.ɢ., ᴍᴏᴠɪᴇ ɴᴀᴍᴇ, sᴏɴɢ ᴛɪᴛʟᴇ, ᴇᴛᴄ.)

➢ <code>{file_size}</code> - Tʜᴇ sɪᴢᴇ ᴏғ ᴛʜᴇ ғɪʟᴇ ɪɴ ʜᴜᴍᴀɴ-ʀᴇᴀᴅᴀʙʟᴇ ғᴏʀᴍᴀᴛ (ᴇ.ɢ., 2.5 MB, 3 GB, ᴇᴛᴄ.)

➢ <code>{file_caption}</code> - Tʜᴇ ᴄᴀᴘᴛɪᴏɴ ᴏғ ᴛʜᴇ ғɪʟᴇ (ᴍᴀʏ ɪɴᴄʟᴜᴅᴇ ᴡᴏʀᴅ ʀᴇᴘʟᴀᴄᴇᴍᴇɴᴛs ᴀɴᴅ ʀᴇᴍᴏᴠᴀʟs)

➢ <code>{language}</code> - Tʜᴇ ʟᴀɴɢᴜᴀɢᴇ(s) ᴇxᴛʀᴀᴄᴛᴇᴅ ғʀᴏᴍ ᴛʜᴇ ғɪʟᴇ ɴᴀᴍᴇ ᴏʀ ᴄᴀᴘᴛɪᴏɴ (ᴇ.ɢ., Eɴɢʟɪsʜ, Hɪɴᴅɪ, ᴇᴛᴄ.)

➢ <code>{year}</code> - Tʜᴇ ʏᴇᴀʀ ᴇxᴛʀᴀᴄᴛᴇᴅ ғʀᴏᴍ ᴛʜᴇ ғɪʟᴇ ɴᴀᴍᴇ ᴏʀ ᴄᴀᴘᴛɪᴏɴ (ᴇ.ɢ., 2021, 2019, ᴇᴛᴄ.)

➢ <code>{subtitles}</code> - Dɪsᴘʟᴀʏ "ESᴜʙ" ᴏʀ "MSᴜʙ" ʙᴀsᴇᴅ ᴏɴ ᴛʜᴇ ᴘʀᴇsᴇɴᴄᴇ ᴏғ sᴜʙᴛɪᴛʟᴇs ɪɴ ᴛʜᴇ ғɪʟᴇ ɴᴀᴍᴇ ᴏʀ ᴄᴀᴘᴛɪᴏɴ. Iғ ɴᴇɪᴛʜᴇʀ ɪs ғᴏᴜɴᴅ, ɪᴛ ᴡɪʟʟ sʜᴏᴡ ɴᴏᴛʜɪɴɢ.

➢ <code>{wish}</code> - A ᴛɪᴍᴇ-ʙᴀsᴇᴅ ɢʀᴇᴇᴛɪɴɢ (ᴇ.ɢ., Gᴏᴏᴅ Mᴏʀɴɪɴɢ, Gᴏᴏᴅ Aғᴛᴇʀɴᴏᴏɴ, Gᴏᴏᴅ Eᴠᴇɴɪɴɢ).

➢ <code>{duration}</code> - Tʜᴇ ᴛᴏᴛᴀʟ ᴅᴜʀᴀᴛɪᴏɴ ᴏғ ᴛʜᴇ ᴍᴇᴅɪᴀ ɪɴ HH:MM:SS ғᴏʀᴍᴀᴛ (ᴇ.ɢ., 01:50:34).

➢ <code>{prefix}</code> - Tʜᴇ ᴄᴜsᴛᴏᴍ ᴘʀᴇғɪx sᴇᴛ ғᴏʀ ᴛʜᴇ ᴄʜᴀɴɴᴇʟ.

➢ <code>{suffix}</code> - Tʜᴇ ᴄᴜsᴛᴏᴍ sᴜғғɪx sᴇᴛ ғᴏʀ ᴛʜᴇ ᴄʜᴀɴɴᴇʟ.

<b>Note:</b> Yᴏᴜ ᴄᴀɴ ᴄᴜsᴛᴏᴍɪᴢᴇ ʏᴏᴜʀ ᴄᴀᴘᴛɪᴏɴ ᴛᴇᴍᴘʟᴀᴛᴇ ʙʏ ᴜsɪɴɢ ᴛʜᴇsᴇ ᴘʟᴀᴄᴇʜᴏʟᴅᴇʀs ᴛᴏ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ғɪʟʟ ɪɴ ᴅᴇᴛᴀɪʟs ᴀʙᴏᴜᴛ ᴛʜᴇ ғɪʟᴇ.
For example: <code>{prefix} {file_name} {year} {language} {subtitles} {suffix}</code>
"""

# Static Text for Commands
command_list = """
<b>ᴀᴠᴀɪʟᴀʙʟᴇ ʙᴏᴛ ᴄᴏᴍᴍᴀɴᴅ:</b>

<code>/set_prefix</code> - ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ɪs ᴜsᴇᴅ ᴛᴏ sᴇᴛ ᴛʜᴇ ᴘʀᴇғɪx ғᴏʀ ᴛʜᴇ ᴄʜᴀɴɴᴇʟ's ᴄᴀᴘᴛɪᴏɴ.

<code>/clear_prefix</code> - ᴄʟᴇᴀʀs ᴛʜᴇ sᴇᴛ ᴘʀᴇғɪx.

<code>/set_suffix</code> - ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ɪs ᴜsᴇᴅ ᴛᴏ sᴇᴛ ᴛʜᴇ sᴜғғɪx ғᴏʀ ᴛʜᴇ ᴄʜᴀɴɴᴇʟ's ᴄᴀᴘᴛɪᴏɴ.

<code>/clear_suffix</code> - ᴄʟᴇᴀʀs ᴛʜᴇ sᴇᴛ sᴜғғɪx.

<code>/rem_words</code> - sᴇᴛ ᴀ ʟɪsᴛ ᴏғ ᴡᴏʀᴅs ᴛᴏ ʙᴇ ʀᴇᴍᴏᴠᴇᴅ ғʀᴏᴍ ᴛʜᴇ ᴄᴀᴘᴛɪᴏɴ.

<code>/rem_words_off</code> - ᴛᴜʀɴs ᴏғғ ᴛʜᴇ ʀᴇᴍᴏᴠᴀʙʟᴇ ᴡᴏʀᴅs ғᴇᴀᴛᴜʀᴇ ғᴏʀ ᴛʜᴇ ᴄʜᴀɴɴᴇʟ.

<code>/replace_words</code> - ʀᴇᴘʟᴀᴄᴇ ᴀ ᴡᴏʀᴅ ᴡɪᴛʜ ᴀɴᴏᴛʜᴇʀ ɪɴ ᴛʜᴇ ᴄʜᴀɴɴᴇʟ ᴄᴀᴘᴛɪᴏɴ.

<code>/del_replace_word</code> - ᴅɪsᴀʙʟᴇ ᴛʜᴇ ᴡᴏʀᴅ ʀᴇᴘʟᴀᴄᴇᴍᴇɴᴛ ғᴇᴀᴛᴜʀᴇ.

<code>/view</code> - ᴠɪᴇᴡ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴄᴀᴘᴛɪᴏɴ, ᴘʀᴇғɪx, sᴜғғɪx, ʀᴇᴍᴏᴠᴀʙʟᴇ ᴡᴏʀᴅs, ʀᴇᴘʟᴀᴄᴇ ᴡᴏʀᴅs, ᴀɴᴅ ᴍᴏʀᴇ.

<code>/tags</code> - ᴠɪᴇᴡ ᴀ ʟɪsᴛ ᴏғ ʜᴛᴍʟ ᴛᴀɢs ғᴏʀ ᴛᴇxᴛ ғᴏʀᴍᴀᴛᴛɪɴɢ (ᴇ.ɢ., ʙᴏʟᴅ, ɪᴛᴀʟɪᴄ, ᴇᴛᴄ.).

<code>/Cmd</code> - ɢᴇᴛ ᴀ ʟɪsᴛ ᴏғ ᴀᴠᴀɪʟᴀʙʟᴇ ʙᴏᴛ ᴄᴏᴍᴍᴀɴᴅs ᴡɪᴛʜ ᴅᴇsᴄʀɪᴘᴛɪᴏɴs.

<code>/placeholders</code> - ᴠɪᴇᴡ ᴀ ʟɪsᴛ ᴏғ ᴀᴠᴀɪʟᴀʙʟᴇ ᴘʟᴀᴄᴇʜᴏʟᴅᴇʀs ᴀɴᴅ ᴛʜᴇɪʀ ᴜsᴀɢᴇ ɪɴ ᴄᴀᴘᴛɪᴏɴs.
"""
