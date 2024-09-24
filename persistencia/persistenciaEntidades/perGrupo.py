import json
import os
rutaDatosGrupos = "datos\\grupos.json"

def guardarGrupo(grupo):
    
    # Verifica si el archivo ya existe
    if os.path.exists(rutaDatosGrupos):
        with open(rutaDatosGrupos, 'r') as file:
            datos = json.load(file)
    else:
        datos = []

    # Agregar nuevo grupo
    datos.append(grupo)

    # Guardar los datos actualizados
    with open(rutaDatosGrupos, 'w') as file:
        json.dump(datos, file, indent=4)

def obtener_grupos():
    if os.path.exists(rutaDatosGrupos):
        with open(rutaDatosGrupos, 'r') as file:
            return json.load(file)
    return []