#multilevel inheritance
class class_a:
    def show1(self):
        print("class a")
class class_b(class_a):
    def show2(self):
        print("class b")
class class_c(class_b):
    def show3(self):
        print("class c")
obj_c=class_c()
obj_c.show1()
obj_c.show2()
obj_c.show3()
