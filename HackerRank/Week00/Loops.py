""" 
Task
The provided code stub reads an integer, n, from STDIN. For all non-negative integers i<n, print i^2.
"""

number = int(input("Number: "))

if number >=0:
    i = 0
    while i < number:
        print(i*i)
        i +=1

else:
    print("The number is negative.")