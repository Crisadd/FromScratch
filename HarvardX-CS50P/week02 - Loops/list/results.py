results = ["Mario", "Luigi"]

# .append() add a new element at the END of the list
# .remove() remove items from the list
# .extend() each element of the new list append into the list insteod of adding the complete list, it add each element
# .insert(0, "") Insert a new element into the list. The first number is the position of the list
# .reverse() flip the list

results.append("Princess")
results.append("Yoshi")
results.append("Koopa Troopa")

results.append(["Bowser", "Donkey Kong Jr."])
results.remove(["Bowser", "Donkey Kong Jr."])

results.extend(["Bowser", "Donkey Kong Jr."])

print(results)