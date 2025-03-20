class Cars:
    wheels=5    #class Varables (is ko sirf eik change kar sakty hain)
    def __init__(self):
        self.model=2005         #These are instance Variable(is har object main alag sy change karna pary ga )
        self.com='BMW'

c1=Cars()
c2=Cars()
Cars.wheels=5
c1.model=2006
print(c1.model,' ',c1.com,' ',c1.wheels)
print(c2.model,' ',c2.com,' ',c2.wheels)