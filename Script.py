import os

class script(object):
    HELP_CAPTION_TEXT = """<b>You can add custom caption to your channel by the following :-

» command

•> /set {file_name}
•> /del & /del_caption

<blockquote expendable>
» variables 

• {file_name} = file name.
• {file_size} = original file size.
• {file_caption} = default file name.
• {language} = languages from file name.
• {year} = year from file name.
• {quality} = quality from file name.
• {duration} = duration from video.
• {subtitles} = Display "ESub" or "MSub"
• {wish} = add wish to video.
 </blockquote>

for further support ask in our support group.</b>
"""   
    
    HELP_TXT = """<blockquote>❗ alert ❗</blockquote>
• **add this bot in your channel with full admin rights.**
• **use command give below in your channel.**
• **these commands only work in channel.**
• **keep file without forward tag.**
<blockquote expandable> 
» **command**
•> **/set - Set New Caption In your Channel**
•> **/del - Delete Your Caption**
•> **/view - View Your Caption**
•> **/cmd - to Get a list of available bot commands**
•> **/placeholder - to View a list of available placeholders and their usage in captions**
•> **/add_button - add buttons to message.**
•> **/del_button - to delete all the buttons.**
•> **/replace_word - replace multiple words with your own words.**
•> **/del_replace_word - delete all the replace words.**
•> **/rem_words - remove multiple words from file name.**
•> **/del_rem_word - remove all the delete words.**
•> **/rem_mention - remove all the unwanted username.**
•> **/rem_url - remove all the unwanted urls.**
•> **/set_preflix - set your prefix.**
•> **/set_suffix - set your suffix.**
•> **/del_preflix - delete your prefix.**
•> **/del_suffix - delete your suffix.**
</blockquote>"""

    # Static Text for HTML Tags
    HTML_TAGS_TEXT = """🔰 Use this html tags
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

<b>Note:</b> You can customize your caption template by using these placeholders to automatically fill in details about the file.
For example: <code>{prefix} {file_name} {year} {language} {subtitles} {suffix}</code>
"""

    # Static Text for Commands
    COMMAND_LIST = """
<b>Available bot commands:</b>

<code>/set_prefix</code> - This command is used to set the prefix for the channel's caption.

<code>/clear_prefix</code> - Clears the set prefix.

<code>/set_suffix</code> - This command is used to set the suffix for the channel's caption.

<code>/clear_suffix</code> - Clears the set suffix.

<code>/rem_words</code> - Set a list of words to be removed from the caption.

<code>/rem_words_off</code> - Turns off the removable words feature for the channel.

<code>/replace_words</code> - Replace a word with another in the channel's caption.

<code>/del_replace_word</code> - Disable the word replacement feature.

<code>/view</code> - View the current caption, prefix, suffix, removable words, replace words, and more.

<code>/tags</code> - View a list of available HTML tags to format your caption.
"""
      
