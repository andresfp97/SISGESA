import json
import os
rutaDatosProfesor = "datos\\profesor.json"

def guardarProfesor(profesor):
    
    # Verifica si el archivo ya existe
    if os.path.exists(rutaDatosProfesor):
        with open(rutaDatosProfesor, 'r') as file:
            datos = json.load(file)
    else:
        datos = []

    # Agregar nuevo estudiante
    datos.append(profesor)

    # Guardar los datos actualizados
    with open(rutaDatosProfesor, 'w') as file:
        json.dump(datos, file, indent=4)

def obtenerProfesor():
    if os.path.exists(rutaDatosProfesor):
        with open(rutaDatosProfesor, 'r') as file:
            return json.load(file)
    return []