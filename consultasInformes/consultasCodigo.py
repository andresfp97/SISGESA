import json
import os

def obtenerDetallesEstudiante(codigo_estudiante):
    # Ruta al archivo donde se encuentran los datos de los estudiantes
    rutaEstudiantes = 'datos/estudiantes.json'
    
    # Verificar si el archivo de estudiantes existe
    if not os.path.exists(rutaEstudiantes):
        print("El archivo de estudiantes no existe.")
        return 'Nombre no encontrado'
    
    try:
        # Leer el archivo JSON de estudiantes
        with open(rutaEstudiantes, 'r') as file:
            estudiantes = json.load(file)
        
        # Buscar el estudiante por código
        estudiante = next((est for est in estudiantes if est['codigo'] == codigo_estudiante), None)
        
        if estudiante:
            return estudiante['nombre']  # Retornar el nombre del estudiante
        else:
            return 'Nombre no encontrado'  # Si no se encuentra el estudiante
    
    except json.JSONDecodeError:
        print("Error al leer el archivo de estudiantes. El archivo está malformado.")
        return 'Nombre no encontrado'
    except Exception as e:
        print(f"Ha ocurrido un error inesperado: {e}")
        return 'Nombre no encontrado'


# Función para consultar los estudiantes en un grupo específico
def consultarEstudiantesEnGrupo(codGrupo):
    try:
        # Ruta del archivo de grupos
        rutaGrupos = 'datos/grupos.json'
        
        if not os.path.exists(rutaGrupos):
            raise FileNotFoundError("No hay grupos registrados.")
        
        # Cargar el archivo de grupos
        with open(rutaGrupos, 'r') as file:
            grupos = json.load(file)
        
        # Buscar grupo por código
        grupo = next((gru for gru in grupos if gru['codigo'] == codGrupo), None)
        if not grupo:
            print(f"Grupo con código {codGrupo} no encontrado.")
            return []
        
        # Obtener los estudiantes matriculados en el grupo
        estudiantes = grupo.get('estudiantes', [])
        
        if estudiantes:
            print(f"Estudiantes matriculados en el grupo {codGrupo}:")
            # Formatear salida numerada y mostrar código y nombre
            for idx, codigo in enumerate(estudiantes, start=1):
                nombre = obtenerDetallesEstudiante(codigo)
                print(f"{idx}. Código: {codigo} - Nombre: {nombre}")
        else:
            print(f"No hay estudiantes matriculados en el grupo {codGrupo}.")
        
        return estudiantes  # Retornar la lista de estudiantes
    
    except FileNotFoundError as e:
        print(e)
        return []  # Retornar lista vacía en caso de error
    except json.JSONDecodeError:
        print("Error al leer los datos del archivo. El archivo JSON está corrupto o malformado.")
        return []  # Retornar lista vacía en caso de error
    except Exception as e:
        print(f"Ha ocurrido un error inesperado: {e}")
        return []  # Retornar lista vacía en caso de error


# Consultar los estudiantes inscritos en un módulo

def consultarEstudiantesEnModulo(codModulo):
    try:
        # Ruta del archivo de módulos
        rutaModulos = 'datos/modulos.json'
        
        if not os.path.exists(rutaModulos):
            raise FileNotFoundError("No hay módulos registrados.")
        
        with open(rutaModulos, 'r') as file:
            modulos = json.load(file)
        
        # Buscar módulo por código
        modulo = next((mod for mod in modulos if mod['codigo'] == codModulo), None)
        if not modulo:
            print(f"Módulo con código {codModulo} no encontrado.")
            return []

        # Obtener los estudiantes inscritos en el módulo
        estudiantes = modulo.get('estudiantes', [])
        
        if estudiantes:
            print(f"Estudiantes inscritos en el módulo {codModulo}:")
            # Formatear salida bonita mostrando código y nombre del estudiante
            for idx, codigo in enumerate(estudiantes, start=1):
                nombre = obtenerDetallesEstudiante(codigo)
                print(f"{idx}. Código: {codigo} - Nombre: {nombre}")
        else:
            print(f"No hay estudiantes inscritos en el módulo {codModulo}.")
        
        return estudiantes  # Retornar la lista de estudiantes
    
    except FileNotFoundError as e:
        print(e)
        return []  # Retornar lista vacía en caso de error
    except json.JSONDecodeError:
        print("Error al leer los datos del archivo. El archivo JSON está corrupto o malformado.")
        return []  # Retornar lista vacía en caso de error
    except Exception as e:
        print(f"Ha ocurrido un error inesperado: {e}")
        return []  # Retornar lista vacía en caso de error


     
