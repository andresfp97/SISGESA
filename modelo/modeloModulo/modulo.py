from persistencia.persisModulo.perModulo import guardarModulo
from utils.validacion import leerUsuario, leerCodigo

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

    modulo = {
        'codigo': codigo,
        'nombre': nombre,
        'duracionSemanas': duraSemanas
    }

    # Guardar grupo
    guardarModulo(modulo)
    print(f"Modulo  '{nombre}' registrado exitosamente.")
    input("Enter para volver al menu :)")