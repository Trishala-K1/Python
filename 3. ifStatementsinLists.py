'''
Conditional Tests

If a conditional test evaluates to Boolean expression, True, Python executes the code following the if statement. 
If the test evaluates to False, Python ignores the code following the if statement.
equality = inequality !=

Checking multiple conditions using or and and, if-elif-else chain
'''
#In summary, if you want only one block of code to run, use an if-elif-else chain. 
# If more than one block of code needs to run, use a series of independent if statements.
alien_color = ['green','yellow','red']
if 'green' in alien_color:
    print("You earned 5 points!")

#Ordinal Numbers Challenge

Numbers = [1,2,3,4,5,6,7,8,9]
for value in Numbers:
    if value == 1:
        print (f"{value}st")
    elif value == 2:
        print (f"{value}nd")
    elif value == 3:
        print (f"{value}rd")
    else:
        print (f"{value}th")

