""" Build a small airport database.

Requirements:

Store at least 10 ICAO airport codes.
Ask the user to enter an ICAO code.
Print the airport name.
If the code doesn't exist, print:
Airport not found.
"""
airport_database = {
    'SABE': 'Buenos Aires - Aeroparque Jorge Newbery',
    'SAEZ': 'Buenos Aires - Ministro Pistarini (Ezeiza)',
    'SADF': 'San Fernando',
    'SADM': 'Morón',
    'SADP': 'El Palomar',
    'SACO': 'Córdoba - Ingeniero Taravella',
    'SAME': 'Mendoza - El Plumerillo',
    'SAAR': 'Rosario - Islas Malvinas',
    'SAAV': 'Santa Fe - Sauce Viejo',
    'SAAP': 'Paraná - General Justo José de Urquiza',
    'SAZS': 'San Carlos de Bariloche',
    'SAZN': 'Neuquén - Presidente Perón',
    'SAWG': 'Río Gallegos - Piloto Civil Norberto Fernández',
    'SAWH': 'Ushuaia - Malvinas Argentinas',
    'SAWE': 'Río Grande',
    'SASA': 'Salta - Martín Miguel de Güemes',
    'SANT': 'Tucumán - Teniente Benjamín Matienzo',
    'SARE': 'Resistencia',
    'SARC': 'Corrientes',
    'SARF': 'Formosa',
    'SARI': 'Puerto Iguazú - Cataratas del Iguazú',
    'SAVC': 'Comodoro Rivadavia',
    'SAVT': 'Trelew',
    'SAVY': 'El Tehuelche - Puerto Madryn',
    'SAZY': 'San Martín de los Andes - Chapelco',
    'SAZM': 'Mar del Plata - Astor Piazzolla',
    'SAZB': 'Bahía Blanca - Comandante Espora',
    'SAOC': 'Río Cuarto',
    'SAOU': 'San Luis',
    'SAOR': 'Villa Reynolds',
    'SAAC': 'Concordia',
    'SAZR': 'Santa Rosa',
    'SAZA': 'Azul',
    'SAVR': 'Alto Río Senguer',
    'SAWR': 'Gobernador Gregores'
}

get_code = input('Enter an ICAO code: ').upper()

if get_code in airport_database:
    print(airport_database[get_code])
else:
    print('Airport not found')


""" Pythonic way
airport = airport_database.get(get_code)

if airport:
    print(airport)
else:
    print("Airport not found.")


Este ejercicio ya muestra que empezás a manejar una estructura de datos nueva (dict). Es un paso importante.

El siguiente desafío que te daría sería agregar un menú como este:

===== Airport Database =====
1 - Search airport
2 - Show all airports
0 - Exit

Y cuando el usuario elija 2, mostrar algo como:

SADF - San Fernando
SADM - Morón
SABE - Aeroparque
...

Ese ejercicio te va a obligar a aprender a recorrer un diccionario, que es el siguiente paso natural después de saber buscar por clave.
Un desafío extra (sin decirte cómo hacerlo)

Cuando termines el menú, agregale estas opciones:

===== AIRPORT DATABASE =====

1 - Search airport by ICAO
2 - Show all airports
3 - Add a new airport
4 - Delete an airport
5 - Count airports
0 - Exit

Con ese solo programa vas a practicar:

✅ Diccionarios (dict)
✅ if
✅ while
✅ for
✅ Funciones
✅ Menús
✅ Validación de datos
✅ Agregar elementos a un diccionario
✅ Eliminar elementos de un diccionario
✅ Recorrer un diccionario

Ese proyecto ya se parece bastante a un programa real de consola y es un excelente ejercicio antes de pasar a temas más avanzados como archivos o APIs.
"""
