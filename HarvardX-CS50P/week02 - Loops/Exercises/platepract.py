vanity_plate = input('Vanity Plate: ').upper()
numbers = {'0','1','2','3','4','5','6','7','8','9'}
list = []

verification = True


#print(len(vanity_plate))

if len(vanity_plate) < 2 and len(vanity_plate) > 6:
    verification = False

elif vanity_plate[0] in numbers or vanity_plate[1]  in numbers:
        verification = False

else:
    found_number = False
    for i in vanity_plate:
        if not i.isalnum():
            verification = False
            
        if i in numbers:
             if not found_number:
                if i == '0':
                    verification = False
                found_number=True
        
        elif found_number:
            verification = False
        
if verification:
    print("Valid")
else:
    print("Invalid")

#is_valid returns True if s meets all requirements and False if it does not.

#- “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity 
#plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”