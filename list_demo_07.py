listStudents= []
listSize = int(input("enter no of elements:"))
i = 1 
item = 0
print("please provide items to sorted in the list...")
while i<= listSize:
    item = input("enter students name:")
    listStudents.append(item)
    print(item,"Added to the list!!!")
    i= i + 1
print("Updated list:\n")

print(listStudents)    