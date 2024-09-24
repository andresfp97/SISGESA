import json
import os

rutaDatosAsistencia = 'datos/asistencia.json'

# Función para guardar los registros de asistencia
def guardar_asistencia(asistencias):
    with open(rutaDatosAsistencia, 'w') as file:
        json.dump(asistencias, file, indent=4)
 # Función para cargar los registros de asistencia       
def cargar_asistencia():
    if os.path.exists(rutaDatosAsistencia):
        try:
            with open(rutaDatosAsistencia, 'r') as file:
                return json.load(file)
        except json.JSONDecodeError:
            # Si el archivo está vacío o corrupto, inicializar como un diccionario vacío
            print("El archivo de asistencia está vacío o tiene un formato incorrecto. Inicializando...")
            return {}
    return {} 