def topten():
    n=1
    while n<=10:
        num=n*n
        yield num           #yield keywork make a funciton generator 
        n+=1

values=topten()
for i in values:
    print(i)