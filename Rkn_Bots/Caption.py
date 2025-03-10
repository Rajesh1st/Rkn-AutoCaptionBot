
# (c) @RknDeveloperr
# Rkn Developer 
# Don't Remove Credit 😔
# Telegram Channel @RknDeveloper & @Rkn_Botz
# Developer @RknDeveloperr

from pyrogram import Client, filters, errors, types
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import FloodWait
from config import Rkn_Bots
from Script import script
from datetime import datetime
import asyncio
import os
import re
import sys
import time
import motor.motor_asyncio
from .database import total_user, total_channels, getid, delete, addCap, updateCap, insert, chnl_ids, ban_user, unban_user, is_banned

@Client.on_message(filters.private & filters.user(Rkn_Bots.ADMIN) & filters.command(["rknusers"]))
async def all_db_users_here(client, message):
    start_t = time.time()
    rkn = await message.reply_text("Processing...")
    uptime = time.strftime("%Hh%Mm%Ss", time.gmtime(time.time() - client.uptime))    
    total_users = await total_user()
    total_chnls = await total_channels()  # Get the total number of channels
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rkn.edit(text=f"**--Bot Processed--** \n\n**> 𝙼𝚢 𝚂𝚝𝚊𝚝𝚜**\n\n"
                        "```text\n"
                        f"‣ Bot ᴜᴘᴛɪᴍᴇ: {uptime}\n"
                        f"‣ Bot ᴘɪɴɢ: {time_taken_s:.3f} ᴍꜱ\n"
                        f"‣ ᴛᴏᴛᴀʟ ᴜꜱᴇʀꜱ: {total_users}\n"
                        f"‣ ᴛᴏᴛᴀʟ ᴄʜᴀɴɴᴇʟꜱ: {total_chnls}\n"
                        "```")
                        
@Client.on_message(filters.private & filters.user(Rkn_Bots.ADMIN) & filters.command(["broadcast"]))
async def broadcast(bot, message):
    if (message.reply_to_message):
        rkn = await message.reply_text("Bot Processing.\nI am checking all bot users.")
        all_users = await getid()
        tot = await total_user()
        success = 0
        failed = 0
        deactivated = 0
        blocked = 0
        await rkn.edit(f"bot ʙʀᴏᴀᴅᴄᴀsᴛɪɴɢ started...")
        async for user in all_users:
            try:
                time.sleep(1)
                await message.reply_to_message.copy(user['_id'])
                success += 1
            except errors.InputUserDeactivated:
                deactivated +=1
                await delete({"_id": user['_id']})
            except errors.UserIsBlocked:
                blocked +=1
                await delete({"_id": user['_id']})
            except Exception as e:
                failed += 1
                await delete({"_id": user['_id']})
                pass
            try:
                await rkn.edit(f"<u>ʙʀᴏᴀᴅᴄᴀsᴛ ᴘʀᴏᴄᴇssɪɴɢ</u>\n\n• ᴛᴏᴛᴀʟ ᴜsᴇʀs: {tot}\n• sᴜᴄᴄᴇssғᴜʟ: {success}\n• ʙʟᴏᴄᴋᴇᴅ ᴜsᴇʀs: {blocked}\n• ᴅᴇʟᴇᴛᴇᴅ ᴀᴄᴄᴏᴜɴᴛs: {deactivated}\n• ᴜɴsᴜᴄᴄᴇssғᴜʟ: {failed}")
            except FloodWait as e:
                await asyncio.sleep(t.x)
        await rkn.edit(f"<u>ʙʀᴏᴀᴅᴄᴀsᴛ ᴄᴏᴍᴘʟᴇᴛᴇᴅ</u>\n\n• ᴛᴏᴛᴀʟ ᴜsᴇʀs: {tot}\n• sᴜᴄᴄᴇssғᴜʟ: {success}\n• ʙʟᴏᴄᴋᴇᴅ ᴜsᴇʀs: {blocked}\n• ᴅᴇʟᴇᴛᴇᴅ ᴀᴄᴄᴏᴜɴᴛs: {deactivated}\n• ᴜɴsᴜᴄᴄᴇssғᴜʟ: {failed}")
        
