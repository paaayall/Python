myDict = {
    "empid" : 101,
    "empName" : "jack",
    "empAge" : 30,
    "empSalary" : 40000
}

print(myDict)

#retriving value using key from  dictinory
print("EmpName: " , myDict["empName"])
#retriving value key from dictonory using get method
print("Empname: " , myDict.get("empName"))


#Adding a new key-value pair
myDict["empCity"] = "Mumbai"
print(myDict)

#Updating value for a key in dictinory.
myDict["empAge"] = 40
print(myDict)

# Removing dicitinory item
myDict.pop("empAge")
print(myDict)