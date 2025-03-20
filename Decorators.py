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
