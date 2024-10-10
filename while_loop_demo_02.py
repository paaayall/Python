num = int(input("enter a number:"))
flag = 1
sum = 0
i = 2
while i < num:
    if(num%1 ==0):
        flag = 0
        break
    i = i + 1
if(flag == 0):
    print(num, "is not prime!!!")
else:
    print(num, "is  prime!!!")     
  