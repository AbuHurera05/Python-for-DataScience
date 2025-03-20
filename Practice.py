# print("hellow world")
# print("My name is Abu Hurera Junejo")

# print('''Village Haji Talib Junejo
# Taluka Tando Bago 
# District: Badin''')

# a='Apple'
# b=55
# c=55.787
# print(a)
# print(type(a))
# print(b)
# print(type(b))
# print(c)
# print(type(c))

# city="Badin"
# print(type(city))
# city=55
# print(type(city))
# city=5.43
# print(type(city))

# print(4+5)
# print(8-4)
# print(66*2)
# print(2**6) #In this 6 is a exponentional
# print(8/2)
# print(17//5) #this is a floor division 

# print(round(55.629)) # to round up the number

# print(abs(-877)) # it convert negative to positive

# print(bin(425))
# print(int('0b10', base=0))
# print()
#__________________________________________________________________________________________
# print(r'C: mydocument\python\practice.py') # r is use to print sentences as it same as write

# name='Youtube'
# print(name)
# print(name[4]) #it gives 5 indext character
# print(name[1:5])    #it gives character between 1 and 5
# print(name[1:])     #it gives character from 1 index to last
# print(name[:3])     #it gies character from 0 to which indext you write
# print(name[-4])     #it subtract index 
# print('My'+name[3:])
# print(len(name))

#________________________________List__________________________________
# nums=[55,35,53,8,88,7]
# print(nums)
# print(nums[2:5])
# print(nums[-4])
# print(nums())

# cities=['badin','tando bago','golarchi','matli']
# print(cities)

# name=['4.4','John','junaid','77','45']
# print(name)

# mil=[nums,cities]
# print(mil)

# nums.append(59)
# print(nums)

# nums.insert(4,532)
# print(nums)

# nums.remove(88)
# print(nums)

# print(nums.pop())

# del nums[1:2]
# print(nums)

# nums.extend([45,78,21,32,]) #add more than one values
# print(nums)

# print(min(nums))
# print(max(nums))
# print(sum(nums))

# nums.sort()
# print(nums)

#________________________________________Tuple_____________________________________
#We cannot change the tuple element it has only two method
# tup=(12,34,53,22,14,12,12)
# print(tup[2])
# print(tup.count(12)) 
# print(tup.index(34))

#_______________________________________Set________________________________________
#set eliminated the duplicate value
#indexing is not supported 
# s={23,43,12,11,53,32,21,34,34,12,11}
# print(s)

#______________________________________Dictionary__________________________________
#in dictionary we can easily get data by own maded key 
# data={1:'Shahnawaz',2:'Aslam',3:'Soomar',4:'Talib'}
# print(data)
# print(data[2])
# print(data.get(1,'not found'))
# print(data.get(5,'not found'))

# name=['Junaid','Faizan','Haroon']
# values=['JS','Python','Java']

# test= dict(zip(name,values))
# print(test)

# test['Monika']='CS' #to add new key and values in test dictionary
# print(test)
# del test['Faizan']  #to delete the by putting key which do you want to delete
# print(test)

# prog={'JS':'Atom','CS':'VS','Python':['Pycharm','Sublime'], 'Java': {'JSE':'Netbeans','JEE':'Eclipse'}}
# print(prog)
# print(prog['JS'])
# print(prog['Python'])
# print(prog['Python'][1])
# print(prog['Java'])

#__________________________________________Variable_____________________________________________
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

#____________________________________________Data Type_______________________________________________
#int there are different type of data type
#1. numaric(a:int,b:float,c:complex,d:bool)
# a=4     #int
# b=6.4   #float
# c=4+5j  #complex
# print(type(a))
# print(type(b))
# print(type(c))

# d=complex(a,b)  #type casting from ineger and float to complex
# print(d)
# e=int(True) 
# f=int(False)
# print(e, f)

#2. Sequence (a:list,b:set,c:tuple,d:String,e:Range)
# li=['apple','banana','mangos','satabarry']
# print(type(li))
# s={44,22,'aslam','jan'}
# print(type(s))
# tup=('mehran','civic','corrola','yarsi')
# print(type(tup))
# str='Badin'
# print(type(str))

