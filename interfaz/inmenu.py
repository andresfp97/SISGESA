
def menu():
    while True:
        print("")
        print(">>>>             MENU            <<<<")
        print("")
        print("1. Registro de grupos." )
        print("2. Registro de módulos.")
        print("3. Registro de estudiantes. " )
        print("4. Registro de docentes. " )
        print("5. Registro de docentes. " )
        print("7. Registro de asistencia." )
        print("8. Consultas de información." )
        print("9. Generación de informes. " )
        print("10. Cambio de contraseña. " )
        print("9. Salida del sistema.")
        print("")
        print(">>> Seleccione la opcion ?", end="")

        try:
            opcion = int(input())
            if opcion < 1 or opcion > 9:
                print("Error. opcion no valida")
                input("presione cualquier tecla para volver al menu")
                continue
            return opcion
        except ValueError:
            print("Error opcion no valida.")
            input("Presione cualquier tecla para volver al menu")
            


