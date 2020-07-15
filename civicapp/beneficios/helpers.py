import random
import string

def calcular_edad(fecha_nacimiento):
    return 0

def generar_codigo(length):
    """Genera un código alfanúmerico aleatorio de la longitud dada.
    """
    letters_digits = string.ascii_uppercase + string.digits
    return  "".join(random.choice(letters_digits) for i in range(length))