def check_prime_no(num):
    if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num,end=" ")
    
lower = int(input("enter lower limit: "))
upper = int(input("enter upper limit: "))

print("Prime numbers between", lower, "and", upper, "are:")

for i in range(lower, upper + 1):

   check_prime_no(i)