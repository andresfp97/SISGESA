from persistencia.persisProfesor.perProfesor import guardarProfesor
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
    guardarProfesor(profesor)
    print(f"Profesor '{nombre}' registrado exitosamente.")
   