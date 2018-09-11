import discord
from discord.ext import commands
import random
from random import choice
import datetime
import json
'''
This is the main commands for the bot
'''

class CoreCommands:

    def __init__(self, client):
        self.client = client


    @commands.command(name="hello",
                      brief="Self explanatory",
                      pass_context=True)
    async def greet(self, context):
        await self.client.say("*Hi there* " + context.message.author.mention)

    @commands.command(name = "8ball",
                    description = "This will give you some random answers from a list\n"
                                  "Answers yes or no questions",
                    brief = "Answers Yes/No questions",
                    pass_context = True)
    async def eight_ball(self, context):
        possible_responce = [

            "IDK this is not google",
            "Maybe",
            "Sure",
            "Not a chance",

        ]
        await self.client.say(random.choice(possible_responce) + ", " + context.message.author.mention)

    @commands.command(name = "clear",
                      brief="Cleans up to 20 msgs",
                    pass_context = True)
    async def clear(self, ctx, amount = 10):
        channel = ctx.message.channel
        messages = []
        if ctx.message.author.id == '128190893793476608' or '316164087501553665':
            async for message in self.client.logs_from(channel, limit = int(amount)+ 1):
                messages.append(message)
            await self.client.delete_messages(messages)
            print(amount, "messages have been deleted by: ", ctx.message.author)
            self.client.say("The channel has been nuked by: ", ctx.message.author)
        else:
            await self.client.say("You dont have the launch codes for that puppy, pal...\U0001f92f")

    @commands.command(name = "nukethechannel",
                      brief="Cleans whole channel!",
                    pass_context = True)
    @commands.cooldown(1, 60, commands.BucketType.user)
    async def nukethechannel(self, ctx, amount = 99):
        channel = ctx.message.channel
        messages = []
        if ctx.message.author.id == '128190893793476608'or '316164087501553665':
            async for message in self.client.logs_from(channel, limit = int(amount)+ 1):
                messages.append(message)
            await self.client.delete_messages(messages)
            print(amount, "messages have been cleaned using the nuke by: ", ctx.message.author)
        else:
            await self.client.say("You dont have the launch codes for that puppy, pal...\U0001f92f")

    @commands.command(name="quit",
                      pass_context = True)
    async def bot_quit(self, ctx):
        """Gives Foxxy Chloroform"""
        if ctx.message.author.id == '128190893793476608':
            await self.client.say("Gonna take a nap...\U0001f634")
            await self.client.logout()

            key = str(datetime.datetime.now())
            insert = 'Foxxy has been turned OFF'
            logged = {key: insert}

            data = json.load(open('StartLog.json', 'r'))
            with open('StartLog.json', 'w') as f:
                data['Logs'].update(logged)
                json.dump(data, f, indent=2)
        else:
            await self.client.say("You dont have the launch codes for that puppy, pal...\U0001f92f")


    @commands.command(brief = "Flips a coin... or a user",
                      pass_context=True)
    async def flip(self, ctx, user : discord.Member=None):
        if user != None:
            msg = ""
            if user.id == self.client.user.id:
                user = ctx.message.author
                msg = "Nice try. You think this is funny? How about *this* instead:\n\n"
            char = "abcdefghijklmnopqrstuvwxyz"
            tran = "ɐqɔpǝɟƃɥᴉɾʞlɯuodbɹsʇnʌʍxʎz"
            table = str.maketrans(char, tran)
            name = user.display_name.translate(table)
            char = char.upper()
            tran = "∀qƆpƎℲפHIſʞ˥WNOԀQᴚS┴∩ΛMX⅄Z"
            table = str.maketrans(char, tran)
            name = name.translate(table)
            await self.client.say(msg + "(╯°□°）╯︵ " + name[::-1])
        else:
            await self.client.say("*flips a coin and... " + choice(["HEADS!*", "TAILS!*"]))

    @commands.command(brief="PMs Server invite",
                      pass_context=True)
    async def serverinvite(self, context):
        """Pm's A Invite Code (To The Server) To The User"""
        invite = await self.client.create_invite(context.message.server, max_uses=1, xkcd=True)
        await self.client.send_message(context.message.author, "Your invite URL is {}".format(invite.url))
        await self.client.say("*Check Your Dm's* :wink: ")


def setup(client):
    client.add_cog(CoreCommands(client))
