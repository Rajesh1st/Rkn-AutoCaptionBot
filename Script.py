import os

class script(object):
      HELP_CAPTION_TEXT = """<b>ʏᴏᴜ ᴄᴀɴ ᴀᴅᴅ ᴄᴜsᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ ᴛᴏ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ʙʏ ᴛʜᴇ ғᴏʟʟᴏᴡɪɴɢ :-

» cᴏᴍᴍᴀɴᴅ

•> /set {file_name}
•> /del & /del_caption

<blockquote expendable>
» vᴀʀɪᴀʙʟᴇs 

• {file_name} = ғɪʟᴇ ɴᴀᴍᴇ.
• {file_size} = ᴏʀɪɢɪɴᴀʟ ғɪʟᴇ sɪᴢᴇ.
• {file_caption} = ᴅᴇғᴀᴜʟᴛ ғɪʟᴇ ɴᴀᴍᴇ.
• {language} = ʟᴀɴɢᴜᴀɢᴇs ғʀᴏᴍ ғɪʟᴇ ɴᴀᴍᴇ.
• {year} = ʏᴇᴀʀ ғʀᴏᴍ ғɪʟᴇ ɴᴀᴍᴇ.
• {quality} = ǫᴜᴀʟɪᴛʏ ғʀᴏᴍ ғɪʟᴇ ɴᴀᴍᴇ.
• {duration} = ᴅᴜʀᴀᴛɪᴏɴ ғʀᴏᴍ ᴠɪᴅᴇᴏ.
•{subtitles} = Dɪsᴘʟᴀʏ "ESᴜʙ" ᴏʀ "MSᴜʙ"
• {wish} = ᴀᴅᴅ ᴡɪsʜ ᴛᴏ ᴠɪᴅᴇᴏ.
 </blockquote>

ғᴏʀ ғᴜʀᴛʜᴇʀ sᴜᴘᴘᴏʀᴛ ᴀsᴋ ɪɴ ᴏᴜʀ sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ.</b>
"""   
    
  HELP_TXT = """<blockquote>❗ ᴀʟᴇʀᴛ ❗</blockquote>
• **ᴀᴅᴅ ᴛʜɪs ʙᴏᴛ ɪɴ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ᴡɪᴛʜ ғᴜʟʟ ᴀᴅᴍɪɴ ʀɪɢʜᴛs.**
• **ᴜsᴇ ᴄᴏᴍᴍᴀɴᴅ ɢɪᴠᴇ ʙᴇʟᴏᴡ ɪɴ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ.**
• **ᴛʜᴇsᴇ ᴄᴏᴍᴍᴀɴᴅs ᴏɴʟʏ ᴡᴏʀᴋ ɪɴ ᴄʜᴀɴɴᴇʟ.**
• **ᴋᴇᴇᴘ ғɪʟᴇ ᴡɪᴛʜᴏᴜᴛ ғᴏʀᴡᴀʀᴅ ᴛᴀɢ.**
<blockquote expandable> 
» **cᴏᴍᴍᴀɴᴅ**
•> **/set - Sᴇᴛ Nᴇᴡ Cᴀᴘᴛɪᴏɴ Iɴ ʏᴏᴜʀ Cʜᴀɴɴᴇʟ**
•> **/del - Dᴇʟᴇᴛᴇ Yᴏᴜʀ Cᴀᴘᴛɪᴏɴ**
•> **/view - Vɪᴇᴡ Yᴏᴜʀ Cᴀᴘᴛɪᴏɴ**
•> **/cmd - ᴛᴏ Gᴇᴛ ᴀ ʟɪsᴛ ᴏғ ᴀᴠᴀɪʟᴀʙʟᴇ ʙᴏᴛ ᴄᴏᴍᴍᴀɴᴅs**
•> **/placeholder - ᴛᴏ Vɪᴇᴡ ᴀ ʟɪsᴛ ᴏғ ᴀᴠᴀɪʟᴀʙʟᴇ ᴘʟᴀᴄᴇʜᴏʟᴅᴇʀs ᴀɴᴅ ᴛʜᴇɪʀ ᴜsᴀɢᴇ ɪɴ ᴄᴀᴘᴛɪᴏɴs**
•> **/add_button - ᴀᴅᴅ ʙᴜᴛᴛᴏɴs ᴛᴏ ᴍᴇssᴀɢᴇ.**
•> **/del_button - ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴀʟʟ ᴛʜᴇ ʙᴜᴛᴛᴏɴs.**
•> **/replace_word - ʀᴇᴘʟᴀᴄᴇ ᴍᴜʟᴛɪᴘʟᴇ ᴡᴏʀᴅs ᴡɪᴛʜ ʏᴏᴜʀ ᴏᴡɴ ᴡᴏʀᴅs.**
•> **/del_replace_word - ᴅᴇʟᴇᴛᴇ ᴀʟʟ ᴛʜᴇ ʀᴇᴘʟᴀᴄᴇ ᴡᴏʀᴅs.**
•> **/rem_words - ʀᴇᴍᴏᴠᴇ ᴍᴜʟᴛɪᴘʟᴇ ᴡᴏʀᴅs ғʀᴏᴍ ғɪʟᴇ ɴᴀᴍᴇ.**
•> **/del_rem_word - ʀᴇᴍᴏᴠᴇ ᴀʟʟ ᴛʜᴇ ᴅᴇʟᴇᴛᴇ ᴡᴏʀᴅs.**
•> **/rem_mention - ʀᴇᴍᴏᴠᴇ ᴀʟʟ ᴛʜᴇ ᴜɴᴡᴀɴᴛᴇᴅ ᴜsᴇʀɴᴀᴍᴇ.**
•> **/rem_url - ʀᴇᴍᴏᴠᴇ ᴀʟʟ ᴛʜᴇ ᴜɴᴡᴀɴᴛᴇᴅ ᴜʀʟs.**
•> **/set_preflix - sᴇᴛ ʏᴏᴜʀ ᴘʀᴇғʟɪx.**
•> **/set_suffix - sᴇᴛ ʏᴏᴜʀ sᴜғғɪx.**
•> **/del_preflix - ᴅᴇʟᴇᴛᴇ ʏᴏᴜʀ ᴘʀᴇғʟɪx.**
•> **/del_suffix - ᴅᴇʟᴇᴛᴇ ʏᴏᴜʀ sᴜғғɪx.**
</blockquote>"""

# Static Text for HTML Tags
    HTML_TAGS_TEXT = """🔰 Usᴇ ᴛʜɪs ʜᴛᴍʟ ᴛᴀɢs
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
    PLACEHOLDERS_TEXT = """
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
    COMMAND_LIST = """
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
