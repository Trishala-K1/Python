#Accessing Values in a Dictionary
User = {'First_Name' : 'Trish', 'Last_Name' : 'K', 'Fav_Colour' : 'Black'}
print(User['Fav_Colour'])

#Adding new key-value pairs
User = {'First_Name' : 'Trish', 'Last_Name' : 'K', 'Fav_Colour' : 'Black'}
User['FavCity'] = 'Ktm'
User['FavCountry'] = 'USA'
User['FavNum'] = 6
print(User)

#Modifying values in a dictionary.
if User['First_Name'] == 'Trish':
    AddOne = 1
    NewFavNum = User['FavNum'] + AddOne
print(f"Trishala's favourite number is actually {NewFavNum}.")

#Using get() to access values
SalaryInfo = User.get('Salary', 'No Salary listed.')
print(SalaryInfo)

#Key-value pairs. Fav Number Challenge

FavNum = {'Soj' : '1', 'Key' : '7'}

SojNumber = FavNum['Soj']
KeyNumber = FavNum['Key']
print(f"Soj's favourite number is {SojNumber}.")
print(f"Key's favourite number is also {KeyNumber}.")

#Looping through key-value pairs in a dictionary using items() method.
for key, value in FavNum.items():
    print(f"\nKey: {key}")
    print(f"\nValue: {value}")
    print(f"{key}'s favorite number is {value}.")
print("* * *")
#Looping through all keys in a dictionary using key() method.
FavNum = {'Soj' : '1', 'Key' : '7'}
Friends = {'Soj', 'Key', 'Trish'}
for name in sorted(FavNum.keys()):
    print(f"Hi, {name}!")
    if name in Friends:
        Number = FavNum[name]
        print(f"\t{name}, I see your favorte number is {Number}!")
if 'Trish' not in FavNum.keys():
    print("Trish, please tell us your favorite number!")

#Looping through all values in a dictionary using values() method.
FavNum = {'Soj' : '1', 'Key' : '7'}
print("The following numbers have been mentioned: ")
for numbers in FavNum.values():
    print(numbers)
