from modelo.modeloLogin.login import inicioSesion
from modelo.modeloLogin.actualizarContrasena import cambiarContrasena
from interfaz.inicio import inicio
from interfaz.fin import fin
from interfaz.inmenu import menu
from modelo.modeloGrupo.grupo import registrarGrupo
from modelo.modeloModulo.modulo import registrarModulo
from modelo.modeloEstudiantes.estudiantes import registrarEstudiante
from modelo.modeloProfesores.profesor import registrarProfesor

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
            registrarGrupo()
        case 2:
            registrarModulo()
        case 3:
            registrarEstudiante()
        case 4:
            registrarProfesor()
        case 5:
            pass
        case 6:
            pass
        case 7:
           pass
        case 8:
            cambiarContrasena()
        case 9:
            fin()
            
            break