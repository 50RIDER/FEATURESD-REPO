from pyrogram import Client, filters
from plugins.helper_functions.admin_check import admin_check
from plugins.helper_functions.extract_user import extract_user
from plugins.helper_functions.string_handling import extract_time


@Client.on_message(filters.command("ban"))
async def ban_user(_, message):
    is_admin = await admin_check(message)
    if not is_admin:
        return

    user_id, user_first_name = extract_user(message)

    try:
        await message.chat.kick_member(
            user_id=user_id
        )
    except Exception as error:
        await message.reply_text(
            str(error)
        )
    else:
        if str(user_id).lower().startswith("@"):
            await message.reply_text(
                "sᴏᴍᴇᴏɴᴇ ᴇʟsᴇ ɪs ᴅᴜsᴛɪɴɢ ᴏғғ..! "
                f"{user_first_name}"
                " Is forbidden."
            )
        else:
            await message.reply_text(
                "sᴏᴍᴇ ᴇʟsᴇ ɪs ᴅᴜsᴛɪɴɢ ᴏғғ..! "
                f"<a href='tg://user?id={user_id}'>"
                f"{user_first_name}"
                "</a>"
                " Is forbidden."
            )


@Client.on_message(filters.command("tban"))
async def temp_ban_user(_, message):
    is_admin = await admin_check(message)
    if not is_admin:
        return

    if not len(message.command) > 1:
        return

    user_id, user_first_name = extract_user(message)

    until_date_val = extract_time(message.command[1])
    if until_date_val is None:
        await message.reply_text(
            (
                "ɪɴᴠᴀʟɪᴅ ᴛɪᴍᴇ ᴛʏᴘᴇ sᴘᴇᴄɪғɪᴇᴅ "
                "ᴇxᴘᴇᴄᴛᴇᴅ m, h, ᴏʀ d, ɢᴏᴛ ɪᴛ: {}"
            ).format(
                message.command[1][-1]
            )
        )
        return

    try:
        await message.chat.kick_member(
            user_id=user_id,
            until_date=until_date_val
        )
    except Exception as error:
        await message.reply_text(
            str(error)
        )
    else:
        if str(user_id).lower().startswith("@"):
            await message.reply_text(
                "sᴏᴍᴇᴏɴᴇ ᴇʟsᴇ ɪs ᴅᴜsᴛɪɴɢ ᴏғғ..! "
                f"{user_first_name}"
                f" ʙᴀɴɴᴇᴅ ғᴏʀ {message.command[1]}!"
            )
        else:
            await message.reply_text(
                "sᴏᴍᴇᴏɴᴇ ᴇʟsᴇ ɪs ᴅᴜsᴛɪɴɢ ᴏғғ..! "
                f"<a href='tg://user?id={user_id}'>"
                "Lavane"
                "</a>"
                f" ʙᴀɴɴᴇᴅ ғᴏʀ {message.command[1]}!"
            )
