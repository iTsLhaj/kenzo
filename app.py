import asyncio
import discord
import dotenv
import random
import os


class Bot(discord.Bot):

    CURSED_USER_IDS = [
        "651391341229506570", # bigfain hh
        "316908854854156290" # snoopi hh
    ]
    CHARMING = [
        "adak L7mar",
        "adak Lklb",
        "adak tarnished",
        "adak Lmaidenless",
        "?",
        "hania ? hh",
        "l3ezzi jab reb7a weee we",
        "ahya hh",
        "shi nas khshom itbanaw !",
        "wa noob wa lbot !",
        "3atiha ghi La97bonixage",
        "blyat",
        "A3tilo\npassilo\nmarkiloo\nwili ya wili\njabha f lfilee\nwili ya wili\njabha f lfilee\naaa 3tilo \nZalalig 3tilo\nA3tilopassilomarkilo\n"
]
    NEXT_ASSAULT = 240

    async def on_ready(self):

        print(f' - Logged in as {self.user.name}')
        print(' - Loading Cogs !')

        await self.wait_until_ready()
        await self.change_presence(activity=discord.Streaming(
            name="Beyond Journey's End",
            url="https://www.youtube.com/watch?v=7jSYWndhDLE"
        ))

        first = True
        while (1):
            role: discord.Role = self.get_guild(1204551376097509396).get_role(1223040077811286067)
            user: discord.User = await self.fetch_user(int(random.choice(self.CURSED_USER_IDS)))
            channel = await self.fetch_channel(1209890649520873502)  # channel <random>
            if first:
                await channel.send(f"{user.mention} {self.CHARMING[-1]}")
                first = False
            else:
                await channel.send(f"{user.mention} {random.choice(self.CHARMING)}")
            await asyncio.sleep(self.NEXT_ASSAULT)
            self.NEXT_ASSAULT += 1

    async def on_connect(self):

        print('\nConnected to Discord!'
              f'\nApplication Id: {str(self.application_id)}\n')
        await self.sync_commands()

def load_cogs(client: discord.Bot) -> None:

    for cog_file in os.listdir('./cogs'):
        if cog_file.endswith('.py'):
            client.load_extension(f'cogs.{cog_file[:-3]}')


if __name__ == '__main__':

    dotenv.load_dotenv()
    bot = Bot()
    load_cogs(bot)
    bot.run(os.getenv('CLIENT_TOKEN'))
