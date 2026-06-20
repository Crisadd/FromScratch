""" 
The included code stub will read an integer, n, from STDIN.

Without using any string methods, try to print the following:
1,2,3...n

Note that "..." represents the consecutive values in between.
Example
n = 5
Print the string 1 2 3 4 5.
"""

def value(a):
    for i in range( 1, a+1 ):
        print(i, end="")

number = int(input("Choose a number: "))

value(number)