class Employee:
    def __init__(self, empName, empSalary):
        self.empName = empName
        self.empSalary = empSalary
    def getEmpName(self):
       return self.empName
    def getEmpSalary(self):
       return self.empSalary

class SalesPerson(Employee):
    def __init__(self, empName, empSalary, noOfHours):
        super().__init__(empName, empSalary)
        self.noOfHours = noOfHours   
    def getSalespersonSalary(self):
        return self.getEmpSalary()* self.noOfHours    
        

        # creating instance of base class 'employee'
emp = Employee("Jack", 30000)
        # creating instance of derived class 'Salesperson'
sp = SalesPerson("Jill", 500, 20)
        #Displaying employee details from base class 'Employee'
print("Employee Details are:")
print("Emp Name:",emp.getEmpName(),",EmpSalary: ",emp.getEmpSalary())
        #Displaying salesperson detalis (which is a derived class)
print("SalesPerson Details are:")
print("SalesPerson Name: ",sp.getEmpName(), ",SalePerson Salary ", sp.getSalesPersonSalary())