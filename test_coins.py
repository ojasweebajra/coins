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
    volunteersfile = open("volunteers.txt", "w+")
    vfound = False
    for row in volunteersfile:
        volunteerinfo = row.split(",")
        print("Name: ", volunteerinfo[0])


def display():
    # Add code to display volunteers details
    print(".")


def check(cointype):
    file = open("coin_stuff.txt", "r")
    cfound = False
    for line in file:
        details = line.split(",")
        if details[0] == cointype:
            cfound = True
            coinweight = float(details[1])
            coinsneeded = details[2]

    if cfound == False:
        print("Coin not found.")
        coins()
    else:
        return coinweight, coinsneeded


def accuracy(weight, coinweight):
    weight = float(weight)
    coinweight = float(coinweight)
    numbags = weight/coinweight
    print(numbags)

    if numbags.is_integer():
        accurate = True
        print("Accurate")
    else:
        accurate = False
        print("Not accurate")
        # Add how many more needed to fill a bag
        numbags = int(numbags)
        print(numbags)

    return numbags


def coins():

    name = input("Name: ")
    cointype = input("Coin type: £")
    weight = float(input("Weight: "))

    new_weight, new_cn = check(cointype)
    print("Coin weight:", new_weight)
    print("Coins needed: ", new_cn)
    numbags = accuracy(weight, new_weight)

    print("Coin type: ", cointype, "Weight: ", new_weight, "Coins needed to fill a bag: ", new_cn)

    checkcoins = input("Check again?: Y/N ")
    if checkcoins == "Y":
        coins()
    else:
        menu()


# Program begins here:
main()

