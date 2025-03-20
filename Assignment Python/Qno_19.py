#Find the Greatest Digit in a Given Number.  
#Write a program to find the largest digit in a given number.
num=int(input('Enter Number: '))
largest=0
while num>0: 
    modulus=num%10
    num=num//10
    if largest<modulus:
        largest=modulus
print(largest,' is largest number')