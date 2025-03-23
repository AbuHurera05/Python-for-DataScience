class Student:
    d=0
    def add(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            d=a+b+c
        elif a!=None and b!=None:
            d=a+b
        else:
            d=a
        return d
    
s1=Student()
print(s1.add(44))