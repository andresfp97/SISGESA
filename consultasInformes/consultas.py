from persistencia.persisAsistencia.perAsistencia import cargar_asistencia
from datetime import datetime
#  Estudiantes que llegaron tarde a un módulo en un mes específico

def estudiantes_tarde_mes(codigo_modulo, mes, anio):
    try:
        asistencias = cargar_asistencia()
        estudiantes_tarde = []

        if codigo_modulo in asistencias:
            for fecha, registros in asistencias[codigo_modulo].items():
                fecha_entrada = datetime.strptime(fecha, '%Y-%m-%d')
                if fecha_entrada.month == mes and fecha_entrada.year == anio:
                    for asistencia in registros:
                        if asistencia['estado'] == 'tarde':
                            estudiantes_tarde.append(asistencia['codigo_estudiante'])

        if estudiantes_tarde:
            print(f"Estudiantes que llegaron tarde en el módulo {codigo_modulo} en {mes}/{anio}: {estudiantes_tarde}")
        else:
            print(f"No hubo estudiantes que llegaran tarde en el módulo {codigo_modulo} en {mes}/{anio}.")

        return estudiantes_tarde
    except Exception as e:
        print(f"Error al generar el informe de estudiantes tarde: {str(e)}")



# Estudiantes que se retiraron antes de la finalización de una sesión en un mes específico:

def estudiantes_retiro_antes_mes(codigo_modulo, mes, anio):
    try:
        asistencias = cargar_asistencia()
        estudiantes_retiro_antes = []

        if codigo_modulo in asistencias:
            for fecha, registros in asistencias[codigo_modulo].items():
                fecha_entrada = datetime.strptime(fecha, '%Y-%m-%d')
                if fecha_entrada.month == mes and fecha_entrada.year == anio:
                    for asistencia in registros:
                        if asistencia['estado_salida'] == 'antes':
                            estudiantes_retiro_antes.append(asistencia['codigo_estudiante'])

        if estudiantes_retiro_antes:
            print(f"Estudiantes que se retiraron antes en el módulo {codigo_modulo} en {mes}/{anio}: {estudiantes_retiro_antes}")
        else:
            print(f"No hubo estudiantes que se retiraran antes en el módulo {codigo_modulo} en {mes}/{anio}.")

        return estudiantes_retiro_antes
    except Exception as e:
        print(f"Error al generar el informe de retiros anticipados: {str(e)}")

#Estudiantes que no han faltado a ningún módulo durante un mes
def estudiantes_asistencia_completa_mes(mes, anio):
    try:
        asistencias = cargar_asistencia()
        estudiantes_completos = set()

        for modulo, fechas in asistencias.items():
            for fecha, registros in fechas.items():
                fecha_entrada = datetime.strptime(fecha, '%Y-%m-%d')
                if fecha_entrada.month == mes and fecha_entrada.year == anio:
                    for asistencia in registros:
                        if asistencia['estado'] == 'temprano' or asistencia['estado'] == 'tarde':
                            estudiantes_completos.add(asistencia['codigo_estudiante'])

        if estudiantes_completos:
            print(f"Estudiantes que no faltaron a ningún módulo en {mes}/{anio}: {list(estudiantes_completos)}")
        else:
            print(f"No hay estudiantes con asistencia completa en {mes}/{anio}.")

        return list(estudiantes_completos)
    except Exception as e:
        print(f"Error al generar el informe de asistencia completa: {str(e)}")


#Porcentaje de asistencia por módulo

def porcentaje_asistencia_modulo(codigo_modulo, mes, anio):
    try:
        asistencias = cargar_asistencia()
        total_estudiantes = 0
        estudiantes_presentes = 0

        if codigo_modulo in asistencias:
            for fecha, registros in asistencias[codigo_modulo].items():
                fecha_entrada = datetime.strptime(fecha, '%Y-%m-%d')
                if fecha_entrada.month == mes and fecha_entrada.year == anio:
                    total_estudiantes += len(registros)
                    estudiantes_presentes += sum(1 for asistencia in registros if asistencia['estado'] in ['temprano', 'tarde'])

        if total_estudiantes == 0:
            porcentaje_asistencia = 0
        else:
            porcentaje_asistencia = (estudiantes_presentes / total_estudiantes) * 100

        print(f"Porcentaje de asistencia en el módulo {codigo_modulo} en {mes}/{anio}: {porcentaje_asistencia:.2f}%")
        return porcentaje_asistencia
    except Exception as e:
        print(f"Error al generar el informe de porcentaje de asistencia: {str(e)}")


