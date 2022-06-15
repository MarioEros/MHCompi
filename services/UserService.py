import discord
from DDBB import UserRepo,mensajes
from DDBB.MHObjects import MHUser

def get_user_info(disc_user: discord.User):
    user = MHUser((disc_user.id,disc_user.name+'#'+disc_user.discriminator,None))
    ret_user = UserRepo.get_user_info(user)
    return ret_user

def update_user_lang(user: MHUser, lang):
    lang = UserRepo.get_lang_info(lang)
    if lang is None:
        return mensajes.get_message("idioma_not_found",user.lang)
    else:
        UserRepo.update_lang(user,lang)
        return mensajes.get_message("lang_updated",lang)

def initialize_user_db():
    UserRepo.set_up_user_table()