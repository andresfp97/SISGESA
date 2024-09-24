from modelo.modeloLogin.login import inicioSesion
from modelo.modeloLogin.actualizarContrasena import cambiarContrasena
from interfaz.inicio import inicio
from interfaz.fin import fin
from interfaz.inmenu import menu
from modelo.modeloEntidades.grupo import registrarGrupo
from modelo.modeloEntidades.modulo import registrarModulo
from modelo.modeloEntidades.estudiantes import registrarEstudiante
from modelo.modeloEntidades.profesor import registrarProfesor
from modelo.modeloasignar.estudianteGrupo import asignarEstudianteGrupo
from modelo.modeloasignar.estudianteModulo import asignarEstudianteModulo

# inicio()
# print("\n"*13)
# permiso = False

# while True:
#     print("Usuario    --->  'admin' ")
#     print("Contraseña --->  'SISGESA'")
#     permiso = inicioSesion()
#     if permiso:
#         break
    
#cambiar True por permiso    
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
                otro = input("¿quiere ingresar otro estudiante? (s/n): ").strip().lower()
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
             
                otro = input("¿quiere asignar otro estudiante a grupo? (s/n): ").strip().lower()
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
                otro = input("¿quiere asignar otro estudiante a modulo? (s/n): ").strip().lower()
                if otro == "y":
                    p = True
                elif otro == "n":
                    p = False
        case 7:
           pass
        case 8:
            cambiarContrasena()
        case 9:
            fin()
            
            break