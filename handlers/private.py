from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from config import BOT_USERNAME, BOT_NAME as bot
from helpers.filters import command, other_filters2
# EfsaneMusicVaves tarafından düzenlendi. 

@Client.on_message(command(["start", f"start@{BOT_USERNAME}"]))
async def start(_, message: Message):
                await message.reply_photo(
                "https://te.legra.ph/file/6a98b64bbdf7e60845729.jpg",
                caption=(f"""**Salam {message.from_user.mention} 🎵\nMən Qruplar üçün hazırlanmış musiqi botuyam!\n Bot @qarabagizim Tərəfindən 0dan tərcümə edilib.\n\nSahibim 👉 [Qarabag](https://t.me/Qarabagizim)**"""),
         reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Qrupa Əlavə et 🧨", url=f"http://t.me/EngilshChattingMusicBot?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🎭 Asistant", url="https://t.me/Siyahmusicasistant"
                    )
                    InlineKeyboardButton(
                        "🔥 Qrup", url="https://t.me/QarabagTeams"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "☄️ Əmrlər" , callback_data= "cbbilgi"
                    ),
                    InlineKeyboardButton(
                        "Sahib 🇦🇿", url=f"https://t.me/qarabagizim"
                    )
                ]
                
           ]
        ),
    )
  


@Client.on_message(command(["bilgi", f"bilgi@{BOT_USERNAME}"]))
async def bilgi(_, message: Message):
      await message.reply_text(" ❗ Qeyd:\n Botun aktiv işləməsi üçün bu üç yetki vermək lazımdır ⬇️:\n- Mesaj silmə yetkisi,\n- Bağlantı ilə dəvət etmə yetkisi,\n- Səsli səhbəti yönətmə yetkisi.", 
      reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "🔴 İstifatəçi Əmrləri", callback_data="herkes")
                 ],[                     
                     InlineKeyboardButton(
                         "⚫ Admin  Əmrləri", callback_data="admin")
                 ],[
                     InlineKeyboardButton(
                         "Geri 🔄", callback_data="cbstart")
                 ],[
                     InlineKeyboardButton(
                         "Qrup ☘️", url="https://t.me/QarabagTeams")
                 ]
             ]
         )
    )


@Client.on_callback_query(filters.regex("cbbilgi"))
async def cbbilgi(_, query: CallbackQuery):
    await query.edit_message_text(" ❗ Qeyd:\nBotun aktiv işləməsi üçün bu üç yetki vermək lazımdır ⬇️\n- Mesaj silmə yetkisi.\n- Bağlantı ilə dəvət etmə yetkisi.\n- Səsli söhbəti yönətmə yetkisi.", 
    reply_markup=InlineKeyboardMarkup(
      [
        [
          InlineKeyboardButton(
            "✨ Hərkəs üçün əmrlər", callback_data ="herkes")
        ],
        [
          InlineKeyboardButton(
            "👑 Admin əmrləri",callback_data ="admin")
        ],
        [
          InlineKeyboardButton(
            "🔄 Geri", callback_data="cbstart")
        ],
        [
          InlineKeyboardButton(
            "Sahib 🇦🇿", url="https://t.me/qarabagizim")
        ]
      ]
     ))


@Client.on_callback_query(filters.regex("herkes"))
async def herkes(_, query: CallbackQuery):
    await query.edit_message_text(f"""<b>Salam {query.from_user.mention}!\nBu botun hərkəs üçün əmr menyusu 😉\n\n ▶️ /play - Musiqi oxutmaq üçün youtube url'sinə vəya musiqi dosyasına yanıt verin\n ▶️ /play <song name> - İstədiyiniz musiqi oxut\n 🔴 \n 🎵 /song <song name> - İstədiyiniz musiqi sürətli bir şəkildə axtarın\n 🎵 /vbul - İstədiyiniz videoları sürətli bir şəkildə axtarın\n 🔍 /video <query> - Youtube'da olan videoları axtarın\n\n</b>""",
    reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "Sahib 🇦🇿", url="https://t.me/qarabagizim")
                 ],
                 [
                     InlineKeyboardButton(
                         "️🔄 Geri", callback_data="cbbilgi")
                 ] 
             ]
         )
         )


@Client.on_callback_query(filters.regex("admin"))
async def admin(_, query: CallbackQuery):
    await query.edit_message_text(f"""<b>Salam {query.from_user.mention}!\nBu botun adminlər üçün əmr menyusu 🤩\n\n ▶️ /resume - Musiqi oxutmağa davam et\n ⏸️ /durdur - Oxuyan musiqini dayandır\n 🔄 /atla - Sıraya alınmış musiqiyə keç\n ⏹ /skip - Musiqi oxumanı dayandır\n 🔼 /promote - Botun sadəcə yönətici üçün olan əmrlərini istifadə üçün istifadəçiyə yetki ver\n 🔽 /demote - Botun yönətici əmrlərini istifadə edən istifadəçinin yetkisini al\n\n ⚪ /asistan - Musiqi asistanı qrupunuza qoşulur.\n\n</b>""",
    reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "Qrup ⛓️", url="https://t.me/QarabagTeams")
                 ],
                 [
                     InlineKeyboardButton(
                         "️🔄 Geri", callback_data="cbbilgi")
                 ] 
             ]
         )
         )


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(f"""**Salam {query.from_user.mention} 🎵\nMən Qruplar üçün hazırlanmış musiqi botuyam.\Bot @Vusaliw Tərəfindən 0dan tərcümə edilib.\n\nSahibim👉 [Vüsal](https://t.me/Vusallldi)**""",
         reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Qrupa Əlavə Et 🧨", url=f"http://t.me/EngilshChattingMusicBot?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🎭 Asistant", url="https://t.me/Siyahmusicasistant"
                    ),
                    InlineKeyboardButton(
                        "⚡ Qrup", url="https://t.me/QarabagTeams"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "☄️ Əmrlər" , callback_data= "cbbilgi"
                    ),
                    InlineKeyboardButton(
                        "Sahib 🇦🇿", url=f"https://t.me/qarabagizim"
                    )
                ]
                
           ]
        ),
    )
