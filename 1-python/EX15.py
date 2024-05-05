#multiple inheritance
class class_a:
    def display1(self):
        print("class a")
class class_b:
    def display2(self):
        print("class b")
class class_c(class_a,class_b):
    def display3(self):
        print("class c")
obj=class_c()
obj.display1()
obj.display2()
obj.display3()
