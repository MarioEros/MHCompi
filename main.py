import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

import DDBB.MHObjects
from DDBB import mensajes
from DDBB.mensajes import get_message
from logs.loggeador import loggear

from services import ItemService, UserService, MonsterService

from KeepAlive import keep_alive

load_dotenv()
token = os.getenv('TOKEN')
if not token:
    raise ValueError("No se encontró el token en las variables de entorno")
print("Token cargado:", token[:10] + "..." if token else "No token")

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(
    command_prefix='$', 
    description="¡Soy un feline-bot que está aquí para ayudarte!",
    intents=intents
)

mh_user: DDBB.MHObjects.MHUser = None

@bot.event
async def on_ready():
    loggear(f'Estamos loggeados como {bot.user}')
    print(f'Bot listo y conectado como: {bot.user}')

@bot.event
async def on_message(message: discord.Message):
    if message.author.bot:
        return
    loggear(f'{message.author} ha enviado: {message.content}')
    global mh_user
    mh_user = UserService.get_user_info(message.author)
    await bot.process_commands(message)
    mh_user = None

@bot.command(hidden=True)
async def saludar(ctx: commands.Context, user_id: str):
    if not user_id.isdigit():
        await ctx.send(mensajes.get_message('args_incorrectos', mh_user.lang))
        return
    receptor = await bot.fetch_user(int(user_id))
    loggear(f'{receptor} ha sido saludado')
    await receptor.send(mensajes.get_message('saludo', mh_user.lang))
    await ctx.send(mensajes.get_message('saludo_enviado', mh_user.lang))

@bot.command()
async def helpme(ctx: commands.Context):
    await ctx.send(get_message('mensAyuda', mh_user.lang))

@bot.command()
async def lang(ctx: commands.Context, lang_code: str):
    mensaje = UserService.update_user_lang(mh_user, lang_code)
    await ctx.send(mensaje)

@bot.command(
    help="""Este comando te permite buscar un monstruo por partes de su nombre como rath plat para Rathalos Plateado
En caso de buscar ratha y encontrar más de uno como Rathalos y Rathalos Plateado, devolverá el primero que encuentre
""",
    brief="Comando para buscar monstruos",
    usage="diab neg",
    description="Buscar monstruo",
)
async def mons(ctx: commands.Context, *args: str):
    if not args:
        await ctx.send(mensajes.get_message('args_minimos', mh_user.lang))
        return
    monster = MonsterService.get_monster_info(args, mh_user.lang)
    if monster is None:
        await ctx.send(get_message('no_encontrado', mh_user.lang))
    else:
        cuadro = MonsterService.get_embbed_monster(monster)
        image_path = f"Imagenes/monster/{monster.nombre_en}.png"
        if os.path.exists(image_path):
            file = discord.File(image_path, filename="image.png")
            cuadro.set_thumbnail(url="attachment://image.png")
            await ctx.send(file=file, embed=cuadro)
        else:
            await ctx.send(embed=cuadro)

UserService.initialize_user_db()

keep_alive()

# Token for replit
bot.run(token)