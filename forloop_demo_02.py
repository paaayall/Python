i = 2
number = int(input("enter a number"))
sum = 0
flag = 1
for i in range(2,number):
    if number % i == 0:
        flag = 0
        break
if flag == 0:
    print(number,"is not a prime")
else:
    print(number,"is a prime")       