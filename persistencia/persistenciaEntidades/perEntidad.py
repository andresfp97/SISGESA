import json
import os

def guardarDatos(entidad, nombre):
    ruta = f"datos\\{nombre}.json"
    
    # Verifica si el archivo ya existe
    if os.path.exists(ruta):
        with open(ruta, 'r') as file:
            datos = json.load(file)
    else:
        datos = []

    # Verificar si el código de la entidad ya existe en los datos
    if not any(d["codigo"] == entidad["codigo"] for d in datos):
        datos.append(entidad)
        print("="*45)
        print(f"'{entidad["nombre"]}' registrado exitosamente en {nombre}.")
        print("="*45)
        
    else:
        print("="*45)
        print(f"{entidad["codigo"]} ya  existe en {nombre}")
        print("="*45)

    # Guardar los datos actualizados
    with open(ruta, 'w') as file:
        json.dump(datos, file, indent=4)
        
def obtenerDatos(nombre):
    ruta = f"datos\\{nombre}.json"
    
    if os.path.exists(ruta):
        with open(ruta, 'r') as file:
            return json.load(file)
    return []
