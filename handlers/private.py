#G-Network Music Projects
#Copyright (C) 2022 By @Groot_Network
#Don't Any Value In This Repo If You Edit Your Github Will Get Banned ๐

import asyncio
from time import time
from datetime import datetime
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from config import BOT_NAME, BOT_USERNAME
from config import BOT_NAME
from config import BOT_USERNAME

@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/bb20e1b39e8d7a31f7cbc.jpg",
        caption=f"""**
โโโโโโโโโโโโโโโโโโโโโโโโ
๐ ๐๐๐ฅ๐๐จ๐ฆ๐**{message.from_user.mention()} ๐**

๐ ๐๐๐ฅ๐ฅ๐จ, ๐ ๐๐ฆ [{BOT_NAME}](https://t.me/{BOT_USERNAME}), ๐ ๐๐ฎ๐ฉ๐๐ซ๐๐๐ฌ๐ญ ๐๐ข๐ ๐ก ๐๐ฎ๐๐ฅ๐ข๐ญ๐ฒ ๐๐จ ๐๐๐  ๐๐ ๐๐ฎ๐ฌ๐ข๐ ๐๐ฅ๐๐ฒ๐๐ซ ๐๐จ๐ญ.

๐ ๐๐ฎ๐ฌ๐ญ ๐๐๐ ๐๐ ยป ๐๐จ ๐๐จ๐ฎ๐ซ ๐๐ซ๐จ๐ฎ๐ฉ ๐๐ง๐ ๐๐ง๐ฃ๐จ๐ฒ ๐๐ฎ๐ฉ๐๐ซ ๐๐ฎ๐๐ฅ๐ข๐ญ๐ฒ โฅ๏ธ๐๐ฎ๐ฌ๐ข๐...
โโโโโโโโโโโโโโโโโโโโโโโโ**""",
    reply_markup=InlineKeyboardMarkup( [[
           InlineKeyboardButton("๐ฑโฐ๐๐ซ๐จ๐จ๐ญ ๐๐๐ญ๐ฐ๐จ๐ซ๐คโฑโจ", url=f"https://t.me/Groot_Network"),
           ],[
           InlineKeyboardButton("๐ธโฐ๐๐ฉ๐๐๐ญ๐๐ฌโฑโจ", url="https://t.me/RJbr0"),  
           InlineKeyboardButton("๐ปโฐ๐๐ข๐ญ ๐๐ฐ๐ง๐๐ซ ๐๐โฑโจ", url="https://t.me/MyNameIsGroot"),
           ],[
           InlineKeyboardButton("๐ฅโฐ๐๐จ๐ฎ๐ซ๐๐ ๐๐จ๐๐โฑโจ", url="https://t.me/TeluguFriendsClub")
           ]]
           )
     )
    
@Client.on_message(command(["Groot"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/0c448c9873a3dcb62673a.jpg",
        caption=f"""**๐ฅ๐ค สธแตแตสณ ๐๐๐๐ฅ๐ง โฑหข ๐ ๐ฌ ๐ฅ๐๐ฆ๐ฃ๐ข๐ก๐ฆ๐๐๐๐๐๐ง๐ฌ๐ค๐ฅ**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "@๐ ๐๐ก๐ฎ๐บ๐ฒ๐๐๐๐ฟ๐ผ๐ผ๐", url=f"https://t.me/MyNameIsGroot")
                ]
            ]
        ),
    )
