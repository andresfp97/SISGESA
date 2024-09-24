import json
import os

def asignarEstudianteModulo(codEstudiante, codModulo):
    # Cargar rutas de los archivos
    rutaEstudiantes = 'datos/estudiantes.json'
    rutaModulos = 'datos/modulos.json'
    
    # Verificar si los archivos existen
    if not os.path.exists(rutaEstudiantes):
        print("No hay estudiantes registrados.")
        return
    
    if not os.path.exists(rutaModulos):
        print("No hay módulos registrados.")
        return
    
    # Cargar datos de los archivos JSON
    with open(rutaEstudiantes, 'r') as file:
        estudiantes = json.load(file)
        
    with open(rutaModulos, 'r') as file:
        modulos = json.load(file)
    
    # Buscar estudiante por código
    estudiante = next((est for est in estudiantes if est['codigo'] == codEstudiante), None)
    if not estudiante:
        print(f"Estudiante con código {codEstudiante} no encontrado.")
        return
    
    # Buscar módulo por código
    moduloNuevo = next((mod for mod in modulos if mod['codigo'] == codModulo), None)
    if not moduloNuevo:
        print(f"Módulo con código {codModulo} no encontrado.")
        return
    
    # Verificar si el estudiante ya tiene una lista de módulos, si no, crearla
    if 'modulos' not in estudiante:
        estudiante['modulos'] = []
    
    # Verificar si el estudiante ya está asignado al mismo módulo (a nivel de estudiante)
    if codModulo in estudiante['modulos']:
        print(f"El estudiante {estudiante['nombre']} ya está asignado al módulo {codModulo}.")
        return
    
    # Verificar si el estudiante ya está asignado al mismo módulo (a nivel de módulo)
    if 'estudiantes' in moduloNuevo and codEstudiante in moduloNuevo['estudiantes']:
        print(f"El estudiante con código {codEstudiante} ya está registrado en el módulo {codModulo}.")
        return

    # Verificar si el estudiante tiene menos de 3 módulos
    if len(estudiante['modulos']) >= 3:
        print(f"El estudiante {estudiante['nombre']} ya está inscrito en 3 módulos. No puede inscribirse en más.")
        return
    
    # Asignar estudiante al nuevo módulo y agregar el módulo a la lista del estudiante
    estudiante['modulos'].append(codModulo)
    if "estudiantes" not in moduloNuevo:
        moduloNuevo["estudiantes"] = []
    
    moduloNuevo["estudiantes"].append(codEstudiante)

    # Actualizar el registro del estudiante en la lista
    for idx, est in enumerate(estudiantes):
        if est['codigo'] == codEstudiante:
            estudiantes[idx] = estudiante  # Actualizamos el estudiante en la lista con el nuevo módulo agregado
            break

    # Actualizar el registro de los módulos
    for idx, mod in enumerate(modulos):
        if mod['codigo'] == moduloNuevo['codigo']:
            modulos[idx] = moduloNuevo  # Actualizamos el módulo con el estudiante agregado

    # Sobrescribir los archivos JSON con las listas completas actualizadas
    with open(rutaEstudiantes, 'w') as file:
        json.dump(estudiantes, file, indent=4)
        
    with open(rutaModulos, 'w') as file:
        json.dump(modulos, file, indent=4)

    print(f"Estudiante {estudiante['nombre']} asignado al módulo {codModulo} exitosamente.")