# Restart to cancell all process 
@Client.on_message(filters.private & filters.user(Rkn_Bots.ADMIN) & filters.command("restart"))
async def restart_bot(b, m):
    rkn_msg = await b.send_message(text="**🔄 𝙿𝚁𝙾𝙲𝙴𝚂𝚂𝙴𝚂 𝚂𝚃𝙾𝙿𝙴𝙳. 𝙱𝙾𝚃 𝙸𝚂 𝚁𝙴𝚂𝚃𝙰𝚁𝚃𝙸𝙽𝙶...**", chat_id=m.chat.id)       
    await asyncio.sleep(3)
    await rkn_msg.edit("**✅️ 𝙱𝙾𝚃 𝙸𝚂 𝚁𝙴𝚂𝚃𝙰𝚁𝚃𝙴𝙳. 𝙽𝙾𝚆 𝚈𝙾𝚄 𝙲𝙰𝙽 𝚄𝚂𝙴 𝙼𝙴**")
    os.execl(sys.executable, sys.executable, *sys.argv)
    
# Ban a user
@Client.on_message(filters.private & filters.user(Rkn_Bots.ADMIN) & filters.command("ban"))
async def ban(client, message):
    if len(message.command) < 2:
        await message.reply_text("Usage: /ban <user_id>")
        return
    try:
        user_id = int(message.command[1])
        await ban_user(user_id)
        await message.reply_text(f"User {user_id} has been banned.")
    except ValueError:
        await message.reply_text("Invalid User ID.")

# Unban a user
@Client.on_message(filters.private & filters.user(Rkn_Bots.ADMIN) & filters.command("unban"))
async def unban(client, message):
    if len(message.command) < 2:
        await message.reply_text("Usage: /unban <user_id>")
        return
    try:
        user_id = int(message.command[1])
        await unban_user(user_id)
        await message.reply_text(f"User {user_id} has been unbanned.")
    except ValueError:
        await message.reply_text("Invalid User ID.")

@Client.on_message(filters.private | filters.channel)
async def block_banned_users(client, message):
    user_id = message.from_user.id
    if await is_banned(user_id):
        await message.reply_text("You are banned from using this bot.")
        return
    
@Client.on_message(filters.command("start") & filters.private)
async def start_cmd(bot, message):
    user_id = int(message.from_user.id)
    await insert(user_id)

    # Assuming Rkn_Bots.RKN_PIC is a valid photo URL or file ID
    await message.reply_photo(
        photo=Rkn_Bots.RKN_PIC,
        caption=f"ʜᴇʏ, {message.from_user.mention}\n\nI ᴀᴍ ᴀ ᴀᴅᴠᴀɴᴄᴇᴅ ᴀᴜᴛᴏᴄᴀᴘᴛɪᴏɴʙᴏᴛ. ᴠᴇʀʏ sɪᴍᴘʟᴇ ᴛᴏ ᴜsᴇ ᴍᴇ. ᴊᴜsᴛ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ᴍᴀᴋᴇ ᴍᴇ ᴀɴ ᴀᴅᴍɪɴ ᴏᴠᴇʀ ᴛʜᴇʀᴇ. ᴛʜᴇɴ sᴇᴛ Yᴏᴜʀ Cᴀᴘᴛɪᴏɴ Bʏ Usɪɴɢ <mono>/set</mono> & <mono>/setCaption</mono> Cᴏᴍᴍᴀɴᴅ ғᴏʀ ᴇɴᴀʙʟɪɴɢ ᴀᴜᴛᴏᴄᴀᴘᴛɪᴏɴ.\n\n"
                f"<blockquote>ɴᴏᴛᴇ: Mᴀᴋᴇ sᴜʀᴇ I ᴀᴍ ᴀɴ ᴀᴅᴍɪɴ ɪɴ ʏᴏᴜʀ ᴄʜᴀᴛ ᴡɪᴛʜ ᴀᴅᴍɪɴ ʀɪɡʜᴛs.</blockquote>",
    reply_markup=InlineKeyboardMarkup([[
        InlineKeyboardButton('➕️ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ➕️', url=f"https://t.me/{bot.me.username}?startchannel&admin=change_info+post_messages+edit_messages+delete_messages+restrict_members+invite_users+pin_messages+manage_topics+manage_video_chats+anonymous+manage_chat+post_stories+edit_stories+delete_stories")
    ], [
        InlineKeyboardButton('Hᴇʟᴘ', callback_data='help_button'),
        InlineKeyboardButton('Aʙᴏᴜᴛ', callback_data='about_button')
    ], [
        InlineKeyboardButton("🌐 Uᴘᴅᴀᴛᴇ", url=f"https://t.me/RxBotz"),
        InlineKeyboardButton("📜 Sᴜᴘᴘᴏʀᴛ", url=r"https://t.me/+zb9_Za9m2kI4NzM1")
    ]])
 
    )

