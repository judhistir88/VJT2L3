# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

import os
import re
import sys
import json
import time
import asyncio
import logging
import requests
import subprocess

import core as helper
from utils import progress_bar
from vars import API_ID, API_HASH, BOT_TOKEN
from aiohttp import ClientSession
from pyromod import listen
from subprocess import getstatusoutput

from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import FloodWait
from pyrogram.errors.exceptions.bad_request_400 import StickerEmojiInvalid
from pyrogram.types.messages_and_media import message

# Configure logging
logging.basicConfig(filename='bot.log', level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Example of logging
logging.info("Bot started")

bot = Client(
    "bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN)

OWNER_ID = 2094369069  # Replace with your Telegram user ID

@bot.on_message(filters.command(["start"]))
async def start(bot: Client, m: Message):
    await m.reply_text(f"<b>Hello {m.from_user.mention} 👋\n\n I Am A Bot For Download Links From Your **.TXT** File And Then Upload That File On Telegram So Basically If You Want To Use Me First Send Me /upload Command And Then Follow Few Steps..\n\nUse /stop to stop any ongoing task.</b>")
    logging.info(f"Start command received from user: {m.from_user.id}")

@bot.on_message(filters.command("stop"))
async def restart_handler(_, m):
    await m.reply_text("**Stopped**🚦", True)
    logging.info(f"Stop command received from user: {m.from_user.id}")
    os.execl(sys.executable, sys.executable, *sys.argv)

@bot.on_message(filters.command(["upload"]))
async def upload(bot: Client, m: Message):
    editable = await m.reply_text('𝕤ᴇɴᴅ ᴛxᴛ ғɪʟᴇ ⚡️')
    input: Message = await bot.listen(editable.chat.id)
    x = await input.download()
    await input.delete(True)

    path = f"./downloads/{m.chat.id}"

    try:
       with open(x, "r") as f:
           content = f.read()
       content = content.split("\n")
       links = []
       for i in content:
           links.append(i.split("://", 1))
       os.remove(x)
    except:
           await m.reply_text("**Invalid file input.**")
           os.remove(x)
           logging.error("Invalid file input.")
           return
   
    await editable.edit(f"**𝕋ᴏᴛᴀʟ ʟɪɴᴋ𝕤 ғᴏᴜɴᴅ ᴀʀᴇ🔗🔗** **{len(links)}**\n\n**𝕊ᴇɴᴅ 𝔽ʀᴏᴍ ᴡʜᴇʀᴇ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ɪɴɪᴛɪᴀʟ ɪ𝕤** **1**")
    input0: Message = await bot.listen(editable.chat.id)
    raw_text = input0.text
    await input0.delete(True)

    await editable.edit("**Now Please Send Me Your Batch Name**")
    input1: Message = await bot.listen(editable.chat.id)
    raw_text0 = input1.text
    await input1.delete(True)
    
    # Create inline keyboard for resolution selection
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("144p", callback_data="144")],
        [InlineKeyboardButton("240p", callback_data="240")],
        [InlineKeyboardButton("360p", callback_data="360")],
        [InlineKeyboardButton("480p", callback_data="480")],
        [InlineKeyboardButton("720p", callback_data="720")],
        [InlineKeyboardButton("1080p", callback_data="1080")]
    ])
    await editable.edit("**𝔼ɴᴛᴇʀ ʀᴇ𝕤ᴏʟᴜᴛɪᴏɴ📸**\nPlease choose quality:", reply_markup=keyboard)

