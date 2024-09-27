from persistencia.persistenciaEntidades.perEntidad import guardarDatos
from utils.validacion import leerUsuario, leerCodigo, leerEdad, leerSexo

def registrarEstudiante():
    
    print("=== Registro de Estudiantes ===")
    
    codigo = leerCodigo()
    nombre = leerUsuario()
    sexo = leerSexo()
    edad = leerEdad()

    estudiante  = {
        
        'codigo': codigo,
        'nombre': nombre,
        'sexo': sexo,
        'edad': edad,
        'grupo': None,
        'modulos': []
        
    }
    
    # Guardar estudiante
    guardarDatos(estudiante, "estudiantes" )
    