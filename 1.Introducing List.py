#Creating  a list
Names = [ 'Soj', 'Key', 'Ra', 'Ked', 'Swi', 'An', 'Chi']
print(Names)

#Accessing elements of list using respective index values.
print(Names[-1])

#Using individual values from the list to compose a message.
#Using title() to format the names correctly. 
message = f"Hey, {Names[0].title()}" #Index position starts at 0. Item at index -1, Python always returns the last item in the list
print (message)

#Modifying elements in a list.

#Inserting an element at position 0
Names.insert(0, 'Trish')
print(Names)

#Deleting element from the list. del deletes permanently can use remove() or pop() method for reuse of the item. 
del Names[-1]
print(Names)

#Removing last item in the list using pop() and reuse that item.
#to remove from any index, use index in parantheses. ex. pop(0)
notBFF = Names.pop()
print(Names)
print(f"{notBFF.title()} is not my BFF.")

#Removing an Item by Value
#remove() only deletes the first occurence of that value.
Busy = 'Swi'
Names.remove(Busy)
print(Names)

#Appending element to the end of the existing list.
NotBusy = 'Raj'
Names.append(NotBusy)
print(Names)
print(f"\n {Busy.title()} can't make it to the party :( but {NotBusy} is joining :) " )

#Organizing a list
print(Names)
#Sorting the order of the list temporarily using sorted().
print(sorted(Names))
print(Names)

#Sorting the order of the list permanently using sort().
# can use reverse=True for reverse alphabetical order.
Names.sort(reverse=True)
print(Names)

#Finding a length of the list
Length= len(Names)
print(f"The length of the list is {Length}.")
