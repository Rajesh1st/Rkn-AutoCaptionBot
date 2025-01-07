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
