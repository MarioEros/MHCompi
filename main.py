import discord
from discord.ext import commands

from DDBB.mensajes import get_message
import monsterController as monCon
import itemController as itemCon
import os
from loggeador import loggear

from KeepAlive import keep_alive

bot = commands.Bot(command_prefix='$', description="¡Soy un feline-bot que está aquí para ayudarte!")

@bot.event
async def on_ready():
  loggear('Estamos loggeados como {0.user}'.format(bot))
  
@bot.event
async def on_message(message):
  if message.author.bot:
    return
  loggear(message.author.name+' ha enviado: '+ message.content)
  await bot.process_commands(message)
  
@bot.command(help='Hola')
async def hola(ctx):
  await ctx.send(ctx.author.mention + ", miaumonos de caza!")

@bot.command()
async def ayuda(ctx, msg):
  await ctx.send(get_message('mensAyuda','es'))
    
@bot.command()
async def mons(ctx, *args):
  mons = monCon.buscarMonstruo(args)
  if mons is None:
    loggear('Monstruo no encontrado')
    await ctx.send(get_message('no_encontrado','es'))
  else:
    loggear(mons.nombre + ' encontrado')
    cuadro=discord.Embed(title = mons.nombre, description = mons.desc)
    cuadro.set_thumbnail(url=mons.url)
    for debilidad in mons.debil:
      cuadro.add_field(name="Normal" if debilidad.forma=="normal" else debilidad.descripcion, value=debilidad.elemento, inline=True)
    cuadro.add_field(name='Estados', value=mons.estado, inline=False)
    await ctx.send(embed=cuadro)

@bot.command()
async def item(ctx, *args):
  item_found = itemCon.buscarItem(args)
  if item_found is None:
    await ctx.send(get_message('no_encontrado','es'))
  else:
    cuadro = discord.Embed(title=item_found.nombre, description=item_found.desc)
    await ctx.send(embed=cuadro)
  
keep_alive()

bot.run(os.getenv('TOKEN'))