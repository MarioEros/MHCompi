import discord
from discord.ext import commands

import DDBB.MHObjects
from DDBB import mensajes
from DDBB.mensajes import get_message
from logs.loggeador import loggear

from services import ItemService,UserService,MonsterService

from KeepAlive import keep_alive

import secret #TODO remove to deploy in replit

bot = commands.Bot(command_prefix='$', description="¡Soy un feline-bot que está aquí para ayudarte!")
mh_user: DDBB.MHObjects.MHUser = None

@bot.event
async def on_ready():
  loggear('Estamos loggeados como {0.user}'.format(bot))
  
@bot.event
async def on_message(message):
  if message.author.bot:
    return
  loggear(message.author.__str__()+' ha enviado: '+ message.content)
  global mh_user
  mh_user= UserService.get_user_info(message.author)
  await bot.process_commands(message)
  mh_user = None
  
@bot.command(help='Hola')
async def hola(ctx):
  await ctx.send(ctx.author.mention + ", miaumonos de caza!")

@bot.command()
async def ayuda(ctx, msg):
  await ctx.send(get_message('mensAyuda','es'))
    
@bot.command() #TODO Arreglar
async def mons(ctx, *args):
  monster = MonsterService.get_monster_info(args,mh_user.lang)
  if monster is None:
    await ctx.send(get_message('no_encontrado',mh_user.lang))
  else:
    cuadro = MonsterService.get_embbed_monster(monster)
    file = discord.File("Imagenes/monster/{}.png".format(monster.nombre_en), filename="image.png")
    cuadro.set_thumbnail(url="attachment://image.png")
    await ctx.send(file=file, embed=cuadro)

@bot.command() #TODO Arreglar
async def item(ctx, *args):
  return None
  cuadro = ItemService.buscarItem(args)
  await ctx.send(embed=cuadro)

@bot.command()
async def saludar(ctx, *args):
  if len(args) != 1:
    await ctx.send(mensajes.get_message('args_incorrectos','es'))
  else:
    receptor = await bot.fetch_user(args[0])
    loggear(receptor.__str__()+' ha sido saludado')
    await receptor.send(mensajes.get_message('saludo','es'))
    await ctx.send(mensajes.get_message('saludo_enviado','es'))


# keep_alive()

# Token for replit
# bot.run(os.getenv('TOKEN'))
# Token for local
bot.run(secret.TOKEN)