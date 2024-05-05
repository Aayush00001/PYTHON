-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class Employee:
    def getEmployee(self):
        self.emp_id= input("Enter a employee Id:")
        self.name= input("Enter a Name:")
        self.salary= input("Enter a salary:")
        self.date_of_join= input("Enter a DOJ:")
    def showEmployee(self):
        print("Employee ID is:",self.emp_id)
        print("Name is:",self.name)
        print("Salary is:",self.salary)
        print("DOJ is:",self.date_of_join)
m=Employee()
m.getEmployee()
m.showEmployee()