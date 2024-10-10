class Employee:                                 # Base or Super or Parent class 'Employee'
    def __init__(self, empName, empSalary):
        self.empName = empName
        self.empSalary = empSalary
    def getEmpName(self):
        return self.empName
    def getEmpSalary(self):
        return self.empSalary

class SalesPerson(Employee):                    # Derived or Child or Sub class 'SalesPerson'
    def __init__(self, empName, empSalary, noOfHours):
        # calling base class constructor in below statement (using super keyword)
        super().__init__(empName, empSalary)    # super keyword is used to access base class members in child class
        self.noOfHours = noOfHours
    def getSalesPersonSalary(self):
        return self.getEmpSalary() * self.noOfHours
    
    # creating instance of base class 'Employee'
emp = Employee("Jack", 30000)
# creating instance of derived class 'SalesPerson'
sp = SalesPerson("Jill", 500, 20)
# Displaying employee details (which is a base class)
print("Employee Details are:")
print("Emp Name: ", emp.getEmpName(), ", EmpSalary: ", emp.getEmpSalary())
# Displaying salesperson details (which is a derived class)
print("SalesPerson Details are:")
print("SalesPerson Name: ", sp.getEmpName(), ", SalesPerson Salary: ", sp.getSalesPersonSalary())