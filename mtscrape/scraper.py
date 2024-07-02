import requests

from bs4 import BeautifulSoup, element
from typing import List, Dict


class MTCScraper(object):

    def __init__(self):
        pass

    def scrape_vcards(self) -> List[Dict[str, str]]:
        '''
        Scrape the Valorant Cards page
        :return: vards data in a format of { title, region, link }
        '''

        valorant_cards: List = []
        with requests.Session() as S:

            r = S.get(
                url="/".join([
                    "https://www.mtcgame.com",
                    "search?q=Valorant"
                ])
            )
            card_class_selector = "flex flex-col bg-mtc-deep-dark shadow-sm rounded-lg overflow-hidden relative"
            soup = BeautifulSoup(r.text, 'lxml')
            cards: List[element.Tag] = soup.find_all(
                "a", { "class": card_class_selector }
            )
            for card in cards:
                if "Valorant Points (VP)" in card.get_text():
                    link = r.url.split('/')
                    link.pop()
                    link.append(card["href"])
                    valorant_cards.append({
                        "title": card.get_text().rstrip().strip(),
                        "region": card.get_text().replace(
                            "Valorant Points (VP) Gift Card ", ""
                        ).replace(" Store", "").rstrip().strip(),
                        "link": "/".join(link).rstrip().strip()
                    })

            r.close()

        return valorant_cards

    def scrape_prods(self, link: str) -> List[Dict[str, str]]:
        '''
        scrape valorant cards from link !
        :param link: link to the products to scrape !
        :return: scraped data in a format of { title, url_image, price }
        '''

        vp_gift_cards: List = []
        with requests.Session() as S:

            r = S.get(url=link)
            soup = BeautifulSoup(r.text, 'lxml')

            cards_div: element.Tag = soup.find(
                "div", { "class": "bg-mtc-deep-dark rounded-xl md:p-3 w-full p-2" })
            cards = cards_div.find_all("div", { "class": "flex items-center mt-5 bg-mtc-dark rounded-lg overflow-hidden" })
            for card in cards:
                vp_gift_cards.append({
                    "url_image": "".join(
                        ["https://www.mtcgame.com",
                         card.find_next("img")["src"]]
                    ),
                    "title": card.find_next("strong").get_text(),
                    "price": card.find_next("span", {
                        "class": "text-md font-bold text-yellow-400"
                    }).get_text()
                })
            r.close()

        return vp_gift_cards

    def get_regions(self) -> List[str]:
        return [card["region"] for card in self.scrape_vcards()]