@Client.on_callback_query(filters.regex('help_button'))
async def help_callback(bot, callback_query):
    await callback_query.message.edit_text(
        script.HELP_TXT,
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup([
            [
                InlineKeyboardButton('• ᴄᴀᴘᴛɪᴏɴ', callback_data='caption_button'),
                InlineKeyboardButton('• ʙᴜᴛᴛᴏɴ', callback_data='button_button')
            ],
            [
                InlineKeyboardButton('• ᴡᴏʀᴅ ᴛᴏ ʀᴇᴍᴏᴠᴇ', callback_data='remove_word_button')
            ],
            [
                InlineKeyboardButton('• ᴜsᴇʀɴᴀᴍᴇ', callback_data='username_button'),
                InlineKeyboardButton('• ᴜʀʟ', callback_data='url_button')
            ],
            [
                InlineKeyboardButton('• ᴡᴏʀᴅ ᴛᴏ ʀᴇᴘʟᴀᴄᴇ', callback_data='replace_word_button')
            ],
            [
                InlineKeyboardButton('• ʀᴇsᴇᴛ', callback_data='reset_button'),
                InlineKeyboardButton('• ᴅᴇᴛᴀɪʟ', callback_data='detail_button')
            ],
            [
                InlineKeyboardButton('• ʜᴛᴍʟ ᴛᴀɢ ᴏʀ ғᴏɴᴛs', callback_data='html_tag_or_fonts_button')
            ],
            [
                InlineKeyboardButton('• Pʀᴇғɪx', callback_data='prefix_button'),
                InlineKeyboardButton('• sᴜғғɪx', callback_data='suffix_button')
            ],
            [
                InlineKeyboardButton('🔙 Back', callback_data='start')
            ]
        ])
    )


@Client.on_callback_query(filters.regex('caption_button'))
async def caption_callback(bot, callback_query):
    await callback_query.message.edit_text(
        script.HELP_CAPTION_TEXT,
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup([
            [
                InlineKeyboardButton('🔙 Back to Help', callback_data='help_button')
            ]
        ])
    )


@Client.on_callback_query(filters.regex('remove_word_button'))
async def remove_word_callback(bot, callback_query):
    await callback_query.message.edit_text(
        script.REMOVE_WORD_BUTTON_TEXT,
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup([
            [
                InlineKeyboardButton('🔙 Back to Help', callback_data='help_button')
            ]
        ])
    )


@Client.on_callback_query(filters.regex('replace_word_button'))
async def replace_word_callback(bot, callback_query):
    await callback_query.message.edit_text(
        script.REPLACE_WORD_BUTTON_TEXT,
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup([
            [
                InlineKeyboardButton('🔙 Back to Help', callback_data='help_button')
            ]
        ])
    )


@Client.on_callback_query(filters.regex('html_tag_or_fonts_button'))
async def html_tag_or_fonts_callback(bot, callback_query):
    await callback_query.message.edit_text(
        script.HTML_TAG_OR_FONTS_BUTTON_TEXT,
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup([
            [
                InlineKeyboardButton('🔙 Back to Help', callback_data='help_button')
            ]
        ])
        )


@Client.on_callback_query(filters.regex('reset_button'))
async def reset_button_callback(bot, callback_query):
    await callback_query.message.edit_text(
        script.RESET_BUTTON_TEXT,
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup([
            [
                InlineKeyboardButton('🔙 Back to Help', callback_data='help_button')
            ]
        ])
    )


@Client.on_callback_query(filters.regex('detail_button'))
async def detail_button_callback(bot, callback_query):
    await callback_query.message.edit_text(
        script.DETAIL_BUTTON_TEXT,
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup([
            [
                InlineKeyboardButton('🔙 Back to Help', callback_data='help_button')
            ]
        ])
    )


