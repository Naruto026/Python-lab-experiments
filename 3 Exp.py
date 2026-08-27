#3. Write a python program to create a list and perform the following operations 
'''''
Length of list
Inserting an element 
Removing an element 
Appending an element 
Displaying the length of the list 
Popping an element 
Clearing the list 
 '''''
list=[1,2,3,4,5]
print ("original list: ",list)
print("appending 6 to list ")
list.append(6)
print("appended list:", list)

print("inserting 10 at 2 index ")
list.insert(2,10)
print("inserted list: ", list)

print("removing 2 from list ")
list.remove(2)
print("removed list: ", list)

print("length of list: ",len(list))
print("popping 4 from list ")
list.pop(4)
print("popped list: ", list)

print("clearing list ")
list.clear()
print("cleared list: ", list)
