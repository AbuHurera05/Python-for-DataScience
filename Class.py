# class Computer:
#     def config(self):
#         print("8gb,5th generation, 513SDD")
 
# comp1=Computer()     #This is the object in python

# Computer.config(comp1)      #now calling the object

# comp1.config()              #can also call the object by using this 

#__________________________________________________________________
# class Computer:
#     def __init__(self,cpu,ram):
#         self.cpu=cpu
#         self.ram=ram
#     def config(self):
#         print(self.cpu,'ram:',self.ram)

# comp=Computer(5,8)
# comp.config()

#____________________________________________________________________
# class Computer: 
#     def __init__(self):
#         self.name='abu'
#         self.age=23

#     def detail(self):
#         print('My name is: ',self.name)
#         print('Age: ',self.age)
#     def compare(self,com2):
#         if self.name==com2.name and self.age==com2.age:
#             return True
#         else: 
#             return False
# com= Computer()
# com1=Computer()
# com.detail()
