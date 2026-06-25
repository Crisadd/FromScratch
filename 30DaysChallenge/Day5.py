""" Arithmetic Product and Conditional Logic

Write a Python function that accepts two integer numbers. If the product of the two numbers is less than or equal to 1000, 
return their product; otherwise, return their sum.

"""

def get_numbers():
    first_number = int(input('Enter first number: '))
    second_number = int(input('Enter second number: '))
    return first_number, second_number

# Ask the user whether they want to perform another calculation.
def ask_to_continue():
    Operation_count = 1
    while True:
        first_number, second_number = get_numbers()
        result, arithmetic = product_or_sum(first_number, second_number)

        print(f'******************** Operation number: {Operation_count} ********************')
        print(f'Result to {first_number} {arithmetic} {second_number} = {result}')
        print('*************************************************************')
        answer = input('Would you like to continue? yes/no: ').lower()
    
        while answer not in ("yes", "no"):
            answer = input('Would you like to continue? yes/no: ').lower()
        
        if answer == 'yes':
            Operation_count +=1
            continue
        else:
            print('Thanks for using this program!')
            break
    

"""
    Return the product of two numbers if it is less than or equal to 1000.
    Otherwise, return their sum.
"""
def product_or_sum(first_number,second_number):
    product = first_number * second_number
    if product <= 1000:
        arithmetic = '*'
        return product, arithmetic
    else:
        return first_number+second_number, '+'

def main():
    ask_to_continue()

main()