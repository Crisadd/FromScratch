x = int(input('x --> '))
y = int(input('y --> '))

if x < y:
    print('X is less than Y')
elif x > y:
    print('X is greater than Y')
else:
    print('X is equal to Y')

if x < y or x > y:  # Another way:    if x != y
    print('X is not equal to Y')
else:
    print('X is equal to Y')

