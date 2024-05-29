from telethon import TelegramClient
from telethon.tl import functions
from icecream import ic
from telethon.tl.functions.users import GetFullUserRequest

from database.models.AlchemyCore import AlchemyCore
from database.models.User import User


class ChannelParser:
    def __init__(self, channel_id: any, client: TelegramClient, database: AlchemyCore):
        self.channel_id = channel_id
        self.client = client
        self.db = database


    async def get_channel_pinned_group(self):
        print("Getting channel pinned group")
        channel = await self.client.get_entity(self.channel_id)
        # Get the discussion group associated with the channel
        full_channel = await self.client(functions.channels.GetFullChannelRequest(channel=channel))
        discussion_group_id = full_channel.full_chat.linked_chat_id
        if discussion_group_id:
            discussion_group = await self.client.get_entity(discussion_group_id)

            # Fetch the last 10 messages from the discussion group
            messages = await self.client.get_messages(discussion_group, limit=100)

            for message in messages:

                try:
                    user = await self.client.get_entity(message.sender_id)
                    user_bio = (await self.client(functions.users.GetFullUserRequest(id=user))).full_user.about
                    await self.db.create_user(User(bio=user_bio, userid=user.id, firstname=user.first_name))
                    print(f"Message ID: {message.id} | Sender: {user.id} | User Bio: {user_bio} | Message: {message.text} |  fist name: {user.first_name}")


                except Exception as ex:
                    print(ex)
                    pass


        else:
            print("No discussion group linked to this channel.")
