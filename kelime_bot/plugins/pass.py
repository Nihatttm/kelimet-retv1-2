from pyrogram import Client
from pyrogram import filters
from random import shuffle
from pyrogram.types import Message
from kelime_bot.helpers.keyboards import *
from kelime_bot.helpers.kelimeler import kelime_sec
from kelime_bot import *



@Client.on_message(filters.command("pas") & ~filters.private & ~filters.channel)
async def passs(c:Client, m:Message):
    global oyun
    
    try:
        aktif = oyun[m.chat.id]["aktif"]
        aktif = True
    except:
        aktif = False

    if aktif:
        if oyun[m.chat.id]["pass"] < 3:
            oyun[m.chat.id]["pass"] += 1 
            await c.send_message(m.chat.id,f"❗ Cəmi 3 keçid Haqqınız Var!\n➡️ Kəlimə Geçişi Çıxtı !\n✏️ Doğru kəlimə : **<code>{oyun[m.chat.id]['kelime']}</code>**")
            
            oyun[m.chat.id]["kelime"] = kelime_sec()
            oyun[m.chat.id]["aktif"] = True
            
            kelime_list = ""
            kelime = list(oyun[m.chat.id]['kelime'])
            shuffle(kelime)
            
            for harf in kelime:
                kelime_list+= harf + " "
            
            text = f"""
🎯 Raund : {oyun[m.chat.id]['round']}/60 
📝 Kəlimə :   <code>{kelime_list}</code>
💰 Qazanacağınız Xal : 1
🔎 İ𝗉𝗎𝖼𝗎 : 1. {oyun[m.chat.id]["kelime"][0]}
✍🏻 Uzunluq: {int(len(kelime_list)/2)} 

✏️ Qarışıq hərflərdən düzgün sözü tapın
            """
            await c.send_message(m.chat.id, text)
            
        else:
            await c.send_message(m.chat.id, f"<code>**❗ Geçiş Düz Saxlanıldı! </code> \n Oyunu diyandırmaq üçün /dayandir yazıb diyandıra Bilərsiniz✍🏻**")
    else:
        await m.reply(f"❗ **Qrupunuzda aktif oyun tapılmadı!\n Yeni bir oyuna başlamaq üçün /basla yazabilərsiniz.✍🏻**")
