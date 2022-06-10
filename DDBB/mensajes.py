messages = {
    'es': {
    'mensAyuda': 'Hola, aun no sé hacer muchas cosas,\nprueba a poner $mons y el nombre de un monstruo y te daré información\nej: $mons Gran jagras',
    'no_encontrado': 'Lo siento no lo encuentro, ¿está bien escrito?',
    'varios_encontrados': 'He encontrado varios, ¿A cual te refieres?',
<<<<<<< HEAD
=======
    'args_incorrectos': 'Numero de argumentos incorrecto',
    'saludo': 'Hola!, qué tal?\nOtro cazador me ha mandado a saludarte!'
>>>>>>> feature/Users
    }
}

def get_message(mens:str, lang:str):
    return messages[lang][mens]