#function not accepting arguments and returning value.
def getSimpleInterest(amount, roi, time):
    si = (amount * roi * time) / 100.0
    return si

amt = float(input("Enter Amount: "))
rate = float(input("Enter rate of intrest:"))
time = int(input("Enter time in years:"))
SimpleInterest = getSimpleInterest(amt, rate, time)
print("simple interest:", SimpleInterest)