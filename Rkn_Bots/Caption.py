
# (c) @RknDeveloperr
# Rkn Developer 
# Don't Remove Credit 😔
# Telegram Channel @RknDeveloper & @Rkn_Botz
# Developer @RknDeveloperr

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import Client, filters, errors, types
from config import Rkn_Bots
import asyncio, re, time, sys
from .database import total_user, getid, delete, addCap, updateCap, insert, chnl_ids
from pyrogram.errors import FloodWait

@Client.on_message(filters.private & filters.user(Rkn_Bots.ADMIN)  & filters.command(["rknusers"]))
async def all_db_users_here(client, message):
    start_t = time.time()
    rkn = await message.reply_text("Processing...")
    uptime = time.strftime("%Hh%Mm%Ss", time.gmtime(time.time() - client.uptime))    
    total_users = await total_user()
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rkn.edit(text=f"**--Bot Processed--** \n\n**Bot Started UpTime:** {uptime} \n**Bot Current Ping:** `{time_taken_s:.3f} ᴍꜱ` \n**All Bot Users:** `{total_users}`")


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
            InlineKeyboardButton('➕ ADD TO CHANNEL ➕', url=f"https://t.me/{bot.me.username}?startchannel&admin=change_info+post_messages+edit_messages+delete_messages+restrict_members+invite_users+pin_messages+manage_topics+manage_video_chats+anonymous+manage_chat+post_stories+edit_stories+delete_stories")
        ], [
            InlineKeyboardButton('🍃 HELP', callback_data='help_button'),
            InlineKeyboardButton('🍁 ABOUT', callback_data='about_button')
        ]])
    )

# Handle the "HELP" button callback
@Client.on_callback_query(filters.regex('help_button'))
async def help_callback(bot, callback_query):
    help_text = """ •••[( Get Help )]•••

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

    await callback_query.message.edit_text(
        help_text,
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton('🏷️ HTML TAGS', callback_data='html_tags_button'),
            InlineKeyboardButton('🔙 Back', callback_data='start')
        ], [
            InlineKeyboardButton('❌ Close', callback_data='close_help')
        ]]))

# Handle the "HTML TAGS" button callback
@Client.on_callback_query(filters.regex('html_tags_button'))
async def html_tags_callback(bot, callback_query):
    html_tags_text = """🔰 About Caption Font

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

➢ Hyperlink Text
☞ <code>&lt;a href="https://t.me/RxBotz"&gt;{filename}&lt;/a&gt;</code>"""

    await callback_query.message.edit_text(
        html_tags_text,
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton('🔙 Back', callback_data='help_button'),
            InlineKeyboardButton('❌ Close', callback_data='close_html_tags')
        ]]))

# Handle "CLOSE" action
@Client.on_callback_query(filters.regex('close_help'))
async def close_help_callback(bot, callback_query):
    await callback_query.message.delete()

@Client.on_callback_query(filters.regex('close_html_tags'))
async def close_html_tags_callback(bot, callback_query):
    await callback_query.message.delete()

# Handle the "ABOUT" button callback
@Client.on_callback_query(filters.regex('about_button'))
async def about_callback(bot, callback_query):
    bot_username = (await bot.get_me()).username  # Ensure the bot's username is fetched here
    ABOUT_TXT = f"""<b><blockquote>⍟───[ MY ᴅᴇᴛᴀɪʟꜱ ]───⍟</blockquote>
    