@Client.on_callback_query(filters.regex('suffix_button'))
async def suffix_button_callback(bot, callback_query):
    await callback_query.message.edit_text(
        script.SUFFIX_BUTTON_TEXT,
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup([
            [
                InlineKeyboardButton('🔙 Back to Help', callback_data='help_button')
            ]
        ])
    )


@Client.on_callback_query(filters.regex('prefix_button'))
async def prefix_button_callback(bot, callback_query):
    await callback_query.message.edit_text(
        script.PREFIX_BUTTON_TEXT,
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup([
            [
                InlineKeyboardButton('🔙 Back to Help', callback_data='help_button')
            ]
        ])
    )
    
# Handle the "ABOUT" button callback
@Client.on_callback_query(filters.regex('about_button'))
async def about_callback(bot, callback_query):
    await callback_query.message.edit_text(
        script.ABOUT_TXT,  # Use the updated ABOUT text from script.py
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton('↩ ʙᴀᴄᴋ', callback_data='start'),
            InlineKeyboardButton('❌ Close', callback_data='close_about')
        ]])
    )

# Handle "CLOSE" action for ABOUT button
@Client.on_callback_query(filters.regex('close_about'))
async def close_about_callback(bot, callback_query):
    await callback_query.message.delete()

# Handle "BACK" to the main START message
@Client.on_callback_query(filters.regex('start'))
async def back_to_start_callback(bot, callback_query):
    bot_username = (await bot.get_me()).username  # Get the bot's username
    await callback_query.message.edit_text(
        f"ʜᴇʏ, {callback_query.from_user.mention}\n\nI ᴀᴍ ᴀɴ ᴀᴅᴠᴀɴᴄᴇᴅ ᴀᴜᴛᴏᴄᴀᴘᴛɪᴏɴʙᴏᴛ. ᴠᴇʀʏ sɪᴍᴘʟᴇ ᴛᴏ ᴜsᴇ ᴍᴇ. ᴊᴜsᴛ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ᴍᴀᴋᴇ ᴍᴇ ᴀɴ ᴀᴅᴍɪɴ ᴏᴠᴇʀ ᴛʜᴇʀᴇ. ᴛʜᴇɴ sᴇᴛ Yᴏᴜʀ Cᴀᴘᴛɪᴏɴ Bʏ Usɪɴɢ <mono>/set</mono> & <mono>/setCaption</mono> Cᴏᴍᴍᴀɴᴅ ғᴏʀ ᴇɴᴀʙʟɪɴɢ ᴀᴜᴛᴏᴄᴀᴘᴛɪᴏɴ.\n\n"
        f"<blockquote>ɴᴏᴛᴇ: Mᴀᴋᴇ sᴜʀᴇ I ᴀᴍ ᴀɴ ᴀᴅᴍɪɴ ɪɴ ʏᴏᴜʀ ᴄʜᴀᴛ ᴡɪᴛʜ ᴀᴅᴍɪɴ ʀɪɢʜᴛs.</blockquote>",
        reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton('➕️ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ➕️', url=f"https://t.me/{bot_username}?startchannel&admin=change_info+post_messages+edit_messages+delete_messages+restrict_members+invite_users+pin_messages+manage_topics+manage_video_chats+anonymous+manage_chat+post_stories+edit_stories+delete_stories")
        ], [
            InlineKeyboardButton('Hᴇʟᴘ', callback_data='help_button'),
            InlineKeyboardButton('Aʙᴏᴜᴛ', callback_data='about_button')
        ], [
            InlineKeyboardButton("🌐 Uᴘᴅᴀᴛᴇ", url=f"https://t.me/RxBotz"),
            InlineKeyboardButton("📜 Sᴜᴘᴘᴏʀᴛ", url="https://t.me/+zb9_Za9m2kI4NzM1")
        ]])
    )    

