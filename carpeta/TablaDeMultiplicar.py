def tablas():
    inicio_rango = int(input("ingresa el inicio"))
    final_rango = int(input("ingresa el final"))
    inicio_tabla = int(input("ingresa el inicio de la tabla"))
    final_tabla = int(input("ingresa el final de la tabla"))

    for i in range(inicio_rango, final_rango + 1):
        for j in range(inicio_tabla,final_tabla +1):
            resultado = i * j
            print(i,"x", j,"=", resultado)
        print()