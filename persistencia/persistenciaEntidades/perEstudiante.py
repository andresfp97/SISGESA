import json
import os
rutaDatosEstudiantes = "datos\\estudiantes.json"

def guardarEstudiante(estudiante):
    
    # Verifica si el archivo ya existe
    if os.path.exists(rutaDatosEstudiantes):
        with open(rutaDatosEstudiantes, 'r') as file:
            datos = json.load(file)
    else:
        datos = []

    # Agregar nuevo estudiante
    datos.append(estudiante)

    # Guardar los datos actualizados
    with open(rutaDatosEstudiantes, 'w') as file:
        json.dump(datos, file, indent=4)

def obtenerEstudiantes():
    if os.path.exists(rutaDatosEstudiantes):
        with open(rutaDatosEstudiantes, 'r') as file:
            return json.load(file)
    return []