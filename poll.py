from discord.ext import commands
import discord
from discord.ext.commands import Bot
import asyncio

def to_emoji(c):
    base = 0x1f1e6
    return chr(base + c)

class Poll:
        """Poll voting system."""

        def __init__(self, client):
            self.client = client

        @commands.command(brief = "Creates a Poll",
                          description = "This makes a poll for you and assigns the corresponding letters for you\n"
                                        'To use this feature, put "" around the question and options\n'
                                        'Leave a space in between!',
                          pass_context = True)
        async def poll(self, ctx, *questions_and_choices: str):

            if len(questions_and_choices) < 3:
                return await self.client.say('Need at least 1 question with 2 choices.')
            elif len(questions_and_choices) > 21:
                return await self.client.say('You can only have up to 20 choices.')


            question = questions_and_choices[0]
            choices = [(to_emoji(e), v) for e, v in enumerate(questions_and_choices[1:])]

            try:
                await ctx.message.delete()
            except:
                pass

            body = "\n".join(f"{key}: {c}" for key, c in choices)
            poll = await self.client.say(f'{ctx.message.author.mention} asks: {question}\n\n{body}')
            for emoji, _ in choices:
                await self.client.add_reaction(emoji)


def setup(client):
    client.add_cog(Poll(client))