# Add a handler to process the resolution selection
@bot.on_callback_query()
async def callback_query_handler(bot: Client, query):
    data = query.data
    resolutions = ["144", "240", "360", "480", "720", "1080"]
    if data in resolutions:
        res_map = {
            "144": "256x144",
            "240": "426x240",
            "360": "640x360",
            "480": "854x480",
            "720": "1280x720",
            "1080": "1920x1080"
        }
        res = res_map[data]
        await query.message.edit_text(f"Selected resolution: {res}")
        
        # Proceed with the remaining steps after resolution selection
        await query.message.edit_text("Now Enter A Caption to add caption on your uploaded file")
        input3: Message = await bot.listen(query.message.chat.id)
        raw_text3 = input3.text
        await input3.delete(True)
        highlighter  = f"️ ⁪⁬⁮⁮⁮"
        if raw_text3 == 'Robin':
            MR = highlighter 
        else:
            MR = raw_text3

        await query.message.edit_text("Now send the Thumb url/nEg » https://graph.org/file/ce1723991756e48c35aa1.jpg \n Or if don't want thumbnail send = no")
        input6: Message = await bot.listen(query.message.chat.id)
        raw_text6 = input6.text
        await input6.delete(True)
        await query.message.delete()

        thumb = input6.text
        if thumb.startswith("http://") or thumb.startswith("https://"):
            getstatusoutput(f"wget '{thumb}' -O 'thumb.jpg'")
            thumb = "thumb.jpg"
        else:
            thumb == "no"

        if len(links) == 1:
            count = 1
        else:
            count = int(raw_text)

        try:
            for i in range(count - 1, len(links)):

                V = links[i][1].replace("file/d/","uc?export=download&id=").replace("www.youtube-nocookie.com/embed", "youtu.be").replace("?modestbranding=1", "").replace("/view?usp=sharing","") # .replace("mpd","m3u8")
                url = "https://" + V

                if "visionias" in url:
                    async with ClientSession() as session:
                        async with session.get(url, headers={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'Accept-Language': 'en-US,en;q=0.9', 'Cache-Control': 'no-cache', 'Connection': 'keep-alive', 'Pragma': 'no-cache', 'Referer': 'http://www.visionias.in/', 'Sec-Fetch-Dest': 'iframe', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-Site': 'cross-site', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Linux; Android 12; RMX2121) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36', 'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform': '"Android"',}) as resp:
                            text = await resp.text()
                            url = re.search(r"(https://.*?playlist.m3u8.*?)\"", text).group(1)

                elif 'videos.classplusapp' in url:
                    url = requests.get(f'https://api.classplusapp.com/cams/uploader/video/jw-signed-url?url={url}', headers={'x-access-token': 'eyJhbGciOiJIUzM4NCIsInR5cCI6IkpXVCJ9.eyJpZCI6MzgzNjkyMTIsIm9yZ0lkIjoyNjA1LCJ0eXBlIjoxLCJtb2JpbGUiOiI5MTcwODI3NzQyODkiLCJuYW1lIjoiQWNlIiwiZW1haWwiOm51bGwsImlzRmlyc3RMb2dpbiI6dHJ1ZSwiZGVmYXVsdExhbmd1YWxlIjpudWxsLCJjb3VudHJ5Q29kZSI6IklOIiwiaXNJbnRlcm5hdGlvbmFsIjowLCJpYXQiOjE2NDMyODE4NzcsImV4cCI6MTY0Mzg4NjY3N30.hM33P2ai6ivdzxPPfm01LAd4JWv-vnrSxGXqvCirCSpUfhhofpeqyeHPxtstXwe0'}).json()['url']

                elif '/master.mpd' in url:
                    id =  url.split("/")[-2]
                    url =  "https://d26g5bnklkwsh4.cloudfront.net/" + id + "/master.m3u8"

                name1 = links[i][0].replace("\t", "").replace(":", "").replace("/", "").replace("+", "").replace("#", "").replace("|", "").replace("@", "").replace("*", "").replace(".", "").replace("https", "").replace("http", "").strip()
                name = f'{str(count).zfill(3)}) {name1[:60]}'

                if "youtu" in url:
                    ytf = f"b[height<={res}][ext=mp4]/bv[height<={res}][ext=mp4]+ba[ext=m4a]/b[ext=mp4]"
                else:
                    ytf = f"b[height<={res}]/bv[height<={res}]+ba/b/bv+ba"

                if "jw-prod" in url:
                    cmd = f'yt-dlp -o "{name}.mp4" "{url}"'
                else:
                    cmd = f'yt-dlp -f "{ytf}" "{url}" -o "{name}.mp4"'

                try:  
                    cc = f'**[📽️] Vid_ID:** {str(count).zfill(3)}.** {𝗻𝗮𝗺𝗲𝟭}{MR}.mkv\n**𝔹ᴀᴛᴄʜ** » **{raw_text0}**'
                    cc1 = f'**[📁] Pdf_ID:** {str(count).zfill(3)}. {𝗻𝗮𝗺𝗲𝟭}{MR}.pdf \n**𝔹ᴀᴛᴄʜ** » **{raw_text0}**'
                    if "drive" in url:
                        try:
                            ka = await helper.download(url, name)
                            copy = await bot.send_document(chat_id=query.message.chat.id, document=ka, caption=cc1)
                            count += 1
                            os.remove(ka)
                            time.sleep(1)
                        except FloodWait as e:
                            await query.message.reply_text(str(e))
                            time.sleep(e.x)
                            continue
                    
                    elif ".pdf" in url:
                        try:
                            cmd = f'yt-dlp -o "{name}.pdf" "{url}"'
                            download_cmd = f"{cmd} -R 25 --fragment-retries 25"
                            os.system(download_cmd)
                            copy = await bot.send_document(chat_id=query.message.chat.id, document=f'{name}.pdf', caption=cc1)
                            count += 1
                            os.remove(f'{name}.pdf')
                        except FloodWait as e:
                            await query.message.reply_text(str(e))
                            time.sleep(e.x)
                            continue
                    else:
                        Show = f"**⥥ 🄳🄾🅆🄽🄻🄾🄰🄳🄸🄽🄶⬇️⬇️... »**\n\n**📝Name »** `{name}\n❄Quality » {res}`\n\n**🔗URL »** `{url}`"
                        prog = await query.message.reply_text(Show)
                        res_file = await helper.download_video(url, cmd, name)
                        filename = res_file
                        await prog.delete(True)
                        await helper.send_vid(bot, query.message, cc, filename, thumb, name, prog)
                        count += 1
                        time.sleep(1)

                except Exception as e:
                    await query.message.reply_text(
                        f"**downloading Interupted **\n{str(e)}\n**Name** » {name}\n**Link** » `{url}`"
                    )
                    logging.error(f"Downloading interrupted: {str(e)}")
                    continue

        except Exception as e:
            await query.message.reply_text(e)
            logging.error(f"Error during upload: {str(e)}")
        await query.message.reply_text("**𝔻ᴏɴᴇ 𝔹ᴏ𝕤𝕤😎**")
        logging.info("Upload process completed successfully")

@bot.on_message(filters.command(["log"]) & filters.user(OWNER_ID))
async def send_logs(bot: Client, m: Message):
    try:
        with open('bot.log', 'r') as f:
            lines = f.readlines()
            last_1000_lines = lines[-1000:]
        
        # Save the last 1000 lines to a temporary file
        with open('last_1000_logs.txt', 'w') as f:
            f.writelines(last_1000_lines)
        
        # Send the log file to the owner/admin
        await bot.send_document(chat_id=m.chat.id, document='last_1000_logs.txt', caption="Here are the last 1000 lines of the log file.")
        
        # Clean up the temporary file
        os.remove('last_1000_logs.txt')
    
    except Exception as e:
        await m.reply_text(f"An error occurred: {str(e)}")
        logging.error(f"Error sending logs: {str(e)}")

bot.run()
