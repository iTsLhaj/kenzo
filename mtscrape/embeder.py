import discord

from typing import List, Dict
from .scraper import MTCScraper
from .types.region import Region


class EmbedVCards(MTCScraper):

    def __init__(self):
        super(EmbedVCards)

    def create_embeded_vcards(self, region: Region, author: discord.Member | discord.User) -> List[discord.Embed] | None:

        embedcs: List = []
        cards: List[Dict[str, str]] = self.scrape_prods(
            link=region.link if region.link else region.link)
        for gift_card in cards:
            dembed = discord.Embed(
                title=gift_card["title"],
                description=f"valorant points card ({region.region}) server".title(),
                color=discord.Color.nitro_pink())
            dembed.add_field(name="price", value=gift_card["price"])
            dembed.set_image(url=gift_card["url_image"])
            dembed.set_author(
                name=author.name,
                icon_url=author.avatar.url
            )
            embedcs.append(dembed)

        return embedcs