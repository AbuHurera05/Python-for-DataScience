class Student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    
    def __add__(self,other):
        m1=self.m1+ other.m1
        m2=self.m2+other.m1
        m3=Student(m1,m2)

        return m3
    
s1=Student(44,55)
s2=Student(88,33)
s3=s1+s2
print(s3.m2)