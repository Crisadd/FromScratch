""" 
x = int(input("What's x? "))
y = int(input("What's y? "))

print(x+y)


x = float(input("What's x? "))
y = float(input("What's y? "))

z= round(x / y,2) # number 2 means 2 digits
p= round(x / y,2)
print(z)

print(f"{p:.2f}") # another way to get 2 digits

"""


def main():
    x = int(input("What's x? "))
    
    print("x squared is:", square(x))


def square(n):
    return n*n #return n ** 2

main()