‣ ᴍʏ ɴᴀᴍᴇ : <a href=https://t.me/{bot_username}>{bot_username}</a>
‣ ᴍʏ ʙᴇsᴛ ғʀɪᴇɴᴅ : <a href='tg://settings'>ᴛʜɪs ᴘᴇʀsᴏɴ</a> 
‣ ᴅᴇᴠᴇʟᴏᴘᴇʀ : <a href='https://t.me/RxBotz'>ʀ'x ʙᴏᴛᴢ</a> 
‣ ʟɪʙʀᴀʀʏ : <a href='https://docs.pyrogram.org/'>ᴘʏʀᴏɢʀᴀᴍ</a> 
‣ ʟᴀɴɢᴜᴀɢᴇ : <a href='https://www.python.org/download/releases/3.0/'>ᴘʏᴛʜᴏɴ 3</a> 
‣ ᴅᴀᴛᴀ ʙᴀsᴇ : <a href='https://www.mongodb.com/'>ᴍᴏɴɢᴏ ᴅʙ</a> 
‣ ʙᴏᴛ sᴇʀᴠᴇʀ : <a href='https://heroku.com'>ʜᴇʀᴏᴋᴜ</a> 
‣ ʙᴜɪʟᴅ sᴛᴀᴛᴜs : ᴠ2.7.1 [sᴛᴀʙʟᴇ]</b>"""
    
    await callback_query.message.edit_text(
        ABOUT_TXT,
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton('Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ', url='https://t.me/RxBotz')
        ], [
            InlineKeyboardButton('🔙 Back', callback_data='start'),
            InlineKeyboardButton('❌ Close', callback_data='close_about')
        ]]))

# Handle "CLOSE" action for ABOUT button
@Client.on_callback_query(filters.regex('close_about'))
async def close_about_callback(bot, callback_query):
    await callback_query.message.delete()

# Handle "BACK" to the main START message
@Client.on_callback_query(filters.regex('start'))
async def back_to_start_callback(bot, callback_query):
    bot_username = (await bot.get_me()).username  # Get the bot's username
    await callback_query.message.edit_caption(
        caption=f"ʜᴇʏ, {callback_query.from_user.mention}\n\nI ᴀᴍ ᴀ ᴀᴅᴠᴀɴᴄᴇᴅ ᴀᴜᴛᴏᴄᴀᴘᴛɪᴏɴʙᴏᴛ. ᴠᴇʀʏ sɪᴍᴘʟᴇ ᴛᴏ ᴜsᴇ ᴍᴇ. ᴊᴜsᴛ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ᴍᴀᴋᴇ ᴍᴇ ᴀɴ ᴀᴅᴍɪɴ ᴏᴠᴇʀ ᴛʜᴇʀᴇ. ᴛʜᴇɴ sᴇᴛ Yᴏᴜʀ Cᴀᴘᴛɪᴏɴ Bʏ Usɪɴɢ <mono>/set</mono> & <mono>/setCaption</mono> Cᴏᴍᴍᴀɴᴅ ғᴏʀ ᴇɴᴀʙʟɪɴɢ ᴀᴜᴛᴏᴄᴀᴘᴛɪᴏɴ.\n\n"
                f"<blockquote>ɴᴏᴛᴇ: Mᴀᴋᴇ sᴜʀᴇ I ᴀᴍ ᴀɴ ᴀᴅᴍɪɴ ɪɴ ʏᴏᴜʀ ᴄʜᴀᴛ ᴡɪᴛʜ ᴀᴅᴍɪɴ ʀɪɢʜᴛs.</blockquote>",
        reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton('➕ ADD TO CHANNEL ➕', url=f"https://t.me/{bot_username}?startchannel&admin=change_info+post_messages+edit_messages+delete_messages+restrict_members+invite_users+pin_messages+manage_topics+manage_video_chats+anonymous+manage_chat+post_stories+edit_stories+delete_stories")
        ], [
            InlineKeyboardButton('🍃 HELP', callback_data='help_button'),
            InlineKeyboardButton('🍁 ABOUT', callback_data='about_button')
        ]]))
    

# Command to set the caption for the channel
@Client.on_message(filters.command("set_caption") & filters.channel)
async def setCaption(bot, message):
    if len(message.command) < 2:
        return await message.reply(
            "Example: /set_caption <code>set your caption (use {file_name} to show file name)</code>"
        )

    chnl_id = message.chat.id
    caption = message.text.split(" ", 1)[1] if len(message.text.split(" ", 1)) > 1 else None
    if caption is None:
        return await message.reply("Please provide a valid caption.")

    try:
        chkData = await chnl_ids.find_one({"chnl_id": chnl_id})

        if chkData:
            await updateCap(chnl_id, caption)
            return await message.reply(f"Successfully Updated Your Caption.\n\nYour New Caption: `{caption}`")
        else:
            await addCap(chnl_id, caption)
            return await message.reply(f"Successfully Added Your Caption.\n\nYour New Caption: `{caption}`")
    except Exception as e:
        return await message.reply(f"An error occurred while updating the caption: {e}")

# Command to delete the caption from the channel
@Client.on_message(filters.command(["delcaption", "del_caption", "delete_caption"]) & filters.channel)
async def delCaption(_, msg):
    chnl_id = msg.chat.id
    try:
        result = await chnl_ids.delete_one({"chnl_id": chnl_id})
        if result.deleted_count > 0:
            return await msg.reply("<b>Successfully deleted your caption. I will now use my default caption.</b>")
        else:
            return await msg.reply("<b>No caption was found to delete.</b>")
    except Exception as e:
        rkn = await msg.reply(f"Error occurred: {e}")
        await asyncio.sleep(5)
        await rkn.delete()

# Automatically edits the caption of the message based on stored caption
@Client.on_message(filters.channel)
async def auto_edit_caption(bot, message):
    chnl_id = message.chat.id
    if message.media:
        for file_type in ("video", "audio", "document", "voice"):
            obj = getattr(message, file_type, None)

            if obj and hasattr(obj, "file_name"):
                file_name = obj.file_name
                file_size = obj.file_size  # Get file size in bytes
                file_size_text = format_file_size(file_size)  # Assuming you have a function for this

                # Clean up the file name
                file_name = re.sub(r"@\w+\s*", "", file_name).replace("_", " ").replace(".", " ")

                # Extract additional file details
                file_details = extract_file_details(file_name)

                try:
                    cap_dets = await chnl_ids.find_one({"chnl_id": chnl_id})

                    if cap_dets:
                        cap = cap_dets["caption"]
                        replaced_caption = cap.format(
                            file_name=file_name,
                            file_size=file_size_text,
                            file_caption=message.caption or "No caption",
                            file_language=file_details["file_language"],
                            year=file_details["year"],
                            file_quality=file_details["file_quality"],
                            file_duration=file_details["file_duration"]
                        )
                        await message.edit(replaced_caption)
                    else:
                        replaced_caption = Rkn_Bots.DEF_CAP.format(
                            file_name=file_name,
                            file_size=file_size_text,
                            file_caption=message.caption or "No caption",
                            file_language=file_details["file_language"],
                            year=file_details["year"],
                            file_quality=file_details["file_quality"],
                            file_duration=file_details["file_duration"]
                        )
                        await message.edit(replaced_caption)

                except FloodWait as e:
                    await asyncio.sleep(e.x)
                    continue
                except Exception as e:
                    await message.reply(f"An error occurred while editing the caption: {e}")

    return

# Rkn Developer 
# Don't Remove Credit 😔
# Telegram Channel @RknDeveloper & @Rkn_Botz
# Developer @RknDeveloperr
