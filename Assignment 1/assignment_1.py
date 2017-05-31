"""
Joakim Levin
AD3897
"""

# Uppgift 1
print("Uppgift 1")

print(5*2<12)
print(55>22)
print(16/4==4)
print(8+2<=128)
print(32*8!=225)


# Uppgift 2
print("\nUppgift 2")

name = "Sherlock Holmes"
numOfChars = len(name)

print(numOfChars)


# Uppgift 3
print("\nUppgift 3")

part1 = "The area of a Triangle with a width of "
width = 12
part2 = " and the height of "
height = 8
part3 = " is: "
area = (width*height)/2

allParts = part1 + str(width) + part2 + str(height) + part3 + str(area)

print(allParts)


# Uppgift 4
print("\nUppgift 4")

# Del 1
print(" Del 1")

tisdag = "Tisdag"
hamburgare = "Hamburgare"
beBack = "I'll be back"

print(tisdag[:3])
print(hamburgare[3:])
print(beBack[-7:])

# Del 2
print(" Del 2")

learning = "It's Learning"
python = "Python: The Good Parts"

print(learning[5:].upper())
print(python[-10:].lower())


# Uppgift 5
print("\nUppgift 5")

width = 12
height = 8

# Returns the area of a triangle.
def calculateTriangleArea(width, height):
	return (width * height) / 2

print(calculateTriangleArea(width, height))


# Uppgift 6
print("\nUppgift 6")

#Returns the smallest value.
def min(value1, value2):
	if value1 < value2:
		return value1
	else:
		return value2


#Returns the biggest value.
def max(value1, value2):
	if value1 > value2:
		return value1
	else:
		return value2

#Test min function.
print("Min")
print(min(12, 17))
print(min(15, 15))
print(min(20, 3))

#Test max function.
print("Max")
print(max(12,17))
print(max(15, 15))
print(max(20, 3))


#Uppgift 7
print("\nUppgift 7")

#Checks if the value is odd (returns False) or even (returns True).
def isEven(value):
	if (value % 2) == 0:
		return True
	else:
		return False
		
print(isEven(4))
print(isEven(7))