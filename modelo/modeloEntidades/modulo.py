from persistencia.persistenciaEntidades.perModulo import guardarModulo
from utils.validacion import leerUsuario, leerCodigo
from persistencia.persistenciaEntidades.perProfesor import obtenerProfesor
from modelo.modeloEntidades.profesor import registrarProfesor

def leerDuracionSemanas():
    while True:
        try:
            cant = int(input("Duracion de semanas: "))
            if cant < 0:
                print(">>> Error. en duracion")
                continue
            return cant

        except ValueError:
            print("Error. duracion invalido.\n")

def registrarModulo():
    
    print("=== Registro de Modulo ===")
    codigo = leerCodigo()
    nombre = leerUsuario()
    duraSemanas = leerDuracionSemanas()
    
    parar = True
    lst = []
    while parar:
        profesor = registrarProfesor()
        lst.append(profesor)
        otro = input("¿quiere asignar otro profesor ? (s/n): ").strip().lower()
        if otro == "s":
            parar = True
        if otro == "n":
             parar = False
    modulo = {
        'codigo': codigo,
        'nombre': nombre,
        'duracionSemanas': duraSemanas,
        'estudiantes': [],
        'profesores': lst    
    }

    # Guardar modulo
    guardarModulo(modulo)
    print(f"Modulo  '{nombre}' registrado exitosamente.")