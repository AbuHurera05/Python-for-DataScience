# Find the sum of the digits of a given number using modulus (%). 
num=int(input('Enter any Number: '))
sum=0
num1=num
while num1>0:
    modulus=num1%10
    sum+=modulus
    num1=num1//10
print('Sum of ',num,' is',sum)