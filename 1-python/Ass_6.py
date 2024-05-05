6.Write a python program to override the super class method in subclass. 
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class Parent:
    def show(self):
        print("Parent")
class Child(Parent):
    def show(self):
        print("Child")
p=Parent()
c=Child()
p.show()
c.show()