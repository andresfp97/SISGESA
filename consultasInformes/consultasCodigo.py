
import json
import os

# Consultar los estudiantes matriculados en un grupo

def consultarEstudiantesEnGrupo(codGrupo):
    try:
        # Ruta del archivo de grupos
        rutaGrupos = 'datos/grupos.json'
        
        if not os.path.exists(rutaGrupos):
            raise FileNotFoundError("No hay grupos registrados.")
        
        with open(rutaGrupos, 'r') as file:
            grupos = json.load(file)
        
        # Buscar grupo por código
        grupo = next((gru for gru in grupos if gru['codigo'] == codGrupo), None)
        if not grupo:
            print(f"Grupo con código {codGrupo} no encontrado.")
            return
        
        # Mostrar los estudiantes matriculados en el grupo
        estudiantes = grupo.get('estudiantes', [])
        if estudiantes:
            print(f"Estudiantes matriculados en el grupo {codGrupo}: {estudiantes}")
        else:
            print(f"No hay estudiantes matriculados en el grupo {codGrupo}.")
    
    except FileNotFoundError as e:
        print(e)
    except json.JSONDecodeError:
        print("Error al leer los datos del archivo. El archivo JSON está corrupto o malformado.")
    except Exception as e:
        print(f"Ha ocurrido un error inesperado: {e}")


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
            return
        
        # Mostrar los estudiantes inscritos en el módulo
        estudiantes = modulo.get('estudiantes', [])
        if estudiantes:
            print(f"Estudiantes inscritos en el módulo {codModulo}: {estudiantes}")
        else:
            print(f"No hay estudiantes inscritos en el módulo {codModulo}.")
    
    except FileNotFoundError as e:
        print(e)
    except json.JSONDecodeError:
        print("Error al leer los datos del archivo. El archivo JSON está corrupto o malformado.")
    except Exception as e:
        print(f"Ha ocurrido un error inesperado: {e}")
        
# Consultar los docentes que imparten un módulo        
def consultarDocentesEnModulo(codModulo):
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
            return
        
        # Mostrar los docentes asignados al módulo
        docentes = modulo.get('docentes', [])
        if docentes:
            print(f"Docentes que imparten el módulo {codModulo}: {docentes}")
        else:
            print(f"No hay docentes asignados al módulo {codModulo}.")
    
    except FileNotFoundError as e:
        print(e)
    except json.JSONDecodeError:
        print("Error al leer los datos del archivo. El archivo JSON está corrupto o malformado.")
    except Exception as e:
        print(f"Ha ocurrido un error inesperado: {e}")


# Consultar los estudiantes a cargo de un docente en un módulo

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
            return
        
        # Verificar si el docente está asignado al módulo
        if codDocente not in modulo.get('docentes', []):
            print(f"El docente con código {codDocente} no imparte el módulo {codModulo}.")
            return
        
        # Mostrar los estudiantes del módulo asignados a ese docente
        estudiantes = modulo.get('estudiantes', [])
        if estudiantes:
            print(f"Estudiantes a cargo del docente {codDocente} en el módulo {codModulo}: {estudiantes}")
        else:
            print(f"No hay estudiantes inscritos en el módulo {codModulo}.")
    
    except FileNotFoundError as e:
        print(e)
    except json.JSONDecodeError:
        print("Error al leer los datos del archivo. El archivo JSON está corrupto o malformado.")
    except Exception as e:
        print(f"Ha ocurrido un error inesperado: {e}")

