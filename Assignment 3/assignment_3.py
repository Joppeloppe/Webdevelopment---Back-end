"""
Joakim Levin
AD3897
"""
import os, os.path, json

# Uppgift 1
print("Uppgift 1\n")


# Clears the screen.
def clearScreen():
    clear = lambda: os.system('cls')
    clear()


# Del 1

# Creates a menu.
def menu1():
    print("Hello and welcome to part 1!\n")
    print("1 - Add new member.")
    print("2 - See all members.")
    print("\n")
    print("0 - Continue assignment.\n")


# Creates a dictionary of a person from parameters given.
def createMember(firstName, lastName):
    member = {}
    member["firstName"] = firstName
    member["lastName"] = lastName

    print(member)

    return member


# Prints the information of a member.
def printMember(member):
    name = member["firstName"] + " " + member["lastName"]

    print(name)


members = list()

while True:
    menu1()
    choice = input("Please select an option from the menu above: ")

    if choice == "1":
        firstName = input("What's the members first name? ")
        lastName = input("What's the members last name? ")

        newMember = createMember(firstName, lastName)

        members.append(newMember)
        pass
    elif choice == "2":

        for i in range(len(members)):
            printMember(members[i])

        pass
    elif choice == "0":
        print("Good bye!")
        clearScreen()
        break;
    else:
        # Invalid entry.
        clearScreen()
        pass


# Del 2

# Creates a menu.
def menu2():
    print("Hello and welcome to part 2!\n")
    print("1 - Add new player.")
    print("2 - See all players.")
    print("\n")
    print("0 - Continue assignment.\n")


# Creates a new player
def addPlayer():
    player = {}


    firstName = input("What's the players first name? ")
    lastName = input("What's the players last name? ")
    country = input("What country does the player play for? ")

    player["firstName"] = firstName
    player["lastName"] = lastName
    player["country"] = country

    if os.path.isfile('players.txt'):

        with open('players.txt', 'a') as fileWriter:
            fileWriter.write(printPlayer(player))
            print("Added new player: " + printPlayer(player))

    else:
        with open('players.txt', 'a') as fileWriter:
            fileWriter.write(printPlayer(player))
            print("Added new player: " + printPlayer(player))

        print("Added new player: " + printPlayer(player))


# Prints the information of a player
def printPlayer(player):
    name = player["firstName"] + "," + player["lastName"] + "," + player["country"]

    return name + "\n"


# Lists all the players from a file	
def listPlayers():
    if os.path.isfile('players.txt'):
        fileReader = open('players.txt', 'r')
        print(fileReader.read().splitlines())
        fileReader.close()

    else:
        print("\nERROR: File not found!\n")


while True:
    menu2()
    choice = input("Please select an option from the menu above: ")

    if choice == "1":
        addPlayer()
        pass
    elif choice == "2":
        listPlayers()
        pass
    elif choice == "0":
        clearScreen()
        break
    else:
        clearScreen()
        pass


# Del 3

# Creates a menu.
def menuJson():
    print("Hello and welcome! Now with more JSON then EVER BEFORE!\n")
    print("1 - Add new player.")
    print("2 - See all players.")
    print("\n")
    print("0 - Continue assignment.\n")


# Adds a new player to JSON file
def addPlayerJSON():

    firstName = input("What's the players first name? ")
    lastName = input("What's the players last name? ")
    country = input("What country does the player play for? ")

    player = {
        "firstname": firstName,
        "lastname": lastName,
        "country": country
    }

    if os.path.isfile('players.json'):

        with open('players.json', 'r') as jsonData:
            data = json.load(jsonData)

        data["players"].append(player)

        with open('players.json', 'w') as jsonData:
            json.dump(data, jsonData)

        print("Added player")

    else:
        data = {
            "players": [player]
        }
        with open('players.json', 'w') as jsonData:
            json.dump(data, jsonData)

        print("Added player")




# Lists all the players in JSON file
def listPlayersJSON():
    if os.path.isfile('players.json'):

        with open('players.json') as jsonData:
            data = json.load(jsonData)

        for player in data["players"]:
            print(player)

        print("\n\n")


    else:
        print("\nERROR: File not found!\n")


while True:
    menuJson()
    choice = input("Please select an option from the menu above: ")

    if choice == "1":
        addPlayerJSON()
        pass
    elif choice == "2":
        listPlayersJSON()
        pass
    elif choice == "0":
        clearScreen()
        break
    else:
        clearScreen()
        pass

print("\n\n\nEnd of assignment!")