# Command to set a custom caption
@Client.on_message(filters.command(["set_caption", "set"]) & filters.channel)
async def set_caption(bot, message):
    if len(message.command) < 2:
        return await message.reply(
            "<b>Provide a caption to set</b>\n<u>Example:</u> ⬇️\n\n<code>/set_caption {file_name}\n\n{file_caption}\n\nsize » {file_size}\n\nJoin :- @your_channel</code>"
        )
    chnl_id = message.chat.id
    caption = message.text.split(" ", 1)[1]
    chk_data = await chnl_ids.find_one({"chnl_id": chnl_id})
    if chk_data:
        await updateCap(chnl_id, caption)
        return await message.reply(f"Caption updated successfully:\n\n`{caption}`")
    else:
        await addCap(chnl_id, caption)
        return await message.reply(f"Caption added successfully:\n\n`{caption}`")

# Command to delete a custom caption
@Client.on_message(filters.command(["delcaption", "del_caption", "delete_caption", "del"]) & filters.channel)
async def del_caption(_, msg):
    chnl_id = msg.chat.id
    try:
        await chnl_ids.delete_one({"chnl_id": chnl_id})
        return await msg.reply("<b>Caption deleted successfully. Default caption will be used.</b>")
    except Exception as e:
        rkn = await msg.reply(f"Error: {e}")
        await asyncio.sleep(5)
        await rkn.delete()

# Extract language from the caption
def extract_language(default_caption):
    language_pattern = r'\b(Hindi|English|Tamil|Telugu|Malayalam|Gujarati|Kannada|Indonesian|Danish|Urdu|Korean|Chinese|Japanese|Hin|Tam|Tel|Ben|Guj|Mal|Mar|Kan|Eng|Kor|Chi|jap)\b'  # Extend with more languages if necessary
    languages = set(re.findall(language_pattern, default_caption, re.IGNORECASE))
    if not languages:
        return None  # Return None if no languages are found 
    return ", ".join(sorted(languages, key=str.lower))

# Extract year from the caption
def extract_year(default_caption):
    match = re.search(r'\b(19\d{2}|20\d{2})\b', default_caption)
    return match.group(1) if match else None

#Command to set prefix in caption
@Client.on_message(filters.command("set_prefix") & filters.channel)
async def set_prefix(bot, message):
    chnl_id = message.chat.id
    
    if len(message.command) < 2:
        return await message.reply("<b>Provide a prefix to set</b>\n<u>Example:</u> ⬇️\n\n<code>/set_prefix @rxbotz~</code>")
    
    prefix = message.text.split(" ", 1)[1]
    
    chk_data = await chnl_ids.find_one({"chnl_id": chnl_id})
    if chk_data:
        await chnl_ids.update_one(
            {"chnl_id": chnl_id},
            {"$set": {"prefix": prefix}}
        )
        return await message.reply(f"Prefix set for this channel ✅: {prefix}")
    else:
        await chnl_ids.insert_one({"chnl_id": chnl_id, "prefix": prefix})
        return await message.reply(f"Prefix set for this channel ✅: {prefix}")


# Command to clear prefix from caption
@Client.on_message(filters.command("clear_prefix") & filters.channel)
async def clear_prefix(bot, message):
    chnl_id = message.chat.id
    
    try:
        await chnl_ids.update_one(
            {"chnl_id": chnl_id},
            {"$unset": {"prefix": ""}}
        )
        return await message.reply("Prefix has been cleared for this channel.")
    except Exception as e:
        rkn = await message.reply(f"Error: {e}")
        await asyncio.sleep(5)
        await rkn.delete()


# Command to set suffix in caption
@Client.on_message(filters.command("set_suffix") & filters.channel)
async def set_suffix(bot, message):
    chnl_id = message.chat.id
    
    # Ensure the user has provided a suffix
    if len(message.command) < 2:
        return await message.reply("<b>Provide a suffix to set</b>\n<u>Example:</u> ⬇️\n\n<code>/set_suffix ~@rxbotz</code>")
    
    # Extract suffix from the message
    suffix = message.text.split(" ", 1)[1]
    
    # Save or update the suffix in the database
    chk_data = await chnl_ids.find_one({"chnl_id": chnl_id})
    if chk_data:
        await chnl_ids.update_one(
            {"chnl_id": chnl_id},
            {"$set": {"suffix": suffix}}
        )
        return await message.reply(f"Suffix set for this channel ✅: {suffix}")
    else:
        await chnl_ids.insert_one({"chnl_id": chnl_id, "suffix": suffix})
        return await message.reply(f"Suffix set for this channel ✅: {suffix}")


