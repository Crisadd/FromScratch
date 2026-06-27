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
def get_code():
    icao_code = input('Enter an ICAO code: ').upper()

    return icao_code

def searching_code(code):
    if code in airport_database:
        print(f'Code {code} is {airport_database[code]}')
    else:
        print('Airport not found.')

def main():
    quantity_of_searches = 0
    while True:
        print('========= MENU =========')
        print('1 - Search airport')
        print('2 - Show all airports')
        print('0 - Exit')
        option = int(input('Option: '))

        if option == 1:
            while True:
                icao_code = get_code()
                searching_code(icao_code)
                quantity_of_searches +=1

                answer = input('Would you like to continue searching? y/n: ')
            
                while answer not in ('y','n'):
                    answer = input('Would you like to continue searching? y/n: ')

                if answer != 'y':
                    print(f'You have done {quantity_of_searches} search/es.\nGoodbye')
                    break
        
        else:
            print('Thank you for using this program.')
            break

if __name__ == "__main__":
    main()


""" Pythonic way
airport = airport_database.get(get_code)
if airport:
    print(airport)
else:
    print("Airport not found.")


Ideas mias: 
imprimir todos los aeropuertos que busco, eso es ponerlo en una lista. 
                                            Imprmir cuantas busquedas realizo

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
