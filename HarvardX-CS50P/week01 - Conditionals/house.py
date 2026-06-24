name = input(" What's your name? ").title()
""" 
if name  == 'Harry' or name == 'Hermaione' or name == 'Ron':
    print('Gryffindor')
elif name == 'Draco':
    print('Slytherin')
else:
    print('Who?')
"""

match name:
    case 'Harry' | 'Hermaione' | 'Ron':
        print('Gryffindor')

    """ case 'Hermaione':
        print('Gryffindor')
    case 'Ron':
        print('Gryffindor')"""
    
    case 'Draco':
        print('Slytherin')
    case _:
        print('Who?')