# print(range(10))
# print(list(range(10))) 
# print(list(range(0,12,2)))
# print(type(range(10)))

# dic={'navin':'iPhone','aslam':'Samsung','Soomar':'oneplus','sidra':'infinix'}
# print(dic.keys())
# print(dic.values())
# print(dic['sidra'])

#___________________________________________Operators______________________________
#assignment Operators(=)
# a=8
# b=2
# a,b=6,2  #we assign two values in one line

#arthmentic operators(+,-,*,/,%)

#unary operators
# n=5
# print(n)
# n=-n
# print(n)

#Operational operator(<,>,==,!=)
# print(a>b)

#Coditional Operator(and,Or,not)
# print(a<b and b>a)
# print(a>b or b>a)
# x=True
# print(not x)

#BitWise Operator
# print(~13)  #(~) this is compliment symbol
# print(12 & 13)
# print(12 | 13)
# print(12^1)
# print(12^13)
# print(10<<2)
#____________________________________________Number System Conversion_____________________
# print(bin(25))
# print(0b11001)

# print(oct(25))
# print(0o31)

# print(hex(25))
# print(0x19)

#_____________________________________________Import Module_________________________________
# import math as m
# from math import sqrt,pow   # it user for choosing some method not all
# x=m.sqrt(25)
# print(x)
# print(m.floor(2.9))
# print(m.ceil(2.4))
# print(m.pow(2,5))
# print(m.pi)
# print(m.e)

# print(help(m))

#_____________________________________________User Input______________________________________
# import sys
# x=int(input('Enter first Number: '))
# y=int(input('Enter 2nd number: '))

# z=x+y
# print(z)
# ch= input('Enter a char: ')
# print(ch[0])

# ch=input('Enter a char: ')[0]
# print(ch)

# result= eval(input('enter 1st number: '))         #it is use for expression
# print(result)

# a=sys.argv[0]
# b=sys.argv[1]
# print(a+b)

#_________________________________________IfElifElse______________________________
# import sys
# x=int(input('Enter first Number: '))
# y=int(input('Enter 2nd number: '))

# z=x+y
# print(z)
# ch= input('Enter a char: ')
# print(ch[0])

# ch=input('Enter a char: ')[0]
# print(ch)

# result= eval(input('enter 1st number: '))         #it is use for expression
# print(result)

# a=sys.argv[0]
# b=sys.argv[1]
# print(a+b)

#___________________________________________While Loop_________________________________
# i=1

# while i<=5:
#     print('Telusko', end=' ')
#     j=1
#     while j<=4:
#         print('Rocks',end=' ')
#         j=j+1
#     i=i+1
#     print('')

#____________________________________________For Loop___________________________________
# x=['navin',55,32,22]
# for i in x:
#     print(i)

# for i in range(0,11):
#     # print(i)
#     if i!=5:
#         print(i)

#_____________________________USE OF BREAK,CONTINUE,PASS________________________
# --> Break
# av=3
# x=input('How many candies do yo want: ')
# x=int(x)
# i=1
# while i<=x:
#     if i>av:
#         break
#     print('candy',i)
#     i+=1

# --> Continue
# for i in range(1,100):
#     if i%3==0:
#         continue
#     print(i)
# -->Pass
# for i in range(1,101):
#     if i%2!=0:
#         pass
#     else:
#         print(i)
#_________________________________________________________
# for i in range(4):
#     for i in range(4):
#         print('#',end='')
#     print()

# for i in range(4):
    
#     for j in range(i+1):
#         print('#',end='')
#     print()

# for i in range(4):
    
#     for j in range(4-i):
#         print('#',end='')
#     print()

#_________________________________ForElse________________________
# nums=[12,43,38,33,54,39]
# for i in nums:
#     if i%5==0:
#         print(i)
#         break
# else:
#     print('Not Found')

# num=int(input('Enter the number: '))
# for i in range(2,num):
#     if num%i==0:
#         print('Not a Prime Number')
#         break
# else:
    # print('Prime Number')
