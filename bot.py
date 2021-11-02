from config import Config
import telegram
from pyrogram import Client, idle
from pyrogram.raw.types import UpdateGroupCallParticipants
from pyrogram.raw.types import UpdateGroupCallParticipants, PeerChannel
from pyrogram.raw.functions.channels import EditBanned
from pyrogram.raw.types import InputPeerChannel, InputChannel, ChatBannedRights, InputGroupCall

api_id=Config.API_ID
api_hash=Config.API_HASH
session_name=Config.STRING_SESSION
bot = Client(session_name, api_id, api_hash)


@bot.on_raw_update()
async def hemheupdet(client, update, users, chats):
    banchat = await client.resolve_peer("DecodeSupport")
    if isinstance(update, UpdateGroupCallParticipants):
        for x in update.participants:
            if isinstance(x.peer, PeerChannel):
                try:
                    hehe = await client.resolve_peer(int(str(-100) + str(x.peer.channel_id)))
                    await client.send(EditBanned(channel=banchat, participant=hehe, banned_rights=ChatBannedRights(until_date=0,
                                view_messages=True,
                                send_messages=True,
                                send_media=True,
                                send_stickers=True,
                                send_gifs=True,
                                send_games=True,
                                send_inline=True,
                                embed_links=True)))
                    await client.send_message(banchat, f"Successfully Banned {int(str(-100) + str(x.peer.channel_id))}")

                except Exception as e:
                    await client.send_message(banchat, f"{e} \n\n")

bot.start()
print("Bot Is Started!")
idle()
