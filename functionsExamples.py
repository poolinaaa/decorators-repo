import random
#file with example functions

#function which simulates lottery
#args are amount of numbers to be chosen and whole range of numbers
def lottery(amount, totalAmount):
    listOfNumbers = [*range(1, totalAmount+1)]
    listOfWinners = []
    for i in range(amount):
        random.shuffle(listOfNumbers)
        chosenNumber = listOfNumbers.pop(
            listOfNumbers.index(random.choice(listOfNumbers)))
        listOfWinners.append(chosenNumber)
    return listOfWinners

#some simple functions, there could be used any func
def func1(a):
    return a**a

def func2(a, b):
    return a+b, a