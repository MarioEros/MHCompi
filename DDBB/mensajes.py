messages = {
    'es': {
    'mensAyuda': 'Hola, aun no sé hacer muchas cosas,\nprueba a poner $mons y el nombre de un monstruo y te daré información\nej: $mons Gran jagras',
    'no_encontrado': 'Lo siento no lo encuentro, ¿está bien escrito?',
    'varios_encontrados': 'He encontrado varios, ¿A cual te refieres?',
    'args_incorrectos': 'Numero de argumentos incorrecto',
    'args_minimos': 'Debes especificar al menos un argumento',
    'saludo': 'Hola!, qué tal?\nOtro cazador me ha mandado a saludarte!',
    'saludo_enviado': 'Se ha enviado el saludo! ^^',
    }
}

def get_message(mensaje:str, lang:str):
    try:
        mens = messages[lang][mensaje]
    except KeyError:
        #Si no existe ponemos un default
        mens = messages['es'][mensaje]
    return mens[mensaje]
