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