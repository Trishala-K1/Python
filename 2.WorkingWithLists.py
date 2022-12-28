Pizzas = ['Chicken', 'Pepporoni', 'Italian meatball']
Friend_Pizzas = ['Salami', 'Mixed Veggies', 'Three cheese']

#Looping through a list
for pizza in Pizzas:
    print(f"My Favorite pizza is, {pizza}.")
for pizza in Friend_Pizzas:
    print(f"My firend's favourite pizza is, {pizza}.")
#Doing something after a for loop- slicing
print("I really love pizza!")
print(f"The first two items of my list are: {Pizzas[:2]}")
print(f"The first two items of my friend's list are: {Friend_Pizzas[:2]}")
#using range() function with two parameters to make a list of chronological numbers
Squares = [value**2 for value in range(1, 21)] #** represents exponents.
print(Squares)
#Adding third parameter for skipping steps
for value in range(3,31, 3): #Multiple of 3.
    print (value)
#Appending values to empty list.
Cubes = []
for value in range(1,11):
    Cubes.append(value**3)
print(Cubes)

#Python refers to values that cannot change as immutable, and an immutable list is called a tuple.
#A tuple looks just like a list, except you use parentheses instead of square brackets.
