from persistencia.persistenciaEntidades.perEntidad import guardarDatos
from utils.validacion import leerUsuario, leerCodigo

def registrarProfesor():
    
    print("=== Registro de Profesores ===")
    print("ingrese la cedula del profesor a registar")
    codigo = leerCodigo()
    nombre = leerUsuario()   
          
    profesor  = {
        'codigo': codigo,
        'nombre': nombre,
    }
        
    # Guardar estudante
    guardarDatos(profesor, "profesores")
    print(f"Profesor '{nombre}' registrado exitosamente.")
    return profesor