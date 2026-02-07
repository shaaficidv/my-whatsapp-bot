import asyncio
from pyrogram import Client, filters
from pytgcalls import PyTgCalls
from pytgcalls.types import AudioPiped
from yt_dlp import YoutubeDL

# --- XOGTAADA ---
API_ID = 36986727
API_HASH = "77510f5c8c8b92a41acd17188595b484"
SESSION = "BAI0X2cAGBHSaplNfNaalwuXE7OjUQlfDKA2qUpogBLwwHe4jjGFYm6dsgIjCAdKI2-4Ucfwdi8Gom1_JjfUpDypOilWx_cp2Ky7anTCuf1iLm2ku6vXwvd6FSa4rw_6FA8ZvRqgGiF5VHdEvXr-GMvTLuZXeAAiKTfFbg<HIDDEN_DUE_TO_LENGTH>"
BOT_TOKEN = "8524748895:AAEBw7opAvIB-PMGaVdjZ-0u1XTbFjAO8DU"

app = Client("user_acc", api_id=API_ID, api_hash=API_HASH, session_string=SESSION)
bot = Client("music_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
call_py = PyTgCalls(app)

ydl_opts = {'format': 'bestaudio/best', 'quiet': True, 'noplaylist': True, 'default_search': 'ytsearch'}

@bot.on_message(filters.command("play") & filters.group)
async def play_audio(client, message):
    query = " ".join(message.command[1:])
    if not query: return await message.reply("Qor heesta!")
    m = await message.reply(f"🔎 Raadinayaa: {query}")
    try:
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(query, download=False)['entries'][0]
            url = info['url']
        await call_py.join_group_call(message.chat.id, AudioPiped(url))
        await m.edit(f"🎶 Hadda waxaa socota: {info['title']}")
    except Exception as e: await m.edit(f"❌ Error: {e}")

@bot.on_message(filters.command("stop") & filters.group)
async def stop_audio(client, message):
    try:
        await call_py.leave_group_call(message.chat.id)
        await message.reply("⏹ Waa la joojiyay.")
    except: pass

async def main():
    await app.start()
    await bot.start()
    await call_py.start()
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
    
