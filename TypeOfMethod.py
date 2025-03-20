class Stuedent:
    school="OPS"
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
# _______________________________________________Instance Method_________________________________
    def avg(self):
        return (self.m1+self.m2+self.m3)/3
    
    # ______________________________________Accessor and Mutator(Setter and getters)__________________
    def getM1(self):
        return self.m1
    def setM1(self,m1):
        self.m1=m1
    def getM2(self):
        return self.m2
    def setM2(self,m2):
        self.m2=m2
    def getM3(self):
        return self.m3
    def setM3(self,m3):
        self.m3=m3
# ____________________________________________ Class Method________________________________________
    @classmethod                #These are called decorators
    def getSchool(cls):
        return cls.school
    @classmethod
    def setSchool(cls,school):
        cls.school=school
# _____________________________________________Static Method________________________________________    
    @staticmethod
    def getInfo():
        print("Helow I am your leader...")

# _________________________________________________This is Main ________________________________
c1=Stuedent(34,56,34)

print(c1.getM1())
print(c1.getM2())
print(c1.getM3())
c1.setM1(57)
c1.setM2(100)
c1.setM3(40)
print(c1.getM1())
print(c1.getM2())
print(c1.getM3())

print(Stuedent.getSchool())
Stuedent.setSchool("Al Rehan Public School Tando Bago")
print(Stuedent.getSchool())

Stuedent.getInfo()