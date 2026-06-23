# x = int(input('X --> '))

# Even number --> Numero Par
# Odd number --> Numero Impar

# if x % 2 == 0:
#    print('Even')
# else:
#    print("Odd")

def main():
    x = int(input('X --> '))
    if is_even(x):
        print('Even')
    else:
        print("Odd")

def is_even(n):
    if n % 2 == 0:  # Boolean
        return True
    else:
        return False

########################################## 42 minutos.38 segundos

main()