# ____________________________________Array__________________________
# from array import *

# vals=array('i',[5,6,7,8,8])
# char=array('u',['a','e','i','o','u'])
# print(vals.buffer_info())
# print(vals.typecode)
# vals.reverse()
# print(vals)
# print(vals[3])

# for i in range(len(vals)):
#     print(vals[i])

# for i in vals:
#     print(i)

# for a in char:
#     print(a)

#copy values from old arry new arry
# newArray=array(vals.typecode,{a for a in vals})
# for a in newArray:
#     print(a)

# newArray=array(vals.typecode,{a*a for a in vals})
# for a in newArray:
#     print(a)
# i=0
# while i<len(newArray):
#     print(newArray[i])
#     i+=1

# __________________________input values from user in Array___________________________
# arr=array('i',[])
# value=int(input('Enter the length of array: '))
# for i in range(value):
#     x=int(input('Enter next value'))
#     arr.append(x)

# print(arr)

# #Search the index number of value
# x=int(input('Eneter the Value: '))
# k=0
# for i in arr:
#     if i==x:
#         print(k)
#         break
#     k+=1
# print(arr.index(x))

# ________________________________Use of Numpy in Array______________________
# from numpy import *
#numpy is used for multidimension array

# arr=array([2,4,3,53,3])
# print(arr)
# arr=array([2,4,3,53,3.5],int)
# print(arr.dtype)

# arr=linspace(1,5,5)
# arr= arange(1,6,2)  #it start with 1 and end with 6 and increment 2
# arr= logspace(1,40,5)  #it gives log valuse 
# print('%.2f'%arr[2])
# arr=zeros(5) #it gives only zeros in array
# arr=ones(5,int) #it give ones in array
# print(arr)

# ______________________________________Copy Array_________________________
#arr methdo: sin(),cos(),sqrt(),sum(),min(),max(),log(),concatenate([])
# arr1=array('i',[1,2,3,4,5,6])
# arr2=array('i',[2,3,4,5,6,4])
# print(concatenate([arr1,arr2]))
# arr3=arr1+arr2
# print(arr3)
# arr=arr1
# print(arr)

#________________________________________Reverse the same array_____________________
# arr=array([2,3,4,5,6,7])
# print(arr)
# start=0
# end=len(arr)-1
# while start<end:
#     arr[start],arr[end]=arr[end],arr[start]
#     start=start+1
#     end=end-1
# print(arr)

# arr4=arr1     

# arr4=arr1.view   #(view change the array id or position 
# it is the shallowcopy which we change in arr1 then arr4 will be changed)
# arr4=arr1.copy()  #now it is the deep copy which means we change the arr1, arr4 cannot be changed

# print(arr4)
# print(id(arr1))
# print(id(arr4))

#_______________________________________Two D Arry + Matrix__________________________
# arr=array([ 
#             [1,3,4,5,6,3],
#             [4,2,4,2,5,3]
#             ])
# print(ndim(arr))  #ndim() is rterun the dimension of array
# print(shape(arr))   #shape() it gives rows and column in array
# print(size(arr))    #size() it count the all the element in the array
# arr2=arr.flatten()  #flatten it convert two dimension array to one dimension array
# print(arr2)
# arr3=arr2.reshape(3,4)   #it gives 2D array form 1D array
# print(arr3)   
# arr3=arr2.reshape(2,2,3)    #it gives 3D arrary from 2D array
# print(arr3)

# m=matrix('1,2,3;5,7,5;9,8,6')
# m2=matrix('1,4,3;5,7,5;0,3,6')
# print(m)
# print(diagonal(m))
# print(m.min)
# print(m.max)
# m3=m+m2
# print(m3)
# m3=m*m2
# print(m3)

#________________________________________Function___________________________________
# def greet():
#     print("hellow ")
#     print("Hi")
# greet()

# def add(s,y):
#     c=s+y
#     print(c)
#     return c
# add(4,3)

# result=add(2,5)
# print(result)

