from persistencia.persisGrupo.perGrupo import guardarGrupo
from utils.validacion import leerUsuario, leerCodigo

def leerMarca():
    while True:
        try:
            nombre = input("Ingrese la marca del grupo?: ").strip()
            
            if len(nombre) == 0:
                print(">>> ERROR. marca invalida")
                continue
            return nombre

        except Exception as e:
            print("Error al ingresar la marca.\n" + e)


def registrarGrupo():
    
    print("=== Registro de Grupo ===")
    codigo = leerCodigo()
    nombre = leerUsuario()
    marca = leerMarca()

    grupo = {
        'codigo': codigo,
        'nombre': nombre,
        'marca': marca,
        "estudiantes": []
    }

    # Guardar grupo
    guardarGrupo(grupo)
    print(f"Grupo '{nombre}' registrado exitosamente.")