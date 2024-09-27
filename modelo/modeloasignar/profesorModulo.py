import json
import os

def asignarProfesorModulo(codProfesor, codModulo):
    # Cargar rutas de los archivos
    rutaProfesores = 'datos/profesores.json'
    rutaModulos = 'datos/modulos.json'
    
    # Verificar si los archivos existen
    if not os.path.exists(rutaProfesores):
        print("No hay profesores registrados.")
        return
    
    if not os.path.exists(rutaModulos):
        print("No hay módulos registrados.")
        return
    
    # Cargar datos de los archivos JSON
    with open(rutaProfesores, 'r') as file:
        profesores = json.load(file)
        
    with open(rutaModulos, 'r') as file:
        modulos = json.load(file)
    
    # Buscar profesor por código
    profesor = next((est for est in profesores if est['codigo'] == codProfesor), None)
    if not profesor:
        print(f"Profesor con código {codProfesor} no encontrado.")
        return
    
    # Buscar módulo por código
    moduloNuevo = next((mod for mod in modulos if mod['codigo'] == codModulo), None)
    if not moduloNuevo:
        print(f"Módulo con código {codModulo} no encontrado.")
        return
    
    # Verificar si el profesor ya tiene una lista de módulos, si no, crearla
    if 'modulos' not in profesor:
        profesor['modulos'] = []
    
    # Verificar si el profesor ya está asignado al mismo módulo (a nivel de profesor)
    if codModulo in profesor['modulos']:
        print(f"El profesor {profesor['nombre']} ya está asignado al módulo {codModulo}.")
        return
    
    # Verificar si el profesor ya está asignado al mismo módulo (a nivel de módulo)
    if 'profesores' in moduloNuevo and codProfesor in moduloNuevo['profesores']:
        print(f"El profesor con código {codProfesor} ya está registrado en el módulo {codModulo}.")
        return

    # Verificar si el profesor tiene menos de 3 módulos
    if len(profesor['modulos']) >= 3:
        print(f"El profesor {profesor['nombre']} ya está inscrito en 3 módulos. No puede inscribirse en más.")
        return
    
    # Asignar profesor al nuevo módulo y agregar el módulo a la lista del profesor
    profesor['modulos'].append(codModulo)
    if "profesores" not in moduloNuevo:
        moduloNuevo["profesores"] = []
    
    moduloNuevo["profesores"].append(codProfesor)

    # Actualizar el registro del profesor en la lista
    for idx, est in enumerate(profesores):
        if est['codigo'] == codProfesor:
            profesores[idx] = profesor  # Actualizamos el profesor en la lista con el nuevo módulo agregado
            break

    # Actualizar el registro de los módulos
    for idx, mod in enumerate(modulos):
        if mod['codigo'] == moduloNuevo['codigo']:
            modulos[idx] = moduloNuevo  # Actualizamos el módulo con el profesor agregado

    # Sobrescribir los archivos JSON con las listas completas actualizadas
    with open(rutaProfesores, 'w') as file:
        json.dump(profesores, file, indent=4)
        
    with open(rutaModulos, 'w') as file:
        json.dump(modulos, file, indent=4)

    print(f"profesor {profesor['nombre']} asignado al módulo {codModulo} exitosamente.")
