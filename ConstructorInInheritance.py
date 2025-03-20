class A:
    def __init__(self):
        print("This is the init of A")
    def feature1(self):
        print("Feature 1 from class A")
    def feature2(self):
        print("Feature 2 from Class A")
class B(A):  
    def __init__(self):
        print("This is the  init of B")
        super().__init__()          #this super keyword called the consturctor of A(Without Super only B class Constructor will be called)           
    def feature3(self):
        print("Feature 3 from class B")
    def feature4(self):
        print("Feature 4 from Class B")
class C(B):  
    def __init__(self):
        print("This is the init of C")
        super().__init__()                
    def feature5(self):
        print("Feature 5 from class C")
    def feature6(self):
        print("Feature 6 from Class C")
#Method Rewolution Order: it get left then right method 