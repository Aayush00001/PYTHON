class myclass:
    def __init__(self):
        print("object crated")
    def __del__(self):
        print("object destroyed!!")
m=myclass()
del m
