from pyrogram import Client
from pyrogram import filters
from random import shuffle
from pyrogram.types import Message
from kelime_bot import oyun
from kelime_bot.helpers.kelimeler import *
from kelime_bot.helpers.keyboards import *
from pyrogram.errors import FloodWait
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message


keyboard = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("➕ Qrupa Əlavə Et", url=f"http://t.me/SozTapmacaRobot?startgroup=new")
    ],
    [
        InlineKeyboardButton("**Developer | 🧑🏻‍💻 Creator**", url="https://t.me/Axhmedov7"),
        InlineKeyboardButton("**Chat 🎉**", url="https://t.me/RichSuppp"),
    ]
])


START = """
**• Salam 👋

• Mən Söz Oyun Botuyam 🎮 

• Əyləncəli vaxt Keçirmək üçün Mənimlə Oynaya bilərsən ✍🏻 

• Oynamaq üçün məni bir qrupa əlavə edib admin etmək lazımdır . 💭**

➤ Bilgi üçün 👉 /komek Tıklayın. Komutlar Asant və Rahatdır. 
"""

HELP = """
**✌️ Komutlar Menusuna XoşGəldiniz.**
/basla - Oyunu Başladmak üçün..
/pas - Cəmi 3 keçid Haqqınız Var.. 
/reyting - Oyuncular arasındaki Xal bilgisi..
/dayandir - Oyundan çıxmaq üçün lazımlı olan komutdur.. 
"""

# Komutlar. 
@Client.on_message(filters.command("start"))
async def start(bot, message):
  await message.reply_photo("https://i.ibb.co/K6QTywd/images-17.jpg",caption=START,reply_markup=keyboard)

@Client.on_message(filters.command("komek"))
async def help(bot, message):
  await message.reply_photo("https://i.ibb.co/K6QTywd/images-17.jpg",caption=HELP) 

# Oyunu başlat. 
@Client.on_message(filters.command("basla")) 
async def kelimeoyun(c:Client, m:Message):
    global oyun
    aktif = False
    try:
        aktif = oyun[m.chat.id]["aktif"]
        aktif = True
    except:
        aktif = False

    if aktif:
        await m.reply("**❗ Oyun Qrupunuzda Artıq Davam Edir ✍🏻 \n Oyunu dayandırmaq üçün yazın /dayandir")
    else:
        await m.reply(f"**{m.from_user.mention}** Tərəfindən! \nKəlimə Tapma Oyunu Başladı .\n\nBol Şanslar !", reply_markup=kanal)
        
        oyun[m.chat.id] = {"kelime":kelime_sec()}
        oyun[m.chat.id]["aktif"] = True
        oyun[m.chat.id]["round"] = 1
        oyun[m.chat.id]["pass"] = 0
        oyun[m.chat.id]["oyuncular"] = {}
        
        kelime_list = ""
        kelime = list(oyun[m.chat.id]['kelime'])
        shuffle(kelime)
        
        for harf in kelime:
            kelime_list+= harf + " "
        
        text = f"""
🎯 Raund : {oyun[m.chat.id]['round']}/60 
📝 Söz :   <code>{kelime_list}</code>
💰 Qazanacağınız Xal: 1
🔎 İpucu: 1. {oyun[m.chat.id]["kelime"][0]}
✍🏻 Uzunluq : {int(len(kelime_list)/2)} 

✏️ Qarışıq hərflərdən düzgün sözü tapın
        """
        await c.send_message(m.chat.id, text)
        
