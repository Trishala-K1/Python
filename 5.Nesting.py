# Nesting 
# A list of dictionaries
Friend1 = {'First_Name': 'Key', 'Last_Name': 'K' }
Friend2 = {'First_Name': 'Soj', 'Last_Name': 'T' }
Friend3 = {'First_Name': 'An', 'Last_Name': 'T' }

Friends = [Friend1, Friend2, Friend3]

for friend in Friends:
    print(friend)

# A List in a Dictionary
Pizza = {
    'Crust' : 'thick',
    'Toppings' : ['Chicken', 'Mushroom','Cheese'],
}
print(f"You ordered a {Pizza['Crust']}-crust pizza"
" with the following toppings: ")

for topping in Pizza['Toppings']:
    print(f"\t{topping}")

# A dictionary in a dictionary

users = {
    'Trishk' : {
        'First': 'Trish',
        'Last': 'Kar',
        'Location':'ktm',
    },
    'Sojt' : {
        'First': 'Soj',
        'Last': 'Th',
        'Location':'ktm',
        },
    }
for username, userinfo in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{userinfo['First']} {userinfo['Last']}"
    location = userinfo['Location']

    print(f"\tFull name: {full_name}")
    print(f"\tLocation: {location}")
