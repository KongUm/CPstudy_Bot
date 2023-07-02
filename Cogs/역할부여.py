import discord
from discord.ext import commands
import datetime
import utils
from common import const


class 역할부여(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    class change_role_button(discord.ui.Button):
        def __init__(self, label: str, emoji: str, style: discord.ButtonStyle, role_id: int, no_duplicate_role_ids: list = []):
            super().__init__(label=label, emoji=emoji, style=style)
            self.role_id = role_id
            self.no_duplicate_role_ids = no_duplicate_role_ids

        async def callback(self, interaction: discord.Interaction):
            role = interaction.user.get_role(self.role_id)
            # 이미 역할을 가지고 있으면
            if role:
                await interaction.user.remove_roles(role)
                return await interaction.response.send_message(f"{interaction.user.mention} `{role.name}` 역할이 삭제되었습니다!", ephemeral=True)
            # 중복 역할 제거
            remove_roles = [
                i for i in interaction.user.roles if i.id in self.no_duplicate_role_ids]
            for i in remove_roles:
                await interaction.user.remove_roles(await utils.get_role(interaction.guild, i))
            # 역할을 가지고 있지 않으면
            role = await utils.get_role_by_guild(interaction.guild, self.role_id)
            await interaction.user.add_roles(role)

            await interaction.response.send_message(f"{interaction.user.mention} `{role.name}` 역할이 추가되었습니다!", ephemeral=True)

    @commands.Cog.listener()
    async def on_ready(self):
        # 역할 부여 채널
        역할부여채널 = await utils.get_channel_by_id(self.bot, const.역할부여_채널_ID)
        await 역할부여채널.purge(limit=100)

        for data in const.역할목록.values():
            embed = discord.Embed(
                title=data['embed']['title'],
                description=data['embed']['description'],
                color=data['embed']['color']
            )

            view = discord.ui.View(timeout=None)

            for button_data in data['buttons']:
                view.add_item(self.change_role_button(
                    label=button_data['label'],
                    emoji=button_data['emoji'],
                    style=discord.ButtonStyle.primary,
                    role_id=button_data['role_id'],
                    no_duplicate_role_ids=[]
                ))

            await 역할부여채널.send(embed=embed, view=view)


async def setup(bot):
    await bot.add_cog(역할부여(bot))
