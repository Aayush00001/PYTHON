#single inheritance
class class_a:
    def show1(self):
        print("class a")
class class_b(class_a):
    def show2(self):
        print("class b")
obj_b=class_b()
obj_b.show1()
obj_b.show2()
