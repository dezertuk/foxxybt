import aiohttp
import json
from discord.ext import commands
import discord
from discord.ext.commands import Bot
import time

class Info:

    def __init__(self, client):
        self.client = client

    @commands.command(name = "uinfo",
                      brief="Some info on chosen user",
                    pass_context = True)
    async def uinfo(self, context, user: discord.Member):
        embed = discord.Embed(title="{}'s info".format(user.name), description = "Here's what I could find.", color = 0x00ff00)
        embed.add_field(name = "Name", value=user.name, inline=True)
        embed.add_field(name = "ID", value=user.id, inline=True)
        embed.add_field(name = "Status", value=user.status, inline=True)
        embed.add_field(name = "Highest role", value=user.top_role)
        embed.add_field(name = "Joined", value=user.joined_at)
        embed.set_thumbnail(url = user.avatar_url)
        await self.client.say(embed = embed)

    @commands.command(brief="Current price of bitcoin in$")
    async def bitcoin(self):
        url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
        async with aiohttp.ClientSession() as session:  # Async HTTP request
            raw_response = await session.get(url)
            response = await raw_response.text()
            response = json.loads(response)
            await self.client.say("Bitcoin price is: $" + response['bpi']['USD']['rate'])

    @commands.command(brief = "Displays info about the server",
                      pass_context=True)
    async def serverinfo(self, ctx):

        server = ctx.message.server
        roles = [x.name for x in server.role_hierarchy]
        role_length = len(roles)

        if role_length > 50:  # Just in case there are too many roles...
            roles = roles[:50]
            roles.append('>>>> Displaying[50/%s] Roles' % len(roles))

        roles = ', '.join(roles);
        channelz = len(server.channels);
        time = str(server.created_at);
        time = time.split(' ');
        time = time[0];

        join = discord.Embed(description='%s ' % (str(server)), title='Server Name', colour=0xFFFF);
        join.set_thumbnail(url=server.icon_url);
        join.add_field(name='__Owner__', value=str(server.owner) + '\n' + server.owner.id);
        join.add_field(name='__Server ID__', value=str(server.id))
        join.add_field(name='__Member Count__', value=str(server.member_count));
        join.add_field(name='__Text/Voice Channels__', value=str(channelz));
        join.add_field(name='__Roles (%s)__' % str(role_length), value=roles);
        join.set_footer(text='Created: %s' % time);

        return await self.client.say(embed=join);

def setup(client):
    client.add_cog(Info(client))