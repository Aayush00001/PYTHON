#method overridding
class parent:
    def show(self):
        print("parent")
class child(parent):
    def show(self):
        print("child")
c=child()
c.show()
p=parent()
p.show()

