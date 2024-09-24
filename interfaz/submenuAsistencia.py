def menuAsis():
    while True:
        print("")
        print(">>>>           SUBMENU           <<<<")
        print("")
        print("1. Asistencia de entrada ." )
        print("2. Asistencia de salida.")
        print("3. Salida de registro de asitencia.")
        print("")
        print(">>> Seleccione la opcion ?", end="")

        try:
            opcion = int(input())
            if opcion < 1 or opcion > 3:
                print("Error. opcion no valida")
                input("presione cualquier tecla para volver al menu")
                continue
            return opcion
        except ValueError:
            print("Error opcion no valida.")
            input("Presione cualquier tecla para volver al menu")