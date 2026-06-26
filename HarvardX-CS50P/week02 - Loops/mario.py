""" def main():
    print_column(3)
    print_row(4)

def print_column(height):
    for _ in range(height):
        print('#')

def print_row(width):
    print("?" * width)

main()
"""

def main():
    print_square(10)

def print_square(size):

    # For each row in square
    for i in range (size):

#
        # For each brick in row
#        for  j in range(size):
            # Print brick
#            print("#", end="")
#        print()


    # Another way to do the same
        print('#' * size)

main()
