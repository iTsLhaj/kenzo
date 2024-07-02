import discord


class Interrupt(discord.Cog):

    @discord.Cog.listener()
    async def on_ready(self):
        print(f'\t - {self.__class__.__name__} Cog Loaded')

    @discord.slash_command()
    async def interrupt(self,
                        ctx: discord.ApplicationContext,
                        user: discord.Option(discord.Member),
                        message: discord.Option(str)):

        dm_channel: discord.DMChannel
        if not user.dm_channel:
            await user.create_dm()

        dm_channel = user.dm_channel
        await dm_channel.send(message)
        await ctx.interaction.response.send_message('Interrupted', ephemeral=True)

def setup(bot: discord.Bot):
    bot.add_cog(Interrupt(bot))