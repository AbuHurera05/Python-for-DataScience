class A:
    def feature1(self):
        print("Feature 1 from class A")
    def feature2(self):
        print("Feature 2 from Class A")
class B(A):                 #Single leve Inheritance(it have all features of A and B)
    def feature3(self):
        print("Feature 3 from class B")
    def feature4(self):
        print("Feature 4 from Class B")
class C(B):                  #Multi level Inheritance (it has all features of A,B and C aswell)
    def feature5(self):
        print("Feature 5 from class C")
    def feature6(self):
        print("Feature 6 from Class C")
# class D(A,B):               #This is the Multiple Inheritance
#     def feature7(self):
#         print("Feature 7 from class D")
#     def feature8(self):
#         print("Feature 8 from Class D")

a1=A()
a1.feature1()

a2=B()     

a3=C()    

# a4=D    
# a4.feature1()
