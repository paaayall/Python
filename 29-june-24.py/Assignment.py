# input marks of 3 subject(phy,chem, maths) and calculate their percentages
#and print the result basis on the below condition:
#if percentage <40,the display the result as "failed with


phy =  int(input("Enter the phy marks"))
chem = int(input("Enter the chem marks"))
maths =int(input("Enter the maths marks"))
  
percentages = (phy+chem+maths)/300
if percentages < 40:
    print("Faild with",percentages ,"%")
elif percentages > 40 and percentages <60:
    print("passed with 2nd grade-",percentages,"%")
elif percentages >= 60 and percentages <75:
    print("passed with 1st grade-",percentages,"%")
elif percentages >= 75 and percentages <100:
    print("passed with 1st grade with distinction-congrast",percentages,"%")
else:
    print("invalid percentages")
