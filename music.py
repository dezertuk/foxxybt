import discord
from discord.ext import commands
from ctypes.util import find_library
from discord import opus

'''
This is the part of the code that is resposible for running the music
'''

class Music:

    players = {}

    def __init__(self, client):
        self.client = client

    @commands.command(name="join",
                      brief="Joins your VC",
                    pass_context=True)
    async def join(self,ctx):
        opus_path = find_library('opus')
        discord.opus.load_opus(opus_path)
        if not opus.is_loaded():
            print('Opus was not loaded')
        else:
            channel = ctx.message.author.voice.voice_channel
            await self.client.join_voice_channel(channel)
            print("Bot joined the voice channel")

    @commands.command(name="check",
                      brief="Used for debugging only",
                    pass_context=True)
    async def check(self, ctx):
        server = ctx.message.server
        if self.client.is_voice_connected(server):
            print("Yes - Voice Client is connected")
        else:
            print("No - Voice Client is not connected")

    @commands.command(name="leave",
                      brief="Leaves your VC",
                    pass_context=True)
    async def leave(self, ctx):
        server = ctx.message.server
        voice_client = self.client.voice_client_in(server)
        if voice_client:
            await voice_client.disconnect()
            print("Bot left the voice channel")
        else:
            print("Bot was not in channel")

    @commands.command(pass_context=True,
                      brief="Plays the YT URL")
    async def play(self, ctx, url):
        server = ctx.message.server
        voice_client = self.client.voice_client_in(server)
        player = await voice_client.create_ytdl_player(url)
        self.players[server.id] = player
        player.start()

    @commands.command(pass_context=True,
                      brief="Pauses the music")
    async def pause(self, ctx):
        id = ctx.message.server.id
        self.players[id].pause()

    @commands.command(pass_context=True,
                      brief="Stops the music")
    async def stop(self, ctx):
        id = ctx.message.server.id
        self.players[id].stop()

    @commands.command(pass_context=True,
                      brief="Resumes the music")
    async def resume(self, ctx):
        id = ctx.message.server.id
        self.players[id].resume()

def setup(client):
    client.add_cog(Music(client))