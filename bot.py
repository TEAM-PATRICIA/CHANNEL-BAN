from config import Config
from pyrogram import Client, idle
from pyrogram.raw.types import UpdateGroupCallParticipants, PeerChannel
from pyrogram.raw.functions.channels import EditBanned
from pyrogram.raw.types import InputPeerChannel, InputChannel, ChatBannedRights, InputGroupCall
from pyrogram.raw.functions.phone import EditGroupCallParticipant

chat=Config.CHAT
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
                    await client.EditGroupCallParticipant(call=update.call, participant=x.peer.channel_id, muted=True)
                    await client.kick_chat_member("DecodeSupport", x.peer.channel_id)
                    await client.send_message(chat, f"Successfully Banned str(x.peer.channel_id)")
                    await client.send_message(chat, f"{e} \n\n{x.peer}")
bot.start() 
idle() 
