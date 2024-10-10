def reverse(no):
    temp = str(no)
    rev_no = temp[::-1]
   
    return rev_no

num = int(input("enter a no:"))

result = reverse(num)
print("Reversed no:",result)
