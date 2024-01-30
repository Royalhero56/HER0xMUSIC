from typing import Union

from pyrogram.types import InlineKeyboardButton

import config
from AarohiX import app


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="🥺 ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴩ 🥺",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="❣️ʜᴇʟᴩ❣️",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="❤‍🔥sᴇᴛᴛɪɴɢs❤‍🔥", callback_data="settings_helper"
            ),
        ],
        [
            InlineKeyboardButton(
                text="💞ᴏᴡɴᴇʀ💞", user_id=OWNER), 
            InlineKeyboardButton(
                text="💓ʙʀᴏᴛʜᴇʀ💓", url=f"https://t.me/@Ayuuubby"
            ),
        ],
        [
            InlineKeyboardButton(
                text="💝ᴍᴀɪɴᴛᴀɪɴᴇʀ💝", url=f"https://t.me/iamcutehero"),
            InlineKeyboardButton(
                text="🥰sᴜᴩᴩᴏʀᴛ🥰", url=config.SUPPORT_GROUP
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="🥺ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴩ🥺",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text="🥺ʜᴇʟᴩ🥺", callback_data="settings_back_helper"
            ),
        ],
        [
            InlineKeyboardButton(
                text="💕ᴏᴡɴᴇʀ💕", user_id=OWNER),
            InlineKeyboardButton(
                text="💓ʙʀᴏᴛʜᴇʀ💓", url=f"https://t.me/Royal_king365"
            ),
        ],
        [
            InlineKeyboardButton(text="💝ᴍᴀɪɴᴛᴀɪɴᴇʀ💝", url=f"https://t.me/iamcutehero"),
            InlineKeyboardButton(
                text="🥰sᴜᴩᴩᴏʀᴛ🥰", url=config.SUPPORT_GROUP
            ),
        ],
        [
            InlineKeyboardButton(
                    text="🥰 ᴍᴏʀᴇ 🥰", url=f"https://t.me/anikahindishayri"
                )
        ],
     ]
    return buttons
