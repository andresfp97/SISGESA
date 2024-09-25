def menuAsis():
    while True:
        print("")
        print(">>>>           SUBMENU           <<<<")
        print("")
        print("1. Asistencia de entrada ." )
        print("2. Asistencia de salida.")
        print("3. Salir.")
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
            
            
def menuconsulAsis():
    while True:
        print("")
        print(">>>>           SUBMENU           <<<<")
        print("")
        print("1. Estudiantes que han llegado tarde a un módulo en un mes específico. " )
        print("2. Estudiantes que se retirarán antes de la finalización de una sesión en un mes específico. ")
        print("3. Estudiantes que no han faltado a ningún módulo durante un mes. ")
        print("4. Porcentaje de asistencia por módulo, calculado como la proporción de estudiantes que asistieron al inicio de clase respecto al total de estudiantes matriculados.")
        print("5. salir")
        print("")
        print(">>> Seleccione la opcion ?", end="")

        try:
            opcion = int(input())
            if opcion < 1 or opcion > 5:
                print("Error. opcion no valida")
                input("presione cualquier tecla para volver al menu")
                continue
            return opcion
        except ValueError:
            print("Error opcion no valida.")
            input("Presione cualquier tecla para volver al menu")
            
 
def menuconsulCodigo():
    while True:
        print("")
        print(">>>>           SUBMENU           <<<<")
        print("")
        print("1. Consultar los estudiantes matriculados en un grupo." )
        print("2. Consultar los estudiantes inscritos en un módulo.")
        print("3. Consultar los docentes que imparten un módulo.")
        print("4. Consultar los estudiantes a cargo de un docente en un módulo.")
        print("5. salir")
        print("")
        print(">>> Seleccione la opcion ?", end="")

        try:
            opcion = int(input())
            if opcion < 1 or opcion > 5:
                print("Error. opcion no valida")
                input("presione cualquier tecla para volver al menu")
                continue
            return opcion
        except ValueError:
            print("Error opcion no valida.")
            input("Presione cualquier tecla para volver al menu")
 
 