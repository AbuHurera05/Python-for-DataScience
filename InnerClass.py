class Student:
    def __init__(self,name,age,add):
        self.name=name
        self.age=age
        self.add=add
        self.lap=self.Laptop('Dell',8,256)
    def show(self):
        print(self.name,' ',self.age,' ',self.add)
        self.lap.show()
    class Laptop:
        def __init__(self,name,ram,ssd):
            self.name=name
            self.ram=ram
            self.ssd=ssd
        def show(self):
            print(self.name,' ',self.ram,' ',self.ssd)

s1=Student('abu',23,'badin')
s1.show()
s1.lap.show()

