from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>👋🏻 Hi {message.from_user.first_name}!</b>
I am a powerful VC music bot of @idanishbaba😁. I am play the musics in your group's VC.
TO PLAY MUSIC ADD ME YOUR GROIP AND PROMOTE ME.
Also add @danishbabamusic.""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⚒COMMANDS", url="https://telegra.ph/MusicBot-Robot-MusicBot-Robo-03-14"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "My CREATOR ☺️", url="https://t.me/idanishbaba"
                    ),
                    InlineKeyboardButton(
                        "Add Me To Group", url="https://t.me/danishbabamusic_bot?startgroup=true"
                    ),
                    
                    InlineKeyboardButton(
                         "Music World", url="https://t.me/joinchat/mkc8fNQ6dtUzZDll"
    
                    )

              ]
@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "💁🏻‍♂️ Do you want to search for a YouTube video?",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✅ Yes", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "No ❌", callback_data="close"
                    )
                ]
            ]
        )
    )
