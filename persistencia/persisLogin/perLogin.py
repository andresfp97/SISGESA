import hashlib
import os
import json

rutaDatosLogin = "datos\\credenciales.json"

def incriptar(contra):
    #crea una instancia del algotimo  SHA-256
    incrip = hashlib.sha256()
    # convierte la contraseña a bytes  y actualiza (encripa)
    incrip.update(contra.encode("utf-8"))
    #aqui la contraseña incriptada la convierte en formato hexadecimal
    contraIncrip = incrip.hexdigest()
    return contraIncrip


def cargarDatosLogin():
    #  se pregunta si la ruta del Json  no existe
    
    if not os.path.exists(rutaDatosLogin):
        credenciales = {}
        codigo = 1
        usuario = "admin"
        contraDefecto = incriptar("SISGESA")

        usuacredencial = {}
        usuacredencial["usuario"] = usuario
        usuacredencial["contrasena"] = contraDefecto

        credenciales[codigo] = usuacredencial

        with open(rutaDatosLogin, "w") as file:
            json.dump(credenciales, file)
        return credenciales
    else:
        # Si el archivo existe, cargamos la contraseña
        with open(rutaDatosLogin, "r") as file:
            try:
                return json.load(file)  # Esto debería devolver un diccionario
            except json.JSONDecodeError:
                print("Error al leer el archivo JSON.")
                return {}
        
        
            