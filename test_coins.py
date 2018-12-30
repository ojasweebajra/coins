import sys

def main():
    menu()

def menu():
    print("Welcome to Coin Count. What would you like to do? ")
    print("1. Display volunteer details, totals etc.")
    print("2. Add coins.")
    print("3. Quit")
    choice = input()
    if choice == "1":
        display()
    elif choice == "2":
        coins()
    elif choice == "3":
        sys.exit()
    else:
        print("Invalid choice, try again.")
        menu()


def volunteers():
    volunteersFile = open("volunteers.txt", "w+")
    vFound = False
    for row in volunteersFile:
        volunteerInfo = row.split(",")
        print("Name: ", volunteerInfo[0])



def display():
    # Add code to display volunteers details
    print(".")

def check(coinType):
    file = open("coin_stuff.txt", "r")
    cFound = False
    for line in file:
        details = line.split(",")
        if details[0] == coinType:
            cFound = True
            coinWeight = float(details[1])
            coinsNeeded = details[2]

    if cFound == False:
        print("Coin not found.")
    else:
        return coinWeight, coinsNeeded



def accuracy(weight, coinweight):
    numBags = weight/coinWeight
    print(numBags)

    if numBags.is_integer():
        accurate = True
        print("Accurate")
    else:
        accurate = False
        print("Not accurate")
        # Add how many more needed to fill a bag
        numBags = int(numBags)
        print(numBags)

    return numBags


def coins():

    checkCoins = "Y"

    while checkCoins == "Y":
        name = input("Name: ")
        coinType = input("Coin type: £")
        weight = float(input("Weight: "))
        coinWeight = " "
        coinsNeeded = " "

        check(coinType)
        accuracy(weight, coinWeight)
        print("Coin type: ", coinType, "Weight: ", coinWeight, "Coins needed to fill a bag: ", coinsNeeded)





    file.close()

    checkCoins = input("Check again?: Y/N ")


# Program begins here:
main()