# from functools import reduce
#Anonymous or Lamda we written a function in a single line
#the sqaure of in functio using lamda
# f= lambda a: a*a

# result=f(4)
# print(result)
# f= lambda a,b: a+b

# result=f(4,7)
# print(result)

#___________________________________Filter,map,lambda,Reduce________________________
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

# sum=reduce(lambda a,b: a+b,double)
# print(sum)