"""
.values()
.keys()
.get()
.pop()
.items()
"""
WORDS = {"PAIR": 4, "HAIR": 4, "CHAIR": 5, "GRAPHIC": 7}

"""
def main():
    print("Welcome to Spelling Bee!")
    print("Your letters are: A I P C R H G")
    while len(WORDS)>0:
        print(f"{len(WORDS)} words left!")
        guess= input("Guess a word: ").upper()

        # TODO: Check if guess in dictionary
        if guess == "GRAPHIC":
            WORDS.clear()       # Removes all the keys in the dictionary
            print("You've won!")

        elif guess in WORDS.keys():
            points= WORDS.pop(guess)        # .pop return the value associate with this key and remove the key from the dictionary
            print(f"Good job! You scored {points} points.")

    print("That's the game!")


main()
"""

for word, points in WORDS.items():   #.items() give the key and the value, that's why it says word, points
    #Another option: for key, value in WORD.items()
    print(f'{word} was worth {points} points')
