import discord
from discord.ext.commands import *
import base64, requests
bot = Bot(command_prefix='/')

@bot.event
async def on_ready():
        print('HELLO DISCORD')
@bot.command()
async def ping(ctx):
        await ctx.send('BOT NAME: ***GENTLE_COSPLAY_BOT*** \nMADE BY: ***MINH QUANG***')
@bot.command()
async def kick(ctx, member: discord.Member,reason='No reason provided'):
        await ctx.send(f'{member.mention} Đã Bị đá khỏi server!')
        await member.send('Bạn đã bị kick =))')
        await member.kick(reason=reason)
@bot.command()
async def ban(ctx, member: discord.Member):
        await ctx.send(f'{member.mention} Đã Bị Ban, Ăn năn hỗi lỗi nhé em!')
        await member.send('Bạn đã bị Ban =))')
        await member.ban()
@bot.command()
async def unban(ctx, member: discord.Member):
        await ctx.send(f'{member.mention} Đã được gỡ Ban!')
        await member.send('Bạn đã được gỡ Ban =))')
        await member.unban()
@bot.command()
async def girl(ctx):
        for i in range(1,100):
                try:
                        with open(f"Coser-baiyin811-Vol.100-2-MrCong.com-00{str(i)}.jpg", "rb") as image_file:
                                b64 = base64.b64encode(image_file.read())

                        data = {
                                'image': b64,
                                'type': 'base64',
                        }

                        headers = {
                                'authorization':'Client-ID 610facfd740080c'
                        }

                        respone = requests.post('https://api.imgur.com/3/image', headers=headers, data=data).json()
                        link = respone['data']['link']
                        await ctx.send(link)
                except:
                        with open(f"Coser-baiyin811-Vol.100-2-MrCong.com-0{str(i)}.jpg", "rb") as image_file:
                                b64 = base64.b64encode(image_file.read())

                        data = {
                                'image': b64,
                                'type': 'base64',
                        }

                        headers = {
                                'authorization':'Client-ID 610facfd740080c'
                        }

                        respone = requests.post('https://api.imgur.com/3/image', headers=headers, data=data).json()
                        try:
                                link = respone['data']['link']
                                await ctx.send(link)
                        except:
                                wait ctx.send('***ẢNH QUÁ NẶNG***')









bot.run('MTAwMDk2NzQ3MDA5MTMzNzgxMQ.GjdvnD.yjLddhJJx73N97QEtn_zTpE6MuQxHZ8yZFVCK4')





