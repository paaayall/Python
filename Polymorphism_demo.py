# Polymorphism: It is used to design loosely coupled systems, we can achieve it using method overriding.
# In this, both base and derived classes contains same method name containing different implementation.
# When the same method is called using base class object, the base class method is called and when the same
# method is called using derived class object, the derived class's method is called. 
class Employee:                                 # Base or Super or Parent class 'Employee'
    def __init__(self, empName, empSalary):
        self.empName = empName
        self.empSalary = empSalary
    def getEmpName(self):
        return self.empName
    def getNetIncome(self):
        return self.empSalary

class SalesPerson(Employee):                    # Derived or Child or Sub class 'SalesPerson'
    def __init__(self, empName, empSalary, noOfHours):
        # calling base class constructor in below statement (using super keyword)
        super().__init__(empName, empSalary)    # super keyword is used to access base class members in child class
        self.noOfHours = noOfHours
    def getNetIncome(self):
        return self.empSalary * self.noOfHours

def printEmployeeDetails(emp):    
    print("Name: ", emp.getEmpName(), ", Salary: ", emp.getNetIncome())

# creating instance of base class 'Employee'
emp = Employee("Jack", 30000)
# creating instance of derived class 'SalesPerson'
sp = SalesPerson("Jill", 500, 20)
# Displaying employee details (which is a base class)
printEmployeeDetails(emp)
printEmployeeDetails(sp)