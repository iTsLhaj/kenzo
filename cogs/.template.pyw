# this python code serves as a template !
# all you have to do is change the class name
# e.g: i wanna make a command called foo
# the class name will be Foo and the command_name will be foo

import discord


class CommandClass(discord.Cog):

    @discord.Cog.listener()
    async def on_ready(self) -> None:
        print(f'\t - {self.__class__.__name__} Cog Loaded')

    @discord.slash_command()
    async def command_name(self, ctx: discord.ApplicationContext) -> None:
        # do something !
        pass

def setup(bot: discord.Bot) -> None:
    bot.add_cog(CommandClass(bot))