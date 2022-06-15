messages = {
    'en': {
    'mensAyuda': """Hi, im still improving...,\ntry to write $mons and the name of a monster and i'll get the info\nex: $mons Great jagras""",
    'no_encontrado': """Not found, it's writen correctly?""",
    'varios_encontrados': """I found many, which one you want?""",
    'args_incorrectos': """Incorrect number of arguments""",
    'args_minimos': """You should specify at least one argument""",
    'saludo': """Hi!, What's up?\nAnother hunter sends me to greet you!""",
    'saludo_enviado': """Greeting sent! ^^""",
    'idioma_not_found': """Language not found :(""",
    'lang_updated': """Language updated to english! :D"""
    },
    'es': {
    'mensAyuda': 'Hola, aun no sé hacer muchas cosas,\nprueba a poner $mons y el nombre de un monstruo y te daré información\nej: $mons Gran jagras',
    'no_encontrado': 'Lo siento no lo encuentro, ¿está bien escrito?',
    'varios_encontrados': 'He encontrado varios, ¿A cual te refieres?',
    'args_incorrectos': 'Numero de argumentos incorrecto',
    'args_minimos': 'Debes especificar al menos un argumento',
    'saludo': 'Hola!, qué tal?\nOtro cazador me ha mandado a saludarte!',
    'saludo_enviado': 'Se ha enviado el saludo! ^^',
    'idioma_not_found': 'No he encontrado ese idioma :(',
    'lang_updated': '¡Idioma actualizado al español! :D'
    }
}

def get_message(mensaje:str, lang:str) -> str:
    try:
        mens = messages[lang][mensaje]
    except KeyError:
        #Si no existe ponemos un default
        mens = messages['es'][mensaje]
    return mens
