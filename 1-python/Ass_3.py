3.Create a class Drawing that has width & length as attributes, getdata() & putdata() as actions. Create class Rect that inherits Drawing class. Create an 
  object of Ract class& access the methods of Drawing class.
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class Drawing:
    def getdata(self):
        self.width=input("Enter Width:")
        self.height=input("Enter Height:")
    def putdata(self):
        print("Width is:",self.width)
        print("Height is:",self.height)
class Rect(Drawing):
    pass
m=Rect()
m.getdata()
m.putdata()