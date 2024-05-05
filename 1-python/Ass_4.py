4.Create a class GrandM that has height & color as attributes & actions to get & display it. Create a class Mother that has eyecolor as attributes & actions 
  to get & display it. Mother class will inherit the GrandM class. Create a class Daughter that inherits the Mother class. Create an object of the Daughter 
  class and then access the method of GrandM & Mother class. 
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class GrandM:
    def get(self):
        self.height=input("Enter a Height of Grand Mother:")
        self.eyecolor=input("Enter a Eye color of Grand Mother:")
    def display(self):
        print("Height of Grand Mother is:",self.height)
        print("Eye color of Grand Mother is:",self.eyecolor)
class Mother (GrandM):
    def getd(self):
        self.eyecolor=input("Enter a Eye color of Mother:")
    def put(self):
        print("Eye color of Mother is:",self.put)
class Daughter (Mother):
    pass
m=Daughter()
m.get()
m.display()
m.getd()
m.put()