listNums= []
listSize = int(input("enter no of elements:"))
i = 1 
item = 0
print("please provide items to sorted in the list...")
while i<= listSize:
    item = input("enter numbers:")
    listNums.append(item)
    print(item,"Added to the list!!!")
    i= i + 1
print("Initial list:\n")
print(listNums)
listNums.sort() 
print("Sorted list in ascending order:\n")
print(listNums)
listNums.sort(reverse=True) 
print("Sorted list in reverse order:\n")  
print(listNums)