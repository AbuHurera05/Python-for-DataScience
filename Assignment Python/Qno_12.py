# Find the Product of Digits of a Given Number. 
# Write a Python program to compute the product of digits of a given number. 
num=int(input('Enter ther Number: '))
multiply=1
while True:
    modulus=num%10
    multiply*=modulus
    num=num//10
    if num==0:
        print('Output: ',multiply)
        break
   