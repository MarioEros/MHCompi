import os
import discord
from discord.ext import commands

import DDBB.MHObjects
from DDBB import mensajes
from DDBB.mensajes import get_message
from logs.loggeador import loggear

from services import ItemService,UserService,MonsterService

from KeepAlive import keep_alive

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


@bot.command(hidden=True)
async def saludar(ctx, *args):
  if len(args) != 1:
    await ctx.send(mensajes.get_message('args_incorrectos', mh_user.lang))
  else:
    receptor = await bot.fetch_user(args[0])
    loggear(receptor.__str__() + ' ha sido saludado')
    await receptor.send(mensajes.get_message('saludo', mh_user.lang))
    await ctx.send(mensajes.get_message('saludo_enviado', mh_user.lang))


@bot.command()
async def helpme(ctx, *args):
  await ctx.send(get_message('mensAyuda', mh_user.lang))


@bot.command()
async def lang(ctx, *args):
  if len(args) != 1:
    await ctx.send(mensajes.get_message('args_incorrectos', mh_user.lang))
  else:
    mensaje = UserService.update_user_lang(mh_user,args[0])
    await ctx.send(mensaje)


@bot.command(help="""Este comando te permite buscar un monstruo por partes de su nombre como rath plat para Rathalos Plateado
En caso de buscar ratha y encontrar mas de uno como Rathalos y Rathalos plateado, devolverá el primero que encuentre
""",brief="Comando para buscar monstruos",usage="diab neg",description="Buscar monstruo",)
async def mons(ctx, *args):
  if len(args) < 1:
    await ctx.send(mensajes.get_message('args_minimos', mh_user.lang))
  else:
    monster = MonsterService.get_monster_info(args,mh_user.lang)
    if monster is None:
      await ctx.send(get_message('no_encontrado',mh_user.lang))
    else:
      cuadro = MonsterService.get_embbed_monster(monster)
      file = discord.File("Imagenes/monster/{}.png".format(monster.nombre_en), filename="image.png")
      cuadro.set_thumbnail(url="attachment://image.png")
      await ctx.send(file=file, embed=cuadro)


UserService.initialize_user_db()

keep_alive()

# Token for replit
bot.run(os.getenv('TOKEN'))