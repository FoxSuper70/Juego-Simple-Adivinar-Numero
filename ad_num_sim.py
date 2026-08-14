import random 

def dificultad():
    dif = input("Selecione la dificultad: Fácil (1), Normal (2), Difícil (3), Extremo (4):")
    if dif == "1":
        facil()
    elif dif == "2":
        normal()
    elif dif == "3":
        dificil()
    elif dif == "4":
        extremo()
    else:
        print("Dificultad no válida.")
        dificultad()

def facil():
    print("Has elegido la dificultad fácil, deberás adivinar el número del 1 al 10. Empecemos!")
    respuesta = random.randint(1, 10)
    while True:
        try:
            numero = int(input("Escribe el número:"))
        except ValueError:
            print("Tienes que escribir un número.")
        if numero == respuesta:
            print("Excelente lo has adivinado! Mi número era:", respuesta)
            return
        elif numero > 10:
            print("Incorrecto, el número que he pensado es del 1 al 10!")
        else:
            print("Número incorrecto!")

def normal():
    print("Has elegido la dificultad normal, deberás adivinar el número del 1 al 25. Empecemos!")
    respuesta = random.randint(1, 25)
    while True:
        try:
            numero = int(input("Escribe el número:"))
        except ValueError:
            print("Tienes que escribir un número.")
        if numero == respuesta:
            print("Excelente lo has adivinado! Mi número era:", respuesta)
            return
        elif numero > 25:
            print("Incorrecto, el número que he pensado es del 1 al 25!")
        else:
            print("Número incorrecto!")


def dificil():
    print("Has elegido la dificultad difícil, deberás adivinar el número del 1 al 50. Empecemos!")
    respuesta = random.randint(1, 50)
    while True:
        try:
            numero = int(input("Escribe el número:"))
        except ValueError:
            print("Tienes que escribir un número.")
        if numero == respuesta:
            print("Excelente lo has adivinado! Mi número era:", respuesta)
            return
        elif numero > 50:
            print("Incorrecto, el número que he pensado es del 1 al 50!")
        else:
            print("Número incorrecto!")


def extremo():
    print("Has elegido la dificultad extremo, deberás adivinar el número del 1 al 500. Como esta díficultad es la más difícil te brindaré un poco de ayuda... Empecemos!")
    respuesta = random.randint(1, 500)
    while True:
        try:
            numero = int(input("Escribe el número:"))
        except ValueError:
            print("Tienes que escribir un número.")
        if numero == respuesta:
            print("Excelente lo has adivinado! Mi número era:", respuesta)
            return
        elif numero > respuesta:
            print("Incorrecto! Mi número es más pequeño!")
        elif numero < respuesta:
            print("Incorrecto! Mi número es más grande!")


while True:
    dificultad()