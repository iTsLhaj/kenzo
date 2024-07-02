import discord

from mtscrape.embeder import EmbedVCards
from mtscrape.types.region import Region


class Mtc(discord.Cog):

    @discord.Cog.listener()
    async def on_ready(self):
        print(f'\t - {self.__class__.__name__} Cog Loaded')

    # @discord.slash_command(name='mtc', description='scrape valorant vp gift cards prices from mtcgame.com !', help='/mtc region:[Turkey, Euro, North America, Brazil, Mena, India]')
    # , region: discord.Option(str, choices=['Turkey', 'Euro', 'North America', 'Brazil', 'Mena', 'India'])
    @discord.slash_command()
    async def mtc(self,
                  ctx: discord.ApplicationContext,
                  region: discord.Option(
                      str,
                      choices=['Turkey', 'Euro', 'North America', 'Brazil', 'Mena', 'India'])):

        embed = EmbedVCards()
        region_ = Region(region=str(region).title())
        for card in embed.scrape_vcards():
            if card["region"].title() == region_.region:
                region_.link = card["link"]
                break
        if region_.link is None:
            await ctx.interaction.response.send_response("No such region !")
            return None
        embeds_ = embed.create_embeded_vcards(region=region_, author=ctx.author)
        for e in embeds_:
            await ctx.send(embed=e)

def setup(bot: discord.Bot):
    bot.add_cog(Mtc(bot))