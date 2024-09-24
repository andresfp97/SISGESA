from datetime import datetime, timedelta
from persistencia.persistenciaEntidades.perEstudiante import obtenerEstudiantes
from persistencia.persistenciaEntidades.perModulo import obtenerModulos
from persistencia.persisAsistencia.perAsistencia import cargar_asistencia, guardar_asistencia


# Función para validar si un estudiante está registrado
def estudiante_valido(codigo_estudiante):
    estudiantes = obtenerEstudiantes()
    return any(est['codigo'] == codigo_estudiante for est in estudiantes)

# Función para validar si un módulo está registrado
def modulo_valido(codigo_modulo):
    modulos = obtenerModulos()
    return any(mod['codigo'] == codigo_modulo for mod in modulos)

# Función para registrar asistencia de varios estudiantes en un mismo módulo
def tomarAsistencia():
    # Ingresar el módulo solo una vez
    codigo_modulo = input("Ingrese el código del módulo: ")
    
    # Obtener la fecha actual
    fecha_actual = datetime.now().strftime('%Y-%m-%d')
    
    # Cargar asistencias existentes
    asistencias = cargar_asistencia()

    # Verificar si ya se ha registrado asistencia para este módulo y fecha
    if codigo_modulo in asistencias and fecha_actual in asistencias[codigo_modulo]:
        print(f"Ya se ha registrado asistencia para el módulo {codigo_modulo} en la fecha {fecha_actual}.")
        return  # Termina la función sin permitir nuevo registro

    # Crear la estructura del módulo y fecha si no existe
    if codigo_modulo not in asistencias:
        asistencias[codigo_modulo] = {}
    if fecha_actual not in asistencias[codigo_modulo]:
        asistencias[codigo_modulo][fecha_actual] = []

    hora_inicio = datetime.now()
    print(f"Hora de inicio del módulo {codigo_modulo}: {hora_inicio.strftime('%Y-%m-%d %H:%M:%S')}")
    
    while True:
        codigo_estudiante = input("Ingrese el código del estudiante (o 'fin' para terminar): ").strip()
        
        if codigo_estudiante.lower() == 'fin':
            break

        # Validación de estudiante
        if not estudiante_valido(codigo_estudiante):
            print(f"Estudiante con código {codigo_estudiante} no encontrado.")
            continue

        # Registrar la asistencia
        hora_llegada = datetime.now()
        diferencia = hora_llegada - hora_inicio
        
        # Determinar estado (temprano o tarde)
        estado = "temprano" if diferencia <= timedelta(minutes=5) else "tarde"

        nueva_asistencia = {
            'codigo_estudiante': codigo_estudiante,
            'entrada': hora_llegada.strftime('%Y-%m-%d %H:%M:%S'),
            'salida': None,
            'estado': estado,
            'estado_salida': None  # El estado de salida se asignará más tarde
        }

        # Agregar la asistencia al registro del módulo y fecha
        asistencias[codigo_modulo][fecha_actual].append(nueva_asistencia)

        # Confirmar registro
        print(f"Asistencia registrada para {codigo_estudiante}: {estado}. Hora de llegada: {hora_llegada.strftime('%Y-%m-%d %H:%M:%S')}.")

    # Guardar todas las asistencias
    guardar_asistencia(asistencias)
    print(f"Asistencia completada para el módulo {codigo_modulo} en la fecha {fecha_actual}.")


    
def tomarSalida():
    # Ingresar el módulo solo una vez
    codigo_modulo = input("Ingrese el código del módulo para registrar salidas: ")

    # Obtener la fecha actual
    fecha_actual = datetime.now().strftime('%Y-%m-%d')

    # Cargar asistencias existentes
    asistencias = cargar_asistencia()

    # Verificar si ya existe alguna salida registrada para el módulo en la fecha actual
    if codigo_modulo in asistencias and fecha_actual in asistencias[codigo_modulo]:
        # Verificar si alguna salida ya ha sido registrada para cualquier estudiante
        any_salida_registrada = any(asistencia['salida'] is not None for asistencia in asistencias[codigo_modulo][fecha_actual])
        if any_salida_registrada:
            print(f"Ya se ha registrado una salida para el módulo {codigo_modulo} en la fecha {fecha_actual}. No se puede volver a registrar.")
            return  # Termina la función sin permitir nuevo registro de salidas

    # Si ninguna salida ha sido registrada, proceder con la toma de salidas
    while True:
        codigo_estudiante = input("Ingrese el código del estudiante (o 'fin' para terminar): ").strip()

        if codigo_estudiante.lower() == 'fin':
            break

        # Buscar el registro de asistencia del estudiante sin salida
        asistencia_encontrada = None
        for asistencia in asistencias[codigo_modulo][fecha_actual]:
            if asistencia['codigo_estudiante'] == codigo_estudiante and asistencia['salida'] is None:
                asistencia_encontrada = asistencia
                break

        if asistencia_encontrada is None:
            print(f"No se encontró un registro de entrada pendiente para el estudiante {codigo_estudiante} en el módulo {codigo_modulo}.")
            continue

        # Registrar la salida
        hora_salida = datetime.now()
        asistencia_encontrada['salida'] = hora_salida.strftime('%Y-%m-%d %H:%M:%S')

        # Estado de salida siempre será "bien" aquí
        asistencia_encontrada['estado_salida'] = 'bien'

        # Confirmar registro
        print(f"Salida registrada para {codigo_estudiante}: Estado de salida - bien. Hora de salida: {hora_salida.strftime('%Y-%m-%d %H:%M:%S')}.")

    # Guardar todas las asistencias
    guardar_asistencia(asistencias)

    print(f"Registro de salidas completado para el módulo {codigo_modulo} en la fecha {fecha_actual}.")




def actualizar_salidas_pendientes():
    # Cargar asistencias existentes
    asistencias = cargar_asistencia()

    for modulo, fechas in asistencias.items():
        for fecha, registros in fechas.items():
            for asistencia in registros:
                # Si la salida sigue siendo None, asignar estado "antes"
                if asistencia['salida'] is None:
                    asistencia['estado_salida'] = 'antes'

    # Guardar los cambios
    guardar_asistencia(asistencias)
    print("Salidas pendientes actualizadas correctamente.")
