import os
import discord
import asyncio


class Kick(discord.Cog):

    @discord.Cog.listener()
    async def on_ready(self):
        print(f'\t - {self.__class__.__name__} Cog Loaded')

    @discord.slash_command()
    async def kick(self,
                   ctx: discord.ApplicationContext,
                   member: discord.Option(discord.Member),
                   *, reason: discord.Option(str, required=False)) -> None:

        tarnished: discord.Member | discord.User = member
        voice_channel = tarnished.voice

        if not voice_channel:

            await ctx.response.send_message(
                f"{tarnished.mention} Can you please get into a voice channel?")
        else:
            voice_channel = voice_channel.channel
            voice: discord.VoiceProtocol = await voice_channel.connect()
            if tarnished.guild_permissions.administrator:

                source = discord.FFmpegPCMAudio(source=os.getenv("BOT_COWARD_AUDIO"))

                await ctx.response.send_message(
                    f"Can't kick an administrator. You mf!")

                voice.play(source)
                while voice.is_playing():
                    await asyncio.sleep(.1)
                await voice.disconnect()

            else:

                source = discord.FFmpegPCMAudio(source=os.getenv("BOT_KICK_AUDIO"))

                voice.play(source)
                while voice.is_playing():
                    await asyncio.sleep(.1)
                await voice.disconnect()

                if reason:
                    await tarnished.kick(reason=reason)
                else:
                    await tarnished.kick(reason=">///<")

def setup(bot: discord.Bot):
    bot.add_cog(Kick(bot))