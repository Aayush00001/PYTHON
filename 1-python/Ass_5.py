5.Define a class Human having attributes firstname, lastname and gender. Define two actions  input_Human() and display_Human() to accept and display values. 
  Define derived class Employee having attributes company and level. Define two actions 
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class Human:
    def input_Human(self):
        self.firstname=input("Enter a First Name of Human:")
        self.lastname=input("Enter a Last Name of Human:")
        self.gender=input("Enter a Gender of Human:")
    def display_Human(self):
        print("Firstname of Human is:",self.firstname)
        print("Lastname of Human is:",self.lastname)
        print("Gender of Human is:",self.gender)
class Employee(Human):
    def input_emp(self):
         self.company=input("Enter a Company of Employee:")
         self.level=input("Enter a Level of Employee:")
    def display_emp(self):
          print("Company is:",self.company)
          print("Level is:",self.company)
m=Employee()
m.input_Human()
m.display_Human()
m.input_emp()
m.display_emp()