# Ask user for their name
name = input("What's your name? ").strip().title()

""" 
Multi line comments 

 Say hello to user: 3 ways to do that
print('Hello, ' + name)
print('Hello,',name)
print('Hello,',name,sep='???') 

# Remove whitespace from str
name = name.strip()  

# Capitalize user's name
#name = name.capitalize()  Solo pone mayuscula a la primer letra, si es un nombre y apellido no le pone a ambas, por eso se pone title
name = name.title()

# Remove whitespace and Capitalize user's name
name = name.strip().title()
"""

# Split user's name into first name and last name
first, last = name.split(" ")

print(f'Hello, {name}') #This is the correct way to use 
print(f'Hello, {first}')

