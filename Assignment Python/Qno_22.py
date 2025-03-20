#Reverse a given number using arithmetic operations (without using strings). 
num=int(input('Enter any number: '))
print('Revrse of ',num,' is ',end='')
while num>0:
    modulus=num%10
    print(modulus,end='')
    num=num//10
   
