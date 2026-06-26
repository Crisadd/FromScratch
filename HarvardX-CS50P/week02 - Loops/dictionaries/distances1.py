distances = {
    "Voyager 1": 163,
    "Voyager 2": 136,
    "Pioneer 10": 80,
    "New Horizons": 58,
    "Pioneer 11": 44,
}


def main():
    for distance in distances.values(): #This method returns all the values in the dictionary. In this opportunity, values are 163, 136, etc
        print(f"{distance} AU is {convert(distance)} m")


def convert(au):
    return au * 149597870700


main()
