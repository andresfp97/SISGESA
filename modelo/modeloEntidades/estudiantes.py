from persistencia.persistenciaEntidades.perEstudiante import guardarEstudiante
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
    guardarEstudiante(estudiante)
    print(f"Estudiante '{nombre}' registrado exitosamente.")