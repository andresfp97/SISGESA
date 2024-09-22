import json
from persistencia.persisLogin.perLogin import cargarDatosLogin, incriptar

rutaDatosLogin = "datos\\credenciales.json"


def leerUsuario():
    while True:
        try:
            nombre = input("Ingrese su nombre de usuario: ").strip()
            
            if len(nombre) == 0:
                print(">>> ERROR. Usuario invalido")
                continue
            return nombre

        except Exception as e:
            print("Error al ingresar el nombre.\n" + e)


def cambiarContrasena():
    # Cargar las credenciales del JSON
    credenciales = cargarDatosLogin()

    usuIngre = leerUsuario()

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
