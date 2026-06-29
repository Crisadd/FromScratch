"""Use a simplified METAR.
Example input:

METAR SADF 121300Z 0500 FG SCT003 08/07 Q1021
Requirements:
Detect:
    Airport
    Visibility
    Fog (FG)
    Temperature
    Then print something like:
    Airport: SADF
    Visibility: 500 meters
    Fog: Yes
    Temperature: 8°C
    IFR conditions likely.
"""
#metar = input('Paste the METAR: ')

airports = {
    'SABE': 'Buenos Aires - Aeroparque Jorge Newbery',
    'SAEZ': 'Buenos Aires - Ministro Pistarini (Ezeiza)',
    'SADF': 'San Fernando',
    'SADM': 'Morón',
}

name = "SADF"
def main():
    for key, value in airports.items():
        if key == name:
            print(f'{key} - {value}')
        else:
            print('Airport not found.')

main()