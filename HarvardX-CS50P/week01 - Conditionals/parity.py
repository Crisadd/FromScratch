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
    #if n % 2 == 0:  # Boolean
    #    return True
    #else:
    #    return False
    
    # Other WAY: return True if n % 2 == 0 else False

    #Other WAY:
    return n % 2 == 0
main()