# Command to clear suffix from caption
@Client.on_message(filters.command("clear_suffix") & filters.channel)
async def clear_suffix(bot, message):
    chnl_id = message.chat.id
    
    # Remove the suffix setting from the database
    try:
        await chnl_ids.update_one(
            {"chnl_id": chnl_id},
            {"$unset": {"suffix": ""}}
        )
        return await message.reply("Suffix has been cleared for this channel.")
    except Exception as e:
        rkn = await message.reply(f"Error: {e}")
        await asyncio.sleep(5)
        await rkn.delete()
        
# Generate greetings based on the current time
def generate_wish():
    current_hour = datetime.now().hour
    if 5 <= current_hour < 12:
        return "Good Morning"
    elif 12 <= current_hour < 17:
        return "Good Afternoon"
    elif 17 <= current_hour < 21:
        return "Good Evening"
    else:
        return "Good Night"

# Command to set words replacement (original word -> replacement word)
@Client.on_message(filters.command("replace_words") & filters.channel)
async def replace_words(bot, message):
    chnl_id = message.chat.id
    if len(message.command) < 3:
        return await message.reply(
            "<b>Provide the words to replace and their replacements</b>\n<u>Example:</u> ⬇️\n\n<code>/replace_words oldword1 newword1 oldword2 newword2</code>"
        )
    
    # Split the message text to get the word pairs (after the command)
    words = message.text.split(" ")[1:]
    if len(words) % 2 != 0:
        return await message.reply(
            "<b>Please provide pairs of words: original -> replacement</b>\n<u>Example:</u> ⬇️\n\n<code>/replace_words oldword1 newword1 oldword2 newword2</code>"
        )
    
    # Create a list of tuples for word replacements
    word_pairs = [(words[i], words[i+1]) for i in range(0, len(words), 2)]
    
    # Fetch existing data from the database
    chk_data = await chnl_ids.find_one({"chnl_id": chnl_id})
    if chk_data:
        # Update word replacement mapping in the database
        replace_words = chk_data.get("replace_words", [])
        replace_words.extend(word_pairs)  # Add new word pairs to the list
        await chnl_ids.update_one(
            {"chnl_id": chnl_id},
            {"$set": {"replace_words": replace_words}}
        )
        return await message.reply(f"Word replacements set for this channel ✅:\n" + "\n".join([f"{original} -> {replacement}" for original, replacement in word_pairs]))
    else:
        await chnl_ids.insert_one({"chnl_id": chnl_id, "replace_words": word_pairs})
        return await message.reply(f"Word replacements set for this channel ✅:\n" + "\n".join([f"{original} -> {replacement}" for original, replacement in word_pairs]))

# Command to turn off replace words
@Client.on_message(filters.command("del_replace_word") & filters.channel)
async def del_replace_word(bot, message):
    chnl_id = message.chat.id
    
    try:
        await chnl_ids.update_one(
            {"chnl_id": chnl_id},
            {"$unset": {"replace_words": ""}}
        )
        return await message.reply("Word replacements list has been reset for this channel.")
    except Exception as e:
        rkn = await message.reply(f"Error: {e}")
        await asyncio.sleep(5)
        await rkn.delete()

    # Command to view current caption settings
@Client.on_message(filters.command("view") & filters.channel)
async def view_caption(bot, message):
    chnl_id = message.chat.id
    chk_data = await chnl_ids.find_one({"chnl_id": chnl_id})
    
    if chk_data:
        current_caption = chk_data.get("caption", "No custom caption set.")
        prefix = chk_data.get("prefix", "None")
        suffix = chk_data.get("suffix", "None")
        removable_words = chk_data.get("removable_words", None)
        replace_words = chk_data.get("replace_words", None)
        
        if removable_words:
            removable_words_text = ", ".join(removable_words)
        else:
            removable_words_text = "None"
        
        if replace_words:
            replace_words_text = ", ".join([f"{original} -> {replacement}" for original, replacement in replace_words])
        else:
            replace_words_text = "None"
        
        return await message.reply(
            f"<b>Channel Details</b>\n\n"
            f"<b>Prefix:</b> {prefix}\n"
            f"<b>Suffix:</b> {suffix}\n"
            f"<b>Removable Words:</b> {removable_words_text}\n"
            f"<b>Replace Words:</b> {replace_words_text}\n\n"
            f"<b>Caption Template:</b>\n{current_caption}"
        )
    else:
        return await message.reply("<b>No custom caption set. Using the default caption.</b>")


