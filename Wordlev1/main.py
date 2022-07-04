from wordleList import wordleList
import random
import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)


def printTable():
    print("---------------------------")
    print("| ", "_", "| ", "_", "| ", "_", "| ", "_", "| ", "_", " |")
    print("---------------------------")


# amount of tries user gets
x = 0
# position of matching letter of guess inside randomword
indexOfRand = 0
# position of matching letter of randomword inside guess
indexOfGuess = 0

myIndexOfGuess = []
myIndexOfRand = []

green = False
yellow = False

# choose a random word from the list
randomWord = wordleList[random.randrange(1, 12972)]
print("---------------------------")
print("Wordle first word is", Fore.RED + randomWord)

# print the table for the user to enter the words
printTable()

userGuess = input("Enter the 5 letter word guess:")
userGuessLen = len(userGuess)

# if user enters a word > or < 5 then make them re-enter the word
if userGuessLen != 5:
    print("You entered a word that is less than or greater than 5 characters")
    while len(userGuess) != 5:
        userGuess = input("Enter the 5 letter word guess:")

# yellow if in word
for char in randomWord:
    indexOfGuess = 0
    for letter in userGuess:
        if letter == char:
            # print(letter + " is equal to " + char)
            # print("This is indexOfGuess ", indexOfGuess)
            # print("This is indexOfRand ", indexOfRand)
            # call function on this one
            myIndexOfRand.append(indexOfRand)
            myIndexOfGuess.append(indexOfGuess)
            break
        indexOfGuess += 1
    indexOfRand += 1


# print("This is myIndexOfGuess", myIndexOfGuess[0])
# print("This is myIndexOfGuess", myIndexOfGuess[1])


for i in myIndexOfGuess:
    print("This is i in Guess ", i)
    i = 0
    if i < len(myIndexOfGuess):
        print("These are the values in myIndexOfGuess[", i, "]:", myIndexOfGuess[i])

for i in myIndexOfRand:
    print("This is i in Rand ", i)
    if i < len(myIndexOfGuess):
        print("These are the values in myIndexOfRand[", i, "]:", myIndexOfRand[i])


# if there was a letter found
if myIndexOfGuess[0] is not None and myIndexOfRand[0] is not None:
    # if they are not in the same index
    if myIndexOfGuess[0] is not myIndexOfRand[0]:
        # make the letter in guess yellow as it is in the incorrect index
        print("This letter ", userGuess[myIndexOfGuess[0]], "is in the word but wrong spot")
        yellow = True
    else:
        # make letter green as they match the index
        print()
        green = True


def printGuess(indexGuess, indexRand, yellow, green):
    loop = 5
    start = 0
    print("---------------------")
    # print("| ", end=" ")
    while start < loop:
        if start == indexGuess:
            print("|", Fore.YELLOW + userGuess[start], end=" ")
        else:
            print("|", userGuess[start], end=" ")
        start += 1
    print("|", end=" ")
    print("\n---------------------")


printGuess(myIndexOfGuess[0], myIndexOfRand[0], yellow, green)
