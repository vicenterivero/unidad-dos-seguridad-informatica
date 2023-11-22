def adivinansa():
    import random

    numero_secreto = random.randint(1, 10)

    while True:
        intento = int(input("Adivina el número (entre 1 y 10): "))
        if intento == numero_secreto:
            print("¡Felicidades! ¡Adivinaste el número!")
            break
        elif intento < numero_secreto:
            print("El número es mayor. Intenta de nuevo.")
        else:
            print("El número es menor. Intenta de nuevo.")