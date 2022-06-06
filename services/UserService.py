import discord
from DDBB import UserRepo
from DDBB.MHObjects import MHUser
import loggeador

def get_user_info(disc_user: discord.User):
    user = MHUser(disc_user.id,disc_user.name+'#'+disc_user.discriminator,None)
    UserRepo.get_user_info(user)
    return user

paco = discord.User

paco.name = 'Kelfindel'
paco.id = 156000408412618754
paco.discriminator = '7546'

print(get_user_info(paco))