# Command to set removable words
@Client.on_message(filters.command("rem_words") & filters.channel)
async def rem_words(bot, message):
    chnl_id = message.chat.id
    if len(message.command) < 2:
        return await message.reply(
            "<b>Provide words to remove</b>\n<u>Example:</u> ⬇️\n\n<code>/rem_words test mkv</code>"
        )
    
    words_to_remove = message.text.split(" ", 1)[1]
    words_list = re.findall(r'\S+', words_to_remove)
    
    chk_data = await chnl_ids.find_one({"chnl_id": chnl_id})
    if chk_data:
        await chnl_ids.update_one(
            {"chnl_id": chnl_id},
            {"$set": {"removable_words": words_list}}
        )
        return await message.reply(f"Words to remove set for this channel ✅: {', '.join(words_list)}")
    else:
        await chnl_ids.insert_one({"chnl_id": chnl_id, "removable_words": words_list})
        return await message.reply(f"Words to remove set for this channel ✅: {', '.join(words_list)}")


# Command to turn off removable words
@Client.on_message(filters.command("rem_words_off") & filters.channel)
async def rem_words_off(bot, message):
    chnl_id = message.chat.id
    
    try:
        await chnl_ids.update_one(
            {"chnl_id": chnl_id},
            {"$unset": {"removable_words": ""}}
        )
        return await message.reply("Removable words list has been reset for this channel.")
    except Exception as e:
        rkn = await message.reply(f"Error: {e}")
        await asyncio.sleep(5)
        await rkn.delete()


# Function to format duration in HH:MM:SS
def format_duration(duration_seconds):
    # Ensure that duration is an integer and not a floating-point number
    duration_seconds = int(duration_seconds)  # Cast to integer to discard decimals
    
    hours = duration_seconds // 3600
    minutes = (duration_seconds % 3600) // 60
    seconds = duration_seconds % 60
    
    # Return the formatted duration
    return f"{hours:02}:{minutes:02}:{seconds:02}"

# Function to extract quality from the media title
def extract_quality(title):
    # Define possible quality numbers and terms
    quality_numbers = ["480p", "720p", "1080p", "1440p", "2K", "4K", "8K"]
    quality_terms = ["Blu-ray", "WEB-DL", "HDRip", "DVDRip", "CAM", "SD", "HD", "HDR", "Bluray", "BluRay", "bluray", "bluRay", "WEBDL", "Webdl", "WEBRip", "WebRip", "CAMRIP", "HDTS"]

    # Search for quality numbers in the title
    found_quality_number = [quality for quality in quality_numbers if quality in title]

    # Search for quality terms in the title
    found_quality_terms = [term for term in quality_terms if term in title]

    # Combine the first found quality number and terms
    quality_number = found_quality_number[0] if found_quality_number else "Unknown"
    quality_terms_str = ", ".join(found_quality_terms) if found_quality_terms else "Unknown"

    # Return combined quality string in the format: quality number (terms)
    return f"{quality_number} ({quality_terms_str})"

# Function to extract language (dummy function for now)
def extract_language(title):
    # Simple placeholder function, can be modified based on actual need
    return "Hindi" if "Hindi" in title else "English"

# Function to extract year (dummy function for now)
def extract_year(title):
    # Look for year pattern in parentheses, e.g., (2008)
    year_match = re.search(r"(\d{4})", title)
    return year_match.group(1) if year_match else "Unknown"

global_button = None  # Global variable to store the button

