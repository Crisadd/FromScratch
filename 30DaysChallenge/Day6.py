""" Cumulative Sum of a Range
Practice Problem: Iterate through the first 10 numbers (0–9). In each iteration, print the current number, the previous number, 
and their sum.
"""
# Ask the user for the last number to count
def get_number():
    number_to_count = int(input('Enter the last number: '))
    return number_to_count


# Print the table header
def print_header():
    print(f'Current\t\tPrevious\tSum ')
    print('----------------------------------------------')


# Print the current number, previous number, and their sum.
def counter():
    number = get_number()
    print_header()

    for current_number in range(0, number+1):
        previous_number = current_number -1
        
        if current_number == 0:
            previous_number = 0
        
        total = current_number + previous_number

        print(f"{current_number}\t\t{previous_number}\t\t{total}")



def main():
    counter()

main()


"""

Nivel 4 ⭐⭐⭐

Al final mostrar:

Largest sum: 17
Smallest sum: 0

Empezás a practicar máximos y mínimos.

Nivel 5 ⭐⭐⭐⭐

Calcular el total de todas las sumas.

Ejemplo:

0
1
3
5
7
9
...

Al final:

Total of all sums = 81

Acumuladores.

Nivel 6 ⭐⭐⭐⭐

Contar cuántas veces la suma fue:

par
impar

Mostrar:

Even sums: 5
Odd sums: 5

Vas practicando %.

Nivel 7 ⭐⭐⭐⭐⭐

Mostrar el resultado con colores o símbolos.

Ejemplo:

✔ Current: 5 Previous: 4 Sum: 9

o

➜ Current: 8 Previous: 7 Sum: 15

No aporta lógica, pero hace el programa agradable.

Nivel 8 ⭐⭐⭐⭐⭐

Guardar cada fila en una lista.

Todavía no viste listas seguramente.

Cuando las veas:

results = []

Cada iteración agregará:

(Current, Previous, Sum)

Eso ya se parece a cómo trabajan los programas reales.

Nivel 9 ⭐⭐⭐⭐⭐

Separarlo en funciones.

Por ejemplo:

main()

get_limit()

calculate_sum()

print_table()

print_statistics()
Nivel 10 ⭐⭐⭐⭐⭐

Que el usuario pueda repetir todo el programa.

Igual que hiciste recién.
====================================
Current: 9
Previous: 8
Sum: 17

Iterations: 10
Largest sum: 17
Smallest sum: 0
Even sums: 5
Odd sums: 5
Total of all sums: 81
====================================
"""