""" Objective
In this challenge, we will use loops to do some math.

Task
Given an integer,n , print its first 10 multiples. Each multiple n x i should be printed on a new line in the form: n x i = result.
"""

number = int(input('Number: '))

for i in range(1,11):
    print(f'{number} x {i} = {number*i}')

