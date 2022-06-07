messages = {
    'es': {
    'mensAyuda': 'Hola, aun no sé hacer muchas cosas,\nprueba a poner $mons y el nombre de un monstruo y te daré información\nej: $mons Gran jagras',
    'no_encontrado': 'Lo siento no lo encuentro, ¿está bien escrito?',
    'varios_encontrados': 'He encontrado varios, ¿A cual te refieres?',
    'args_incorrectos': 'Numero de argumentos incorrecto',
    'saludo': 'Hola!, qué tal?\nOtro cazador me ha mandado a saludarte!'
    }
}

def get_message(mens:str, lang:str):
    return messages[lang][mens]