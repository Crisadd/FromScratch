""" Arithmetic Product and Conditional Logic

Write a Python function that accepts two integer numbers. If the product of the two numbers is less than or equal to 1000, 
return their product; otherwise, return their sum.

"""

def main():
    first_number = int(input('Enter first number: '))
    second_number = int(input('Enter second number: '))

    result = product_or_sum(first_number,second_number)
    print(result)

def product_or_sum(first_number,second_number):
    product = first_number * second_number
    if product <= 1000:
        return product
    else:
        return first_number+second_number

main()



    """Nivel 2 - Que se pueda repetir (while)

En lugar de terminar el programa, podrías hacer algo así:

Ingrese primer número
Ingrese segundo número

Resultado: 120

¿Desea continuar? (s/n)

Si escribe

s

vuelve a empezar.

Si escribe

n

1111111111111111111111
Nivel 5 - Contador

Cada vez que hace una operación:

Operación 1
Operación 2
Operación 3

Cuando sale:

Realizaste 3 operaciones.

1111111111111111111111111
Nivel 7 - Estadísticas

En lugar de solo guardar resultados:

Operaciones realizadas: 5

Productos: 3

Sumas: 2


11111111111111111
ivel 8 - Separar todo en funciones

En vez de tener solo dos funciones, podrías tener:

main()

get_numbers()

product_or_sum()

continue_program()

print_statistics()

Sin mirar soluciones, intentá agregar estas cuatro cosas:

✅ Que el programa siga ejecutándose hasta que el usuario escriba "n".
✅ Que cuente cuántas operaciones realizó.
✅ Que al finalizar muestre ese total.
✅ Que si el usuario escribe algo distinto de "s" o "n", vuelva a preguntar.

Con eso ya estarías practicando varios conceptos importantes a la vez sin que el ejercicio se vuelva demasiado complejo.

    """