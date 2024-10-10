#write a python program to input electric bill units from the user and print the 
#the bill using below conditions 
#if units are < 100, bill will be 8rs/ unit
#if units between 100 to 200, bill will be 8rs/unit
#if units between 201 to 500, bill will be 10rs/unit
#if units are greater then 500, bill will be 15rs /unit

units = int(input("enter no of elevtric units consumed"))
lightBill = 0.0
if units <100:
      lightBill = 5* units
     
elif units >= 100 and units <=200:
    lightBill =8 * units
elif units >= 201 and units <=500:
     lightBill =10 * units
else:
     lightBill = 15 * units
print("light bill:",lightBill)
