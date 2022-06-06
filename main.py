import discord
from discord.ext import commands

from logs.loggeador import loggear

import secret
from services import ItemService,UserService
from DDBB.MHObjects import MHUser

from DDBB import mensajes
import monsterController as monCon

from KeepAlive import keep_alive

bot = commands.Bot(command_prefix='$', description="Hey there, I'm Botty (for example)!")

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
  await ctx.send(mensajes.mensAyuda)
    
@bot.command()
async def mons(ctx, *args):
  mons = monCon.buscarMonstruo(args)
  if mons is None:
    loggear('Monstruo no encontrado')
    await ctx.send(mensajes.mensMonsNoEncontrado)
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
  MHUser = UserService.get_user_info(ctx.author)
  # cuadro = ItemService.buscarItem(args)
  # await ctx.send(embed=cuadro)
  
# keep_alive()

# Token for replit
# bot.run(os.getenv('TOKEN'))
# Token for local
bot.run(secret.TOKEN)