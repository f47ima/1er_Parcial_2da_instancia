
def verificar_minuscula(letra:str):
    minuscula = False
    if (ord(letra) >= 97 and ord(letra) <= 122) or ord(letra) == 164 or ord(letra) == 241:
        minuscula = True
    return minuscula

def verificar_mayuscula(letra:str):
    mayuscula = False
    if (ord(letra) >= 65 and ord(letra) <= 90) or ord(letra) == 165 or ord(letra) == 209:
        mayuscula = True
    return mayuscula

def cambiar_letra_minus_mayus(letra:str,booleano:bool= True)-> str:
    if type(letra) == str and len(letra) == 1:
        if booleano and verificar_minuscula(letra):
            letra = chr(ord(letra) - 32) 
        elif not booleano and verificar_mayuscula(letra):
            letra = chr(ord(letra) + 32) 
    return letra

def cambiar_cadena_minus_mayus(cadena:str, booleano:bool = True):
    nueva_cadena = ""
    if len(cadena) > 0:
        for i in range(len(cadena)):
            nueva_cadena += cambiar_letra_minus_mayus(cadena[i], booleano)
    return nueva_cadena

def capitalizar_cadena(cadena:str):
    cadena_capitalizada = ""
    if len(cadena) > 0:
        primer_caracter = cambiar_letra_minus_mayus(cadena[0], True)
        resto_cadena = cambiar_cadena_minus_mayus(cadena[1:],False)
        cadena_capitalizada = primer_caracter + resto_cadena
    return cadena_capitalizada

def devolver_lista_capitalizada(lista_cadenas:list):
    lista = []
    for i in range(len(lista_cadenas)):
        lista += [capitalizar_cadena(lista_cadenas[i])]
    return lista 

def devolver_lista_convertida_a_mayus(lista_cadenas:list):
    lista = []
    for i in range(len(lista_cadenas)):
        lista += [cambiar_cadena_minus_mayus(lista_cadenas[i])]
    return lista

def devolver_lista_formateada(lista_cadenas:list, booleano:bool):
    if booleano:
        lista = devolver_lista_capitalizada(lista_cadenas)
    if not booleano:
        lista = devolver_lista_convertida_a_mayus(lista_cadenas)
    return lista

def encontrar_elemento_en_lista(elemento,lista:list)-> bool:
    """Valida que el ingreso se encuentre dentro de la lista indicada.
    Recibe un string y una lista.
    Devuelve True si esta, si no False."""
    bandera = False
    for i in range(len(lista)):
        if elemento == lista[i]:
            bandera = True
            break
    return bandera

def validar_float(ingreso:str):
    inicio = 0
    valido = True
    punto= False
    digito = False
    if len(ingreso) > 0 and (ord(ingreso[0]) == 43 or ord(ingreso[0]) == 45):
        inicio = 1 
    if len(ingreso) > inicio:
        for i in range(inicio,len(ingreso)):
            orden = ord(ingreso[i])
            if orden == 46:
                if not punto:
                    punto = True
                else:
                    valido = False
            elif orden >= 48 and orden <= 57:
                digito = True
            else:
                valido = False
    else:
        valido = False
    bandera = valido and digito
    return bandera

def validar_entero(ingreso:str):
    bandera = False
    inicio = 0
    if len(ingreso) > 0 and (ord(ingreso[0]) == 43 or ord(ingreso[0]) == 45):
        inicio = 1 
    if len(ingreso) > inicio:
        for i in range(inicio,len(ingreso)):
            orden_numero = ord(ingreso[i])
            if (orden_numero >= 48 and orden_numero <= 57):
                bandera = True
            else:
                bandera = False
                break
    return bandera