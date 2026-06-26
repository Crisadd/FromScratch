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

    num_max = 0
    total_sum = 0
    num_even = 0
    num_odd = 0

    for current_number in range(0, number+1):
        previous_number = current_number -1


        if current_number == 0:
            previous_number = 0

        total = current_number + previous_number
        total_sum += total

        if total % 2 == 0:
            num_even +=1
        else:
            num_odd +=1

        if total >= num_max:
            num_max = total

        print(f"{current_number}\t\t{previous_number}\t\t{total}")

    return num_max, total_sum, num_even, num_odd


def print_count(num_max, total_sum, num_even, num_odd):
    print(f'Largest Sum = {num_max}')
    print(f'Total of all sums = {total_sum}')
    print(f'Even sums = {num_even}')
    print(f'Odd sums = {num_odd}')

def ask_to_continue():
    answer = input('Would you like to continue? y/n: ').lower()

    while answer not in ("y", "n"):
        answer = input('Invalid answer. Would you like to continue? y/n: ').lower()

    return answer == 'y'

def main():
    while True:
        num_max, total_sum, num_even, num_odd = counter()
        print_count(num_max, total_sum, num_even, num_odd)

        if not ask_to_continue():
            print("Thanks for using this program!")
            break


main()