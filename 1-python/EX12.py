#bulit_in class attributes
class myclass:
    '''
        this class show the use of bulit-in attributes.
    '''
    def __init__(self):
        self.name="aayush"
    def display(self):
        print(self.name)
print(myclass.__name__)
print(myclass.__doc__)
print(myclass.__dict__)
print(myclass.__module__)
print(myclass.__bases__)
