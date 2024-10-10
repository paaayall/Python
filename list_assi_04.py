#create a list of 5 intger element input a number from a user and check in that present in list


listNums = [10,20,30,40,50]
no=int(input("enter a no to search"))
flag = 0
for x in listNums:
    if (x==no):
     print(no,"is found")
     flag = 1
     break
if (flag ==0):
      print(no,"not found")
