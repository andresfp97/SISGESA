
def menu():
    while True:
        print("")
        print(">>>>             MENU            <<<<")
        print("")
        print("1. Registro de grupos." )
        print("2. Registro de módulos.")
        print("3. Registro de estudiantes. " )
        print("4. Registro de docentes. " )
        print("5. Asignacion de estudiantes a grupos." )
        print("6. Asignacion de estudiantes a modulos ." )
        print("7. Asignacion de profesores a modulos ." )
        print("8. Registro de asistencia ." )
        print("9. Consultas de información." )
        print("10. Generación de informes. " )
        print("11. Cambio de contraseña. " )
        print("12. Salida del sistema.")
        print("")
        print(">>> Seleccione la opcion ?", end="")

        try:
            opcion = int(input())
            if opcion < 1 or opcion > 12:
                print("Error. opcion no valida")
                input("presione cualquier tecla para volver al menu")
                continue
            return opcion
        except ValueError:
            print("Error opcion no valida.")
            input("Presione cualquier tecla para volver al menu")
            


