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


