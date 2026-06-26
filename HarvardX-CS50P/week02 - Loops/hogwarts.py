# LIST

"""
students = ["Hermaione", "Harry", "Ron", "Draco"]
houses = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin" ]

print(students[0])
print(students[1])
print(students[2])

for student in students:
    print(student)




for i in range(len(students)):  # Range don't take a string, take a number that's why i use lend()
    print(i + 1, students[i])
"""

# Dictionaries

"""
students = {
    "Hermione" : "Gryffindor",
    "Harry" : "Gryffindor",
    "Ron" : "Gryffindor",
    "Draco" : "Slytherin",
}

for i in students:  # for student in students --> Another way
    print(i, students[i], sep=", ")
"""
# List of Dictionaries
students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russel terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None},
]

for i in students:
    print(i["name"], i["house"], i["patronus"],sep=", ")