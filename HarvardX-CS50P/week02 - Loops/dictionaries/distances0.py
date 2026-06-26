distances = {
    "Voyager 1": 163,
    "Voyager 2": 136,
    "Pioneer 10": 80,
    "New Horizons": 58,
    "Pioneer 11": 44,
}


def main():
    for name in distances.keys():   #This method returns all the keys in the dictionary. In this opportunity, keys are voyager 1, voyager 2, etc
        print(f"{name} is {distances[name]} AU from Earth")


main()
