"""
Joakim Levin
AD3897
"""

# Uppgift 1
print ("\nUppgift 1")

# Prints all the numbers up to the given number.
def printNumbers(max):
	print("Printing numbers up to " + str(max))
	
	for x in range(1,max + 1):
		print(x)
		
printNumbers(5)


# Uppgift 2
print("\nUppgift 2")

"""
 Prints all the numbers up to the given number,
 where divisible by 3 print Foo,
 where divisible by 5 print Bar,
 where divisible by 3 and 5 print FooBar.
 """
def fooBar(max):
	print("FooBaring " + str(max))

	for x in range (1, max + 1):
		if(x % 3 == 0) and (x % 5 == 0):
			print("FooBar")
		elif(x % 3 == 0):
			print("Foo")
		elif (x % 5 == 0):
			print("Bar")
		else:
			print(x)
			
fooBar(15)


# Uppgift 3
print("\nUppgift 3")


# Calculates and prints the average number of a list.
def calculateAverage(list):
	total = 0;
	
	for x in list:
		total += x
		
	return (total / len(list))
	
numbers = [2, 4, 6, 8]

print(str(calculateAverage(numbers)))


# Uppgift 4
print("\nUppgift 4")

# Returns a list with elements with the minimum lenght.
def filterNamesByLenght(list, lenght):
	print("Filtering " + str(list) + " by lenght " + str(lenght))
	
	result = []
	
	for x in list:
		if(len(x) > lenght):
			result.append(x)
	
	return result

names = ["Sherlock", "John", "Eliza", "Joe", "Watson"]

namesFilter = filterNamesByLenght(names, 6)
print(namesFilter)


# Uppgift 5
print("\nUppgift 5")

myself = {
"firstName" : "Sherlock",
"lastName" : "Holmes",
"age" : 35,
"topThreeMovies" : ["Seven", "Gone Girl", "The Prestige"]
}

print(myself["firstName"])
print(myself["lastName"])
print(myself["age"])
print(myself["topThreeMovies"])


# Uppgift 6
print("\nUppgift 6")

# Prints the information of the person given.
def printPerson(person):
	result = ""
	
	name = person["firstName"] + " " + person["lastName"]
	age = "(" + str(person["age"]) + ")"
	movies = ", ".join(person["topThreeMovies"])
	topMovies = "Top Movies: " + movies
	
	print(name + " " +  age + ", " + topMovies)
	
printPerson(myself)



# Uppgift 7
print("\nUppgift 7")

# Creates a dictionary from parameters given.
def createPerson(firstName, lastName, age, topThreeMovies):
	person = {}
	
	person["firstName"] = firstName
	person["lastName"] = lastName
	person["age"] = age
	person["topThreeMovies"] = topThreeMovies
	
	return person
	
sherlock = createPerson("Sherlock", "Holmes", 35, ["Seven", "Gone Girl", "The Prestige"])

printPerson(sherlock)