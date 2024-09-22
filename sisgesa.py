from modelo.modeloLogin.login import inicioSesion
from modelo.modeloLogin.actualizarContrasena import cambiarContrasena
from interfaz.inicio import inicio
from interfaz.fin import fin
from interfaz.inmenu import menu


inicio()
print("\n"*13)
permiso = False

while True:
    print("Usuario    --->  'admin' ")
    print("Contraseña --->  'SISGESA'")
    permiso = inicioSesion()
    if permiso:
        break
       
while permiso:
    
    op = menu()
    match op:
        case 1:
           pass
        case 2:
            pass
        case 3:
            pass
        case 4:
           pass
        case 5:
            pass
        case 6:
            pass
        case 7:
           pass
        case 8:
            pass
        case 9:
            fin()
            
            break