import main_functions

# Exercise 1: Using the function 'read_from_file',
# read superCompHeroes.json as a dictionary in Python,
# and print its type to confirm:
superCompHeroes = main_functions.read_from_file("superCompHeroes.json")

# Exercise 2: Print the number of keys in superCompHeroes
print("-------------------------------------")
print("Number of keys in superCompHeroes")
number = 0
for value in superCompHeroes:
    number = 1 + number
print("number of keys is " + str(number))

# Exercise 3: Print all the keys in superCompHeroes
print("-------------------------------------")
print("All keys in superCompHeroes")
for value in superCompHeroes:
    print(value)
# Exercise 4: Print the type of the value of 'members'
print("-------------------------------------")
print("Print the value of members")
print(type(superCompHeroes["members"]))
# Exericse 5: Print its first element:
print("-------------------------------------")
print("Print its first element")

print(superCompHeroes["members"][0])
# Exercise 6: Print the name of the first element
print("-------------------------------------")
print("Print the name of the first element")
print(superCompHeroes["members"][0]["name"])
# Exercise 7: Print the strength of the second member:
print("-------------------------------------")
print("Print the strength of the second member:")
print(superCompHeroes["members"][1]["strength"])

# Notice that the structure of the data is: dict->list->dict->string

# Notice that the structure of the data is: dict->list->dict->int

# Exercise 8: Print the names and strengths of the Super Component Heroes
# Hint: use a for loop for the list!
print("-------------------------------------")
print("Print the names and strengths of the Super Component Heroes")
for hero in superCompHeroes["members"]:
    print("Name:", hero["name"], "Strength:", hero["strength"])
# Exercise 9: To print members in order of strength:
print("-------------------------------------")
print("To print members in order of strength:")
for order in sorted(superCompHeroes["members"], key=lambda x: x["strength"]):
    print(order["strength"])
# Exercise 10: Create a new Super Component Hero and using the function
# 'save_to_file', overwrite the existing 'superCompHeroes.json' with
# this new entry


# IMPORTANT: automatically typing into the JSON file is not accepted
