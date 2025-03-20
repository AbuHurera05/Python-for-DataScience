#we id() to return the adress of variable. if value of variable are than adress will be same
# num=6
# print(id(num))
# name='ajaz'
# print(id(name))
# a=6
# print(id(a))
# a=77
# print(id(a)) #if we change the value the id will be changed

# PI=3.15 #in python variable can not be a constant but use captital letter for showing that it is a constant
# print(PI)

#Global Variable: variable which outside the function
#Local Variable: variable whic inside the function
#Function will preference the local variable
# a=10
# def somthing():
#     a=30
#     print("in fun",a)

# somthing()
# print("out side fun",a)

# a=10
# def somthing():
#     global a        #this global keyword is say that this is a global variable
#     a=30
#     print("in fun",a)  #output: 30

# somthing()
# print("out side fun",a)  #output: 30

# a=10 
# print(id(a))
# def somthing():
#     a=30
#     x=globals()['a']
#     print('inside:',x)
#     print(id(x))

#     globals()['a']=50

# somthing()
# print('outside',a)

# __________________________________________Special Variable____________________
#speacial varable is that whicha has two '_' at time of makin variable 
#for example this is our main file in which we importing different module 
import Calc
print("Variable: "+__name__)#


