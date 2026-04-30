from datetime import datetime
fecha = input('Ingrese su fecha de nacimiento (año-mes-Dia): ')

fechanac = datetime.strptime(fecha, "%Y-%m-%d")

hoy = datetime.now()

diferencia = hoy - fechanac

diastotales = diferencia.days

anios = diastotales // 365
meses = (diastotales % 365) // 30
dias = (diastotales % 365) % 30

timestamp = int(fechanac.timestamp())

print('Días totales:', diastotales)
print('Edad: ', anios, 'años,', meses, 'meses y', dias, 'días')
print('Timestamp: ', timestamp)