import discord
from discord.ext import commands
import datetime
import utils
from common import const


class 입장메시지(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        embed = discord.Embed(
            title=f"",
            description=f"""\
                {member.mention}님, **{member.guild.name}**에 오신 것을 환영합니다!

                <#{const.공지사항_채널_ID}>을 읽어주시고, [백준 그룹](https://www.acmicpc.net/group/16677)과 [코드포스 그룹](https://codeforces.com/group/G3svECNIkW/contests)에 가입해주세요.
                <#{const.역할부여_채널_ID}>에서 역할을 받아주세요.
                """,
            color=0xe9c2c0,
            timestamp=datetime.datetime.now()
        )
        embed.set_author(
            name=member.name,
            icon_url=member.display_avatar
        )

        channel = await utils.get_channel_by_id(self.bot, const.입장메시지_채널_ID)

        await channel.send(
            content=f"{member.mention}",
            embed=embed
        )


async def setup(bot):
    await bot.add_cog(입장메시지(bot))
