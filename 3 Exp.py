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
My_list=[1,2,3,5,6]
print ("original list:",My_list)

print("appending 6 to list")
My_list.append(7)
print("appended list:",My_list)

print("inserting 4 at 3 index ")
My_list.insert(3,4)
print("inserted list: ", My_list)

print("removing 1 from list ")
My_list.remove(1)
print("removed list:", My_list)

print("length of list: ",len(My_list))

print("popping index 4 from list ")
My_list.pop(4)
print("popped list: ", My_list)

print("clearing list ")
My_list.clear()
print("cleared list: ", My_list)
