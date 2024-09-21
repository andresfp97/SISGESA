
def menu():
    while True:
        print("")
        print(">>>>             MENU            <<<<")
        print("")
        print("A. Registro de grupos." )
        print("B. Registro de módulos.")
        print("C. Registro de estudiantes. " )
        print("D. Registro de docentes. " )
        print("E. Registro de asistencia." )
        print("F. Consultas de información." )
        print("G. Generación de informes. " )
        print("H. Cambio de contraseña. " )
        print("I. Salida del sistema.")
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


menu()


