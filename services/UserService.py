import discord
from DDBB import UserRepo
from DDBB.MHObjects import MHUser

def get_user_info(disc_user: discord.User):
    user = MHUser(disc_user.id,disc_user.name+'#'+disc_user.discriminator,None)
    UserRepo.get_user_info(user)
    return user
#
# crearUsuario1 = discord.User
# crearUsuario1.id = 156000408412618754
# crearUsuario1.name = 'Kelfindel'
# crearUsuario1.discriminator = '7546'
#
# get_user_info(crearUsuario1)