# Consultar los docentes que imparten un módulo        
def consultarDocentesEnModulo(codModulo):
    try:
        # Ruta del archivo de módulos
        rutaModulos = 'datos/modulos.json'
        
        if not os.path.exists(rutaModulos):
            raise FileNotFoundError("No hay módulos registrados.")
        
        # Cargar el archivo de módulos
        with open(rutaModulos, 'r') as file:
            modulos = json.load(file)
        
        # Buscar módulo por código
        modulo = next((mod for mod in modulos if mod['codigo'] == codModulo), None)
        if not modulo:
            print(f"Módulo con código {codModulo} no encontrado.")
            return []
        
        # Obtener los docentes asignados al módulo
        docentes = modulo.get('profesores', [])
        
        if docentes:
            print(f"Docentes que imparten el módulo {codModulo}:")
            # Formatear la salida de los docentes
            for idx, docente in enumerate(docentes, start=1):
                print(f"{idx}. Código: {docente['codigo']} - Nombre: {docente['nombre']}")
        else:
            print(f"No hay docentes asignados al módulo {codModulo}.")
        
        return docentes  # Retornar la lista de docentes
    
    except FileNotFoundError as e:
        print(e)
        return []  # Retornar lista vacía en caso de error
    except json.JSONDecodeError:
        print("Error al leer los datos del archivo. El archivo JSON está corrupto o malformado.")
        return []  # Retornar lista vacía en caso de error
    except Exception as e:
        print(f"Ha ocurrido un error inesperado: {e}")
        return []  # Retornar lista vacía en caso de error


# Función para consultar estudiantes asignados a un docente en un módulo específico
def consultarEstudiantesPorDocenteEnModulo(codDocente, codModulo):
    try:
        # Ruta del archivo de módulos
        rutaModulos = 'datos/modulos.json'
        
        if not os.path.exists(rutaModulos):
            raise FileNotFoundError("No hay módulos registrados.")
        
        with open(rutaModulos, 'r') as file:
            modulos = json.load(file)
        
        # Buscar módulo por código
        modulo = next((mod for mod in modulos if mod['codigo'] == codModulo), None)
        if not modulo:
            print(f"Módulo con código {codModulo} no encontrado.")
            return []
        
        # Verificar si el docente está asignado al módulo
        docentes = modulo.get('profesores', [])
        docente_asignado = next((doc for doc in docentes if doc['codigo'] == codDocente), None)
        
        if not docente_asignado:
            print(f"El docente con código {codDocente} no imparte el módulo {codModulo}.")
            return []
        
        # Obtener los estudiantes del módulo
        estudiantes = modulo.get('estudiantes', [])
        
        if estudiantes:
            print(f"Estudiantes a cargo del docente {docente_asignado['nombre']} en el módulo {codModulo}:")
            # Mostrar código y nombre del estudiante
            for idx, codigo in enumerate(estudiantes, start=1):
                nombre = obtenerDetallesEstudiante(codigo)
                print(f"{idx}. Código: {codigo} - Nombre: {nombre}")
        else:
            print(f"No hay estudiantes inscritos en el módulo {codModulo}.")
        
        return estudiantes  # Retornar la lista de estudiantes
    
    except FileNotFoundError as e:
        print(e)
        return []
    except json.JSONDecodeError:
        print("Error al leer los datos del archivo. El archivo JSON está corrupto o malformado.")
        return []
    except Exception as e:
        print(f"Ha ocurrido un error inesperado: {e}")
        return []

