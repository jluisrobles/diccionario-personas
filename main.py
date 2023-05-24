#Reto 4
"""Teniendo la siguiente estructura de un diccionario:
persona =
{
"nombre" : str,
"apellido" : str,
"anyoNacimiento" : int,
"aficiones": array of str,
"dni": { "anyoExpedicion" : int,
"lugarNacimento": str},
"colorPelo" : str
}
Crear una lista de personas con 4 diccionarios de la estructura persona definida en el punto anterior.
Tomando como base la lista anterior:
Mostrar el nombre de todos aquellas personas de la lista que tengan el pelo castaño.
Mostrar la edad de todos los que sean mayores de 30.
Utilizar los bloques try-except-else-finally para tratar las posibles excepciones que
ocurran."""

persona1 = {
    "nombre": "José Luis",
    "apellido": "García",
    "anyoNacimiento": 1999,
    "aficiones": ["fútbol", "música", "viajar"],
    "dni": {
        "anyoExpedicion": 2000,
        "lugarNacimiento": "Madrid"
    },
    "colorPelo": "castaño"
}

persona2 = {
    "nombre": "Ana",
    "apellido": "López",
    "anyoNacimiento": 1987,
    "aficiones": ["leer", "cocinar", "caminar"],
    "dni": {
        "anyoExpedicion": 2005,
        "lugarNacimiento": "Tenerife"
    },
    "colorPelo": "rubio"
}

persona3 = {
    "nombre": "Luis",
    "apellido": "Martínez",
    "anyoNacimiento": 1989,
    "aficiones": ["senderismo", "cine", "buceo"],
    "dni": {
        "anyoExpedicion": 2002,
        "lugarNacimiento": "Valencia"
    },
    "colorPelo": "Calvo"
}

persona4 = {
    "nombre": "Laura",
    "apellido": "González",
    "anyoNacimiento": 1987,
    "aficiones": ["yoga", "guitarra", "jardinería"],
    "dni": {
        "anyoExpedicion": 2006,
        "lugarNacimiento": "Sevilla"
    },
    "colorPelo": "pelirrojo"
}

lista_personas = [persona1, persona2, persona3, persona4]

try:
    print("Personas con pelo castaño:")
    for persona in lista_personas:
        if persona["colorPelo"] == "castaño":
            print(persona["nombre"])
    print("Personas mayores de 30:")
    for persona in lista_personas:
        edad = 2023 - persona["anyoNacimiento"]
        if edad > 30:
            print(persona ["nombre"], edad, "años")
            #print(f"{persona['nombre']}: {edad} años")
except KeyError:
    print("Error: La clave no está presente en uno de los diccionarios.")
except Exception:
    print("Error: sin datos")
finally:
    print("¡Fin del programa!")
