import discord
from discord.ext import commands


class Disturb(discord.Cog):

    @discord.Cog.listener()
    async def on_ready(self):
        print(f'\t - {self.__class__.__name__} Cog Loaded')

    @discord.slash_command()
    @commands.is_owner()
    async def disturb(self,
                      ctx: discord.ApplicationContext,
                      user: discord.Option(discord.Member),
                      message: discord.Option(str)):

        await ctx.send(f"{user.mention} {message}")
        await ctx.interaction.response.send_message("ez hh", ephemeral=True)

def setup(bot: discord.Bot):
    bot.add_cog(Disturb(bot))