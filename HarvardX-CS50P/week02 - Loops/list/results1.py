results = ["Mario", "Luigi", "Princess", "Yoshi", "Koopa Troopa", "Toad", "Bowser", "Donkey Kong Jr."]

print(results)
# .append() add a new element at the END of the list
# .remove() remove items from the list
# .extend() each element of the new list append into the list insteod of adding the complete list, it add each element
# .insert(0, "") Insert a new element into the list. The first number is the position of the list
# .reverse() flip the list

results.remove("Bowser")
print(results)

results.insert(0, "Bowser")
print(results)

results.reverse()
print(results)


