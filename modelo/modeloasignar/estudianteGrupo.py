import json
import os

def asignarEstudianteGrupo(codEstudiante, codGrupo):
    # Cargar rutas de los archivos
    rutaEstudiantes = 'datos/estudiantes.json'
    rutaGrupos = 'datos/grupos.json'
    
    # Verificar si los archivos existen
    if not os.path.exists(rutaEstudiantes):
        print("No hay estudiantes registrados.")
        return
    
    if not os.path.exists(rutaGrupos):
        print("No hay grupos registrados.")
        return
    
    # Cargar datos de los archivos JSON
    with open(rutaEstudiantes, 'r') as file:
        estudiantes = json.load(file)
        
    with open(rutaGrupos, 'r') as file:
        grupos = json.load(file)
    
    # Buscar estudiante por código
    estudiante = next((est for est in estudiantes if est['codigo'] == codEstudiante), None)
    if not estudiante:
        print(f"Estudiante con código {codEstudiante} no encontrado.")
        return
    
    # Buscar grupo por código
    grupoNuevo = next((gru for gru in grupos if gru['codigo'] == codGrupo), None)
    if not grupoNuevo:
        print(f"Grupo con código {codGrupo} no encontrado.")
        return
    
    # Verificar si el estudiante ya está asignado a algún grupo
    grupoAnteriorCodigo = estudiante.get('grupo')
    if grupoAnteriorCodigo:
        if grupoAnteriorCodigo == codGrupo:
            print(f"El estudiante {estudiante['nombre']} ya está asignado al grupo {codGrupo}.")
            return
        
        # Preguntar si desean cambiar al estudiante de grupo
        confirmacion = input(f"El estudiante {estudiante['nombre']} ya está asignado al grupo {grupoAnteriorCodigo}. ¿Deseas cambiarlo al grupo {codGrupo}? (s/n): ").strip().lower()
        if confirmacion != 's':
            print("No se realizó ningún cambio.")
            return
        
        # Si el estudiante estaba asignado a un grupo anterior, removerlo de ese grupo
        grupoAnterior = next((gru for gru in grupos if gru['codigo'] == grupoAnteriorCodigo), None)
        if grupoAnterior and "estudiantes" in grupoAnterior:
            grupoAnterior['estudiantes'].remove(codEstudiante)
            print(f"El estudiante {codEstudiante} ha sido removido del grupo {grupoAnteriorCodigo}.")
    
    # Asignar estudiante al nuevo grupo
    estudiante['grupo'] = codGrupo
    if "estudiantes" not in grupoNuevo:
        grupoNuevo["estudiantes"] = []
    
    grupoNuevo["estudiantes"].append(codEstudiante)

    # Actualizar el registro del estudiante en la lista
    for idx, est in enumerate(estudiantes):
        if est['codigo'] == codEstudiante:
            estudiantes[idx] = estudiante
            break

    # Actualizar el registro de los grupos
    for idx, gru in enumerate(grupos):
        if gru['codigo'] == grupoNuevo['codigo']:
            grupos[idx] = grupoNuevo
        elif gru['codigo'] == grupoAnteriorCodigo:
            grupos[idx] = grupoAnterior

    # Sobrescribir los archivos JSON con las listas completas actualizadas
    with open(rutaEstudiantes, 'w') as file:
        json.dump(estudiantes, file, indent=4)
        
    with open(rutaGrupos, 'w') as file:
        json.dump(grupos, file, indent=4)

    print(f"Estudiante {estudiante['nombre']} asignado al grupo {codGrupo} exitosamente.")




    
    
    
    
    
    
    