# def add_sub(a,b):
#     x=a+b
#     y=a-b
#     return x,y
# result1,result2= add_sub(5,4)
# print(result1)
# print(result2)

# def list(a):
#     print(id(a))
#     a=8
#     print(id(a))
#     print(a)

# a=10
# list(a)
# print(id(a))

# def list(lst):
#     print(id(lst))
#     lst[1]=25
#     print(id(lst))
#     print(lst)

# lst=[10,20,30]
# list(lst)
# print(id(lst))

#Argument
#1.Formal Argument: that at the time of making funciton
#2.Actul Argument: declare at the time of calling function(positon, keyword, default, variable length)
#keyword: data(name: 'navin',age: 20)
#variable length
# def sum(a,*b):  #in this the b will be the tuple
#     print(a)
#     print(b)
#     c=a
#     for i in b:
#         c=c+i
#     print(c)

# sum(3,5,35,3,2,5)

# def person(name,**data):   # double * is used to store  value wiht key
#     print(name)
#     # print(data)
#     for i,j in data.items():
#         print(i,j)
# person('abu', age=22, city='badin', phone=98030)

#practice
# lst=[2,5,44,59,39,33,53,21,30,92]

# def count(lst):
#     even=0
#     odd=0
#     for i in lst:
#         if i%2==0:
#             even+=1
#         else:
#             odd+=1

#     return even,odd
# even,odd = count(lst)
# print(f'Even: {even} and Odd: {odd}')



# a= int(input('Enter the Legnth: '))
# def counting(a):
#     names=[]

#     count=0
#     for i in range(a):
#         name=input(f'Name {i+1}: ')
#         names.append(name)
#         if len(name)<5:
#             count+=1
#     return names,count

# names,count=counting(a)
# print(f'Names: {names} and 5<name are: {count}')

#______________________________________Fabbonaci Series_____________________
#0,1,1,2,3,5,8,13.....
# def fib(n):
#     a=0
#     b=1
#     if n==1:
#         print(a)
#     elif n<0:
#         print('Invalid Number..')
#     else:
#         print(a)
#         print(b)
#         for i in range(2,n):
#             x=a+b
#             a=b
#             b=x
#             if x>100:
#                 break
#             print(x)
            
# fib(100)

#_________________________________________Factorial_________________________
# def fac(a):
#     num=1
#     for i in range(1,a+1):
#         num=num*i
#     return num
# result=fac(5)
# print(result)
    
# ___________________________________________Recursion____________________________
#this is  infinit recursion
# def greet():
#     print('Hellow ')
#     greet()
# greet()

#Recursion example with factorial
# def fac(n):
#     if n==0:
#         return 1
#     return n*fac(n-1)
# result=fac(5)
# print(result)

# _______________________________________________Lamda Expression_____________________________
#Anonymous or Lamda we written a function in a single line
#the sqaure of in functio using lamda
# f= lambda a: a*a

# result=f(4)
# print(result)
# f= lambda a,b: a+b

# result=f(4,7)
# print(result)

#___________________________________Filter,map,lambda,Reduce________________________
# for reduce we have to import ==> # from functools import reduce
#filter(function,list), map(function,list),reduce(function,list))
# def is_even(a):
#     return a%2==0
# lst=[2,4,5,6,7,8,6,2,1,3]
# even= list(filter(is_even,lst))
# print(even)

# lst=[1,2,4,6,7,9,8]

# even=list(filter(lambda n : n%2==0,lst))   
# print(even)

# double=list(map(lambda n: n*2,even))
# print(double)

# def add_all(a,b):
#     return a+b
# sum=reduce(add_all,double)
# print(sum)

# ________________________________________Decorators____________________________
#Decorators is that which change the function behaviors at the run time 
# def div(a,b): # for example this is a function which we can not change 
#     print(a/b)

#by using decorators we change the function by creating a new function
# def smart_div(func):
#     def inner(a,b):
#         if a<b:
#             a,b=b,a
#         return func(a,b)
#     return inner
# div(2,4)  # it is without decorators
# div= smart_div(div) # it is with the decorators
# div(2,4)



    