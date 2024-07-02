import discord


class Weee(discord.Cog):

    @discord.Cog.listener()
    async def on_ready(self):
        print(f'\t - {self.__class__.__name__} Cog Loaded')

    @discord.slash_command()
    async def weee(self, ctx: discord.ApplicationContext):
        await ctx.interaction.response.send_message('wooo')

def setup(bot: discord.Bot):
    bot.add_cog(Weee(bot))