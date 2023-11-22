def propina():
    costo_comida = float(input("Ingrese el costo de la comida: "))
    porcentaje_propina = float(input("Ingrese el porcentaje de propina que desea dejar: "))

    propina = costo_comida * (porcentaje_propina / 100)
    costo_total = costo_comida + propina

    print(f"Propina: ${propina:.2f}")
    print(f"Costo total de la comida: ${costo_total:.2f}")