@Client.on_message(filters.private & filters.user(Rkn_Bots.ADMIN) & filters.command("add_button"))
async def add_button(bot, message):
    global global_button
    
    # Get the command arguments (button name and URL)
    command_args = message.text.split(" ", 2)
    
    # If there are not enough arguments, ask for the correct format
    if len(command_args) < 3:
        await message.reply("Please provide the button title and URL. Example: /add_button [testing] [https://t.me/RxBotz]")
        return
    
    # Extract button name and URL from the arguments
    button_name = command_args[1].strip("[]")  # Extract the button name without brackets
    button_url = command_args[2].strip("[]")  # Remove any spaces around the URL
    
    # Validate the URL format
    if not re.match(r'^https?://', button_url):
        await message.reply("Invalid URL. Please provide a valid URL starting with 'http://' or 'https://'.")
        return
    
    # Create the inline keyboard button
    button = InlineKeyboardButton(button_name, url=button_url)
    global_button = InlineKeyboardMarkup([[button]])  # Store the button globally
    
    await message.reply(f"Global button '{button_name}' set. It will be applied to all media in the channel.")

@Client.on_message(filters.private & filters.user(Rkn_Bots.ADMIN) & filters.command("del_button"))
async def del_button(bot, message):
    global global_button
    
    # Remove the global button by setting it to None
    global_button = None
    await message.reply("Global button has been deleted and will no longer be applied to media.")

@Client.on_message(filters.channel)
async def auto_edit_caption(bot, message):
    global global_button  # Use the global button
    
    chnl_id = message.chat.id
    if message.media:
        for file_type in ("video", "audio", "document", "voice"):
            obj = getattr(message, file_type, None)
            if obj and hasattr(obj, "file_name"):
                file_name = obj.file_name
                file_size = obj.file_size  # Get file size in bytes

                # Get duration (in seconds) for video or audio
                duration_seconds = getattr(obj, "duration", None)

                # Convert file size to human-readable format
                if file_size < 1024:
                    file_size_text = f"{file_size} B"
                elif file_size < 1024**2:
                    file_size_text = f"{file_size / 1024:.2f} KB"
                elif file_size < 1024**3:
                    file_size_text = f"{file_size / 1024**2:.2f} MB"
                else:
                    file_size_text = f"{file_size / 1024**3:.2f} GB"

                file_name = re.sub(r"@\w+\s*", "", file_name).replace("_", " ").replace(".", " ")

                cap_dets = await chnl_ids.find_one({"chnl_id": chnl_id})
                prefix = cap_dets.get("prefix", "")
                suffix = cap_dets.get("suffix", "")
                removable_words = cap_dets.get("removable_words", [])
                replace_words = cap_dets.get("replace_words", [])
                current_caption = cap_dets.get("caption", "")

                # Process word replacements
                for original, replacement in replace_words:
                    file_name = file_name.replace(original, replacement)
                
                # Remove words based on the removable words list
                for word in removable_words:
                    file_name = file_name.replace(word, "")
                
                # Apply prefix and suffix to the caption
                if prefix:
                    file_name = f"{prefix} {file_name}"
                
                if suffix:
                    file_name = f"{file_name} {suffix}"

                # Extract language, year, and quality from the file name
                language = extract_language(file_name)  # Extract language from file name
                year = extract_year(file_name)  # Extract year from file name
                quality = extract_quality(file_name)  # Extract quality from file name

                # Process word replacements in the caption as well (for {file_caption})
                caption_text = message.caption or "No caption"
                for original, replacement in replace_words:
                    caption_text = caption_text.replace(original, replacement)

                # Remove words from the caption based on removable words list
                for word in removable_words:
                    caption_text = caption_text.replace(word, "")

                # Add time-based wish
                wish = generate_wish()

                # Subtitle Extraction: Check for "ESub" or "MSub"
                subtitles = ""
                if "ESub" in file_name or "ESub" in caption_text:
                    subtitles = "ESub"
                elif "MSub" in file_name or "MSub" in caption_text:
                    subtitles = "MSub"

                # Get the duration in HH:MM:SS format if available
                duration_text = ""
                if duration_seconds:
                    duration_text = format_duration(duration_seconds)

                try:
                    replaced_caption = current_caption.format(
                        file_name=file_name,
                        file_size=file_size_text,
                        file_caption=caption_text,  # Updated caption with replacements and removals
                        language=language,
                        year=year,
                        quality=quality,  # Include quality
                        wish=wish,
                        subtitles=subtitles,  # Include subtitles (ESub or MSub)
                        duration=duration_text  # Add the duration placeholder
                    )

                    await message.edit(replaced_caption, reply_markup=global_button if global_button else None)

                except FloodWait as e:
                    await asyncio.sleep(e.x)
                    continue
    return
