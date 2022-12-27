#Creating  a list
Names = [ 'Soj', 'Key', 'Ra', 'Ked', 'An']
#Accessing content of list using index value
print(Names[-1])

message = f"Hey, {Names[0].title()}"

print (message)
#Removing last item in the list using pop()
#to remove from any index, use index in parantheses. ex. pop(0)
#pop allows reuse of the item, del deletes permanently
# or can use remove() method.

notBFF = Names.pop()
print(f"{notBFF.title()} is not my BFF.")

#remove() only deletes the first occurence.
Names = [ 'Soj', 'Key', 'Ra', 'Ked', 'An']
Busy = 'An'
Names.remove(Busy)

#Add item to existing list.
print(Names)
NotBusy = 'Raj'
Names.append(NotBusy)
print(Names)
print(f"\n {Busy.title()} can't make it to the party :( but {NotBusy} is joining :) " )


#Inserting at position 0
Names.insert(0, 'Trish')
#Sorting the order of the list temporarily
print(sorted(Names))
print(Names)
# can use reverse=True for reverse alphabetical order.

Names.sort(reverse=True)
print(Names)

#Finding a length of the list
len(Names)