# nums=[2,5,3,4,5,6]

# it=iter(nums)     #Iterator has a function called iter() which has different methods.
# print(it.__next__())    #this print the value one by one 
# print(it.__next__())

# print(next(it))         #it also print the value 

#__________________________________now we making an iterator__________________________________
class TopTen:
    def __init__(self):
        self.num=1
    def __iter__(self):
        return self
    def __next__(self):
        if self.num<=10:
            val=self.num
            self.num+=1
            return val
        else:
            raise StopIteration
        
values=TopTen()

print(next(values))
for i in values:
    print(i)


