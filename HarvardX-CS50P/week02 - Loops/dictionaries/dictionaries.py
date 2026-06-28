#Dictionaries are keys and values. Example: "name":"value"
# .keys(): Iterates over keys only.
# .values(): Iterates over values only.
# .items(): Iterates over both keys and values as tuples

"""     {
    "name":"value"
    "name":"voyager1",
    "distance":163
    }

If you are not sure about the value, you can use get("name","Unknown")
"""


dic_pract = {
    "name": "Alonso",
    "Age": 45,
    "Address": "Rincon 468",
    "Nationality": "Argentina",
}


print(
    '*********************************************************\n'
    f'Hello {dic_pract["name"]}, How are you today?\n'
    f'You are {dic_pract["Age"]} years old and your address is {dic_pract['Address']}\n'
    f'Nationality: {dic_pract.get('Nationality',"Unknown")}\n'
    f'Date Of Bird: {dic_pract.get('date_of_bird',"Unknown")}\n'
    '**********************************************************')