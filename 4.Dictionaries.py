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


