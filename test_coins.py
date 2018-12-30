checkCoins = "Y"

while checkCoins == "Y":
    name = input("Name: ")
    coinType = input("Coin type: £")
    weight = float(input("Weight: "))

    file = open("coin_stuff.txt", "r")

    cFound = False

    for line in file:
        details = line.split(",")
        if details[0] == coinType:
            cFound = True
            coinWeight = float(details[1])
            coinsNeeded = details[2]

    # validation
    print("Coin type: ", coinType, "Weight: ", coinWeight, "Coins needed to fill a bag: ", coinsNeeded)

    numBags = weight/coinWeight
    print(numBags)

    # checks accuracy
    if numBags.is_integer():
        accurate = True
        print("Accurate")
    else:
        accurate = False
        print("Not accurate")
        # Add how many more needed to fill a bag
        numBags = int(numBags)
        print(numBags)

    if cFound == False:
        print("Coin not found.")

    file.close()

    checkCoins = input("Check again?: Y/N ")

