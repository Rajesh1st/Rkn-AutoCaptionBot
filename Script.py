import os

class script(object):
    HELP_TXT = """ •••[( Get Help )]•••

    ⚠️ ALTER ⚠️
    • Add this bot to your channel with all admin permissions.
    • Use this command in your channel.
    • These commands work only in the channel.
    • Keep the file without the forward tag.

    •> /set - set a new caption in your channel
    •> /del - delete your caption
    •> /view - view your caption

    Format:
    {file_name} = original file name
    {file_caption} = original file caption 
    {file_size} = file original size       

    Eg:- <code>/set
    {file_name} or {file_caption}

    ⚙️ Size » {file_size}

    ╔═════ ᴊᴏɪɴ ᴡɪᴛʜ ᴜs ════╗
    💥 𝙅𝙊𝙄𝙉 :- channel link 
    💥 𝙅𝙊𝙄𝙉 :- channel link
    ╚═════ ᴊᴏɪɴ ᴡɪᴛʜ ᴜs ════╝
    </code>"""

    HTML_TAGS_TXT = """🔰 About Caption Font

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
<b>Available Caption Placeholders:</b>

➢ <code>{file_name}</code> - The name of the file (e.g., movie name, song title, etc.)

➢ <code>{file_size}</code> - The size of the file in human-readable format (e.g., 2.5 MB, 3 GB, etc.)

➢ <code>{file_caption}</code> - The caption of the file (may include word replacements and removals)

➢ <code>{language}</code> - The language(s) extracted from the file name or caption (e.g., English, Hindi, etc.)

➢ <code>{year}</code> - The year extracted from the file name or caption (e.g., 2021, 2019, etc.)

➢ <code>{subtitles}</code> - Display "ESub" or "MSub" based on the presence of subtitles in the file name or caption. If neither is found, it will show nothing.

➢ <code>{wish}</code> - A time-based greeting (e.g., Good Morning, Good Afternoon, Good Evening).

➢ <code>{duration}</code> - The total duration of the media in HH:MM:SS format (e.g., 01:50:34).

➢ <code>{prefix}</code> - The custom prefix set for the channel.

➢ <code>{suffix}</code> - The custom suffix set for the channel.

<b>Note:</b> Yᴏᴜ ᴄᴀɴ ᴄᴜsᴛᴏᴍɪᴢᴇ ʏᴏᴜʀ ᴄᴀᴘᴛɪᴏɴ ᴛᴇᴍᴘʟᴀᴛᴇ ʙʏ ᴜsɪɴɢ ᴛʜᴇsᴇ ᴘʟᴀᴄᴇʜᴏʟᴅᴇʀs ᴛᴏ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ғɪʟʟ ɪɴ ᴅᴇᴛᴀɪʟs ᴀʙᴏᴜᴛ ᴛʜᴇ ғɪʟᴇ.
For example: <code>{prefix} {file_name} {year} {language} {subtitles} {suffix}</code>
"""

# Static Text for Commands
command_list = """
<b>Available Bot Commands:</b>

<code>/set_prefix</code> - This command is used to set the prefix for the channel's caption.

<code>/clear_prefix</code> - Clears the set prefix.

<code>/set_suffix</code> - This command is used to set the suffix for the channel's caption.

<code>/clear_suffix</code> - Clears the set suffix.

<code>/rem_words</code> - Set a list of words to be removed from the caption.

<code>/rem_words_off</code> - Turns off the removable words feature for the channel.

<code>/replace_words</code> - Replace a word with another in the channel caption.

<code>/del_replace_word</code> - Disable the word replacement feature.

<code>/view</code> - View the current caption, prefix, suffix, removable words, replace words, and more.

<code>/tags</code> - View a list of HTML tags for text formatting (e.g., Bold, Italic, etc.).

<code>/Cmd</code> - Get a list of available bot commands with descriptions.

<code>/placeholders</code> - View a list of available placeholders and their usage in captions. 
"""
