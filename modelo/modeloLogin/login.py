from modelo.modeloLogin.actualizarContrasena import leerUsuario
from persistencia.persisLogin.perLogin import cargarDatosLogin, incriptar

def inicioSesion():
    # Cargar las credenciales almacenadas
    credenciales = cargarDatosLogin()  
    
    usuIngre = leerUsuario()
    conIngre = input("Ingrese su contraseña: ")

    # Buscar el usuario en las credenciales almacenadas
    for codigo, datos in credenciales.items():
        usuJson = datos.get("usuario")
        contJson = datos.get("contrasena")

        if usuIngre == usuJson:
            # Verificar la contraseña ingresada con la almacenada
            if incriptar(conIngre) == contJson:
                print("¡Acceso concedido!")
                return True  
            else:
                print("Contraseña incorrecta.")
                return False  

    print("Usuario no encontrado.")
    return False  


