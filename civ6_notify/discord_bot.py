import asyncio
import os
from discord.ext.commands import Bot, command


class CivDiscordNotifyBotClient(Bot):
    def __init__(self, loop):
        super().__init__(
            "$",
            description="Sends notifications for Civ 6 Play-by-Cloud games",
            loop=loop,
        )

    async def on_ready(self):
        print(f"Logged on as {self.user}")
        print(f"Guilds: {self.guilds}")

    # async def on_message(self, message: discord.Message):
    #     if message.author.id == self.user.id:
    #         return
    #     print(f"Received message {message.content}")
    #     print(f"Mentions: {message.mentions}")
    #     sender_id = message.author.id
    #     sender_channel = message.channel
    #     response = f"<@{sender_id}> did you say something?"
    #     await sender_channel.send(response)


@command(name="civ6")
async def civ6(ctx, arg):
    print(f"Adding new game...{(ctx, arg)}")


def add_commands_to_bot(bot: Bot):
    bot.add_command(civ6)


SERVER = os.getenv("CIV6_NOTIFY_DISCORD_SERVER")


async def start_client(loop: asyncio.AbstractEventLoop = None):
    if loop:
        client = CivDiscordNotifyBotClient(loop=loop)
    else:
        loop = asyncio.get_event_loop()
    token = os.getenv("CIV6_NOTIFY_DISCORD_TOKEN")
    print("Connecting...")
    loop.create_task(client.start(token))
