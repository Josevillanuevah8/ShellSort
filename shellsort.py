
def shell_sort(numeros):
    cantidad = len(numeros)
    salto = cantidad // 2

    while salto > 0:
        for i in range(salto, cantidad):
            temporal = numeros[i]
            j = i

            while j >= salto and numeros[j - salto] > temporal:
                numeros[j] = numeros[j - salto]
                j -= salto

            numeros[j] = temporal

        salto //= 2

    return numeros


while True:
    print("\n===== MENU SHELLSORT =====")
    print("1. Ordenar numeros")
    print("2. Salir")

    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        cantidad = int(input("Cuantos numeros desea ingresar: "))

        numeros = []
        for i in range(cantidad):
            numero = int(input(f"Ingrese el numero {i + 1}: "))
            numeros.append(numero)

        print("Numeros originales:", numeros)
        print("Numeros ordenados:", shell_sort(numeros))

    elif opcion == "2":
        print("Saliendo del programa...")
        break

    else:
        print("Opcion incorrecta, intente nuevamente.")
