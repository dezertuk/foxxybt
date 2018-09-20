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
    
    def is_num(self, s):
        try:
            int(s)
            return True
        except ValueError:
            return False

    # Roll die and get a random number between a and b (inclusive) adding/subtracting the modifier
    # Parameters: a [low number], b [high number], modifier [amount to add/subtract to total]
    # threshold [number that result needs to match or exceed to count as a success]
    # Returns: str
    def roll_basic(self, a, b, modifier, threshold):
        results = ""
        base = randint(int(a), int(b))
        if (base + modifier) >= threshold:
            if modifier != 0:
                if modifier > 0:
                    results += "***Success***: {}+{} [{}] meets or beats the {} threshold.".format(base, modifier,
                                                                                                   (base + modifier),
                                                                                                   threshold)
                else:
                    results += "***Success***: {}{} [{}] does not meet the {} threshold.".format(base, modifier,
                                                                                                 (base + modifier),
                                                                                                 threshold)
            else:
                results += "***Success***: {}".format(base)
        else:
            if modifier != 0:
                if modifier > 0:
                    results += "***Failure***: {}+{} [{}]".format(base, modifier, (base + modifier))
                else:
                    results += "***Failure***: {}{} [{}]".format(base, modifier, (base + modifier))
            else:
                results += "***Failure***: {}".format(base)
        return results

    # Rolls a set of die and returns either number of hits or the total amount
    # Parameters: num_of_dice [Number of dice to roll], dice_type[die type (e.g. d8, d6),
    # hit [number that must be exceeded to count as a success], modifier [amount to add to/subtract from total],
    # threshold [number of successes needed to be a win]
    # Returns: String with results
    def roll_hit(self, num_of_dice, dice_type, hit, modifier, threshold):
        results = ""
        total = 0
        for x in range(0, int(num_of_dice)):
            y = randint(1, int(dice_type))
            if (int(hit) > 0):
                if (y >= int(hit)):
                    results += "**{}** ".format(y)
                    total += 1
                else:
                    results += "{} ".format(y)
            else:
                results += "{} ".format(y)
                total += y
        total += int(modifier)
        if modifier != 0:
            if modifier > 0:
                results += "+{} = {}".format(modifier, total)
            else:
                results += "{} = {}".format(modifier, total)
        else:
            results += "= {}".format(total)
        if threshold != 0:
            if total >= threshold:
                results += " meets or beats the {} threshold. ***Success***".format(threshold)
            else:
                results += " does not meet the {} threshold. ***Failure***".format(threshold)
        return results

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
        
    @commands.command(pass_context=True,
                      description='Rolls dice.\nExamples:\n100  Rolls 1-100.\n50-100  Rolls 50-100.\n3d6  Rolls 3 d6 dice and returns total.\nModifiers:\n! Hit success. 3d6!5 Counts number of rolls that are greater than 5.\nmod: Modifier. 3d6mod3 or 3d6mod-3. Adds 3 to the result.\n> Threshold. 100>30 returns success if roll is greater than or equal to 30.\n\nFormatting:\nMust be done in order.\nSingle die roll: 1-100mod2>30\nMultiple: 5d6!4mod-2>2')
    @asyncio.coroutine
    def roll(self, ctx, roll : str):
        a, b, modifier, hit, num_of_dice, threshold, dice_type = 0, 0, 0, 0, 0, 0, 0
        # author: Writer of discord message
        author = ctx.message.author
        if (roll.find('>') != -1):
            roll, threshold = roll.split('>')
        if (roll.find('mod') != -1):
            roll, modifier = roll.split('mod')
        if (roll.find('!') != -1):
            roll, hit = roll.split('!')
        if (roll.find('d') != -1):
            num_of_dice, dice_type = roll.split('d')
        elif (roll.find('-') != -1):
            a, b = roll.split('-')
        else:
            a = 1
            b = roll
        #Validate data
        try:
            if (modifier != 0):
                if (self.is_num(modifier) is False):
                    raise ValueError("Modifier value format error. Proper usage 1d4+1")
                    return
                else:
                    modifier = int(modifier)
            if (hit != 0):
                if (self.is_num(hit) is False):
                    raise ValueError("Hit value format error. Proper usage 3d6!5")
                    return
                else:
                    hit = int(hit)
            if (num_of_dice != 0):
                if (self.is_num(num_of_dice) is False):
                    raise ValueError("Number of dice format error. Proper usage 3d6")
                    return
                else:
                    num_of_dice = int(num_of_dice)
            if (num_of_dice > 200):
                raise ValueError("Too many dice. Please limit to 200 or less.")
                return
            if (dice_type != 0):
                if (self.is_num(dice_type) is False):
                    raise ValueError("Dice type format error. Proper usage 3d6")
                    return
                else:
                    dice_type = int(dice_type)
            if (a != 0):
                if (self.is_num(a) is False):
                    raise ValueError("Error: Minimum must be a number. Proper usage 1-50.")
                    return
                else:
                    a = int(a)
            if (b != 0):
                if (self.is_num(b) is False):
                    raise ValueError("Error: Maximum must be a number. Proper usage 1-50 or 50.")
                    return
                else:
                    b = int(b)
            if (threshold != 0):
                if (self.is_num(threshold) is False):
                    raise ValueError("Error: Threshold must be a number. Proper usage 1-100>30")
                    return
                else:
                    threshold = int(threshold)
            if (dice_type != 0 and hit != 0):
                if (hit > dice_type):
                    raise ValueError("Error: Hit value cannot be greater than dice type")
                    return
                elif (dice_type < 0):
                    raise ValueError("Dice type cannot be a negative number.")
                    return
                elif (num_of_dice < 0):
                    raise ValueError("Number of dice cannot be a negative number.")
                    return
            if a != 0 and b != 0:
                yield from self.client.say("{} rolls {}-{}. Result: {}".format(author, a, b, self.roll_basic(a, b, modifier, threshold)))
            else:
                yield from self.client.say("{} rolls {}d{}. Results: {}".format(author, num_of_dice, dice_type, self.roll_hit(num_of_dice, dice_type, hit, modifier, threshold)))
        except ValueError as err:
            # Display error message to channel
            yield from self.client.say(err)


def setup(client):
    client.add_cog(CoreCommands(client))
