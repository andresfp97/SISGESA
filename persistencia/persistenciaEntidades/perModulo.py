import json
import os
rutaDatosGrupos = "datos\\modulos.json"
def guardarModulo(modulo):
    
    # Verifica si el archivo ya existe
    if os.path.exists(rutaDatosGrupos):
        with open(rutaDatosGrupos, 'r') as file:
            datos = json.load(file)
    else:
        datos = []

    # Agregar nuevo modulo
    datos.append(modulo)

    # Guardar los datos actualizados
    with open(rutaDatosGrupos, 'w') as file:
        json.dump(datos, file, indent=4)

def obtenerModulos():
    if os.path.exists(rutaDatosGrupos):
        with open(rutaDatosGrupos, 'r') as file:
            return json.load(file)
    return []