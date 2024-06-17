import random 
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden
from PROFESSOR import app

MISHI = [
    "https://telegra.ph/file/c2ff050b35f2a1aeecc09.jpg",
    "https://telegra.ph/file/c2ff050b35f2a1aeecc09.jpg",
    "https://telegra.ph/file/463dd0acf84d4b1ae10b0.jpg",
    "https://telegra.ph/file/e2cba3be8cc93a534435f.jpg",
]

#--------------------------

MUST_JOIN = "https://t.me/+wE8H1Xl6NnBiNzg9"
#------------------------
@app.on_message(filters.incoming & filters.private, group=-1)
async def must_join_channel(app: Client, msg: Message):
    if not MUST_JOIN:
        return
    try:
        try:
            await app.get_chat_member(MUST_JOIN, msg.from_user.id)
        except UserNotParticipant:
            if MUST_JOIN.isalpha():
                link = "https://t.me/" + MUST_JOIN
            else:
                chat_info = await app.get_chat(MUST_JOIN)
                link = chat_info.invite_link
            try:
                await msg.reply_photo(random.choice(MISHI), caption=f"❅ Hᴇʏ I ᴀᴍ Rɪsᴇ ғɪʀsᴛ ᴜɴ Jɪᴏɴ ᴛʜᴇ ɢʀᴏᴜᴘ ᴛʜᴇɴ sᴛᴀʀᴛ ᴛʜᴇ Bᴏᴛ OK ᴛʜᴀɴᴋʏᴏᴜ  ",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇ", url="https://t.me/DevilCommunityyy"),
                                InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url=link),
                            ]
                        ]
                    )
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"๏ ᴘʀᴏᴍᴏᴛᴇ ᴍᴇ ᴀs ᴀɴ ᴀᴅᴍɪɴ ɪɴ ᴛʜᴇ ᴍᴜsᴛ_ᴊᴏɪɴ ᴄʜᴀᴛ ๏: {MUST_JOIN} !")
      
