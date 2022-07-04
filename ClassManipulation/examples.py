import main_functions

class Elf:
    def __init__(self,level,ability_scores=None):
        self.level = level
        self.ability_scores = {
            "str":11, "dex":12, "con":10,
            "int":16, "wis":14, "cha": 13
        } if ability_scores is None else ability_scores
        self.hp = 10 + self.ability_scores["con"]

# A) Create an instance of Elf named Elora
elora = Elf("first")
# B) Create an instance of Elf named Elrond
elrond = Elf("second",{"str":12, "dex":13, "con":11, "int":17, "wis":15, "cha":14})

# C) Print the value of hp for Elora
print(elora.hp)
# D) Print the value of hp for Elrond
print(elrond.hp)
# E) Print the value of level for Elora
print(elora.level)
# F) Print the value of ability_scores for Elrond
print(elrond.ability_scores)
# G) Convert the elora object instantiated above into a Python dictionary
elora_d = elora.__dict__ #converting an object into a Python dictionary
# H) Printing its type:
print("elora is of type", type(elora).__name__," and elora_d is of type", type(elora_d).__name__)
# I) Converting elrond object instantiated above into a Python dictionary
elrond_d = elrond.__dict__
# J) Printing its type:
print("elrond is of type", type(elrond).__name__," and elrond_d is of type", type(elrond_d).__name__)

# K) Printing both Elrond and Elora dictionaries
print(elora_d)
# L) Serializing both Elrond and Elora dictionaries to JSON
main_functions.save_to_file(elrond_d,"elrond.json")
main_functions.save_to_file(elora_d,"elora.json")
# M) Deserializing both Elrond and Elora JSON files to Python dictionary
elrond_des = main_functions.read_from_file("elrond.json")
elora_des = main_functions.read_from_file("elora.json")
# N) Printing their types
print("the type of elora is ", type(elora_des).__name__)
print("the type of elrond is ", type(elrond_des).__name__)
