import json
from persistencia.persisLogin.perLogin import cargarDatosLogin, incriptar
from utils.validacion import leerUsuario

rutaDatosLogin = "datos\\credenciales.json"

def cambiarContrasena():
    # Cargar las credenciales del JSON
    credenciales = cargarDatosLogin()

    usuIngre = input("ingrese el usuario --> admin: ")

    # Verificamos si el usuario existe
    for codigo, datos in credenciales.items():
        usuJson = datos.get("usuario")

        if usuIngre == usuJson:
            
            nuevaContra = input("Ingrese su nueva contraseña: ")
            confirmacionContra = input("Confirme su nueva contraseña: ")

            # Verificamos si la confirmación coincide
            if nuevaContra == confirmacionContra:
                nuevaContraEncrip = incriptar(nuevaContra)
                credenciales[codigo]["contrasena"] = nuevaContraEncrip

                # Guardamos las credenciales actualizadas en el archivo JSON
                with open(rutaDatosLogin, "w") as file:
                    json.dump(credenciales, file)

                print("Contraseña cambiada con éxito.")
                return True
            else:
                print("Las contraseñas no coinciden. Intente nuevamente.")
                return False
    print("Usuario no encontrado.")
    return False
