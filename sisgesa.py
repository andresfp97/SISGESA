from modelo.modeloLogin.login import inicioSesion
from modelo.modeloLogin.actualizarContrasena import cambiarContrasena
from interfaz.inicio import inicio
from interfaz.fin import fin
from interfaz.inmenu import menu
from interfaz.submenus import menuAsis, menuconsulAsis, menuconsulCodigo
from modelo.modeloEntidades.grupo import registrarGrupo
from modelo.modeloEntidades.modulo import registrarModulo
from modelo.modeloEntidades.estudiantes import registrarEstudiante
from modelo.modeloEntidades.profesor import registrarProfesor
from modelo.modeloAsignar.estudianteGrupo import asignarEstudianteGrupo
from modelo.modeloAsignar.estudianteModulo import asignarEstudianteModulo
from modelo.modeloAsistencia.asistencia import tomarAsistencia, tomarSalida
from consultasInformes.consultasCodigo import (
    consultarEstudiantesEnGrupo,
    consultarEstudiantesEnModulo,
    consultarDocentesEnModulo,
    consultarEstudiantesPorDocenteEnModulo,
)
from consultasInformes.consultasAsistencia import (
    estudiantes_tarde_mes,
    estudiantes_asistencia_completa_mes,
    estudiantes_retiro_antes_mes,
    porcentaje_asistencia_modulo,
)

# inicio()
# print("\n"*13)
# permiso = False

# while True:
#     print("Usuario    --->  'admin' ")
#     print("Contraseña --->  'SISGESA'")
#     permiso = inicioSesion()
#     if permiso:
#         break

# cambiar True por permiso
while True:
    op = menu()
    match op:
        case 1:
            p = True
            while p:
                registrarGrupo()
                otro = input("¿quiere ingresar otro grupo? (s/n): ").strip().lower()
                if otro == "s":
                    p = True
                elif otro == "n":
                    p = False
        case 2:
            p = True
            while p:
                registrarModulo()
                otro = input("¿quiere ingresar otro modulo? (s/n): ").strip().lower()
                if otro == "s":
                    p = True
                elif otro == "n":
                    p = False
        case 3:
            p = True
            while p:
                registrarEstudiante()
                otro = (
                    input("¿quiere ingresar otro estudiante? (s/n): ").strip().lower()
                )
                if otro == "s":
                    p = True
                elif otro == "n":
                    p = False
        case 4:
            p = True
            while p:
                registrarProfesor()
                otro = input("¿quiere ingresar otro Profesor? (s/n): ").strip().lower()
                if otro == "s":
                    p = True
                elif otro == "n":
                    p = False
        case 5:
            p = True
            while p:
                codEstudiante = input("ingrese el codigo de estudiante: ")
                codGrupo = input("ingrese el codigo del grupo: ")
                asignarEstudianteGrupo(codEstudiante, codGrupo)

                otro = (
                    input("¿quiere asignar otro estudiante a grupo? (s/n): ")
                    .strip()
                    .lower()
                )
                if otro == "s":
                    p = True
                elif otro == "n":
                    p = False
        case 6:
            p = True
            while p:
                codEstudiante = input("ingrese el codigo de estudiante: ")
                codModulo = input("ingrese el codigo del modulo: ")
                asignarEstudianteModulo(codEstudiante, codModulo)
                otro = (
                    input("¿quiere asignar otro estudiante a modulo? (s/n): ")
                    .strip()
                    .lower()
                )
                if otro == "y":
                    p = True
                elif otro == "n":
                    p = False
        case 7:
            while True:
                op1 = menuAsis()
                match op1:
                    case 1:
                        tomarAsistencia()
                    case 2:
                        tomarSalida()
                    case 3:
                        break
        case 8:
            while True:
                op1 = menuconsulCodigo()
                match op1:
                    case 1:
                        codigoEstudiante = input("Ingrese codigo estudiante: ")
                        consultarEstudiantesEnGrupo(codigoEstudiante)
                    case 2:
                        codigoEstudiante = input("Ingrese codigo estudiante: ")
                        consultarEstudiantesEnModulo(codigoEstudiante)
                    case 3:
                        codigoModulo = input("Ingrese codigo estudiante: ")
                        consultarDocentesEnModulo(codigoModulo)
                    case 4:
                        codigoDocente = input("Ingrese codigo de docente: ")
                        codigoDocente = input("Ingrese codigo de Modulo: ")
                        consultarEstudiantesPorDocenteEnModulo (codigoModulo)
                    case 5:
                        break

        case 9:
            while True:
                op1 = menuconsulAsis()
                match op1:
                    case 1:
                        codigo_modulo = input("Ingrese el código del módulo: ")
                        mes = int(input("Ingrese el mes (1-12): "))
                        anio = int(input("Ingrese el año: "))
                        estudiantes_tarde_mes(codigo_modulo, mes, anio)
                    case 2:
                        codigo_modulo = input("Ingrese el código del módulo: ")
                        mes = int(input("Ingrese el mes (1-12): "))
                        anio = int(input("Ingrese el año: "))
                        estudiantes_retiro_antes_mes(codigo_modulo, mes, anio)
                    case 3:
                        mes = int(input("Ingrese el mes (1-12): "))
                        anio = int(input("Ingrese el año: "))
                        estudiantes_asistencia_completa_mes(mes, anio)
                    case 4:
                        codigo_modulo = input("Ingrese el código del módulo: ")
                        mes = int(input("Ingrese el mes (1-12): "))
                        anio = int(input("Ingrese el año: "))
                        porcentaje_asistencia_modulo(codigo_modulo, mes, anio)
                    case 5:
                        break
        case 10:
            cambiarContrasena()
        case 11:
            fin()
            break
