import discord
from discord.ext import commands
from discord.utils import get
import asyncio

client = commands.Bot(command_prefix='.')
client.remove_command('help')

@client.event
async def on_ready():
    print('bot online')
    await client.change_presence(status=discord.Status.online, activity=discord.Activity(name="DM for .menfess", type=discord.ActivityType.watching))


@client.command()
async def menfess(ctx):
    if ctx.channel.type == discord.ChannelType.private:
        mbed = discord.Embed(
            title='Ketik menfess kamu',
            description='Jangan abuse sistem menfess atau di mute\n\nBot hanya support text'

        )
        mbed.set_footer(text='Kamu memiliki 10 detik untuk tulis menfess')
        demand = await ctx.send(embed=mbed)

        try:
            msg = await client.wait_for(
                'message',
                timeout=10,
                check=lambda message: message.author == ctx.author and message.channel == ctx.channel

            )
            if not msg.attachments:
                channel = get(client.get_all_channels(), guild__name='CS++', name='pacil-menfess')
                mbed = discord.Embed(
                    title='Menfess Pacil',
                    description=f'{msg.content}',
                    color=discord.Colour.random()
                )
                mbed.set_footer(text='Ketik .menfess di DM untuk menfess')
                await channel.send(embed=mbed)
                await demand.delete()

            else:
                await ctx.author.send('Pastikan menfess nya hanya text saja ya', delete_after=5)

        except asyncio.TimeoutError:
            await ctx.send('Gak jadi ya?', delete_after=5)
            await demand.delete()

    else:
        await ctx.message.delete()
        await ctx.send('Baca DM bro', delete_after=5)
        await ctx.author.send('BOT hanya menerima menfess melalui DM', delete_after=10)

client.run('TOKEN')



