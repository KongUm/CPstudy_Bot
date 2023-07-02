import discord
from discord.ext import commands
from common import const


class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix=const.PREFIX,
            intents=discord.Intents.all(),
            sync_command=True,
        )

        self.initial_extension = [
            "Cogs.역할부여",
            "Cogs.입장메시지",
        ]

    async def setup_hook(self):
        for ext in self.initial_extension:
            await self.load_extension(ext)

        await bot.tree.sync()

    async def on_ready(self):
        print(f"DISCORD BOT : {self.user}")
        print(
            f"Discord Version : {discord.__version__}")
        print(f"On ready")


if __name__ == '__main__':
    bot = MyBot()
    bot.run(const.TOKEN)
