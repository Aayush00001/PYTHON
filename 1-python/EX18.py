#polymorephism inheritance
class myclass:
        def sum(self,a=None,b=None,c=None):
            if(a!=None and b!=None and c!=None):
                print(a+b+c)
            else:
                    print(a,b,c)
m=myclass()
m.sum(1,2)
m.sum(1)
m.sum(1,2,3)
m.sum()
