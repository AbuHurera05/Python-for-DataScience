# Reverse the Digits of a Number Without Using Strings. 
# Write a Python program to reverse a given number using arithmetic operators. 
num=int(input('Enter the Number: '))
print('Reverse of ',num,' is ',end='')
while True:
    modulus=num%10
    print(modulus,end='')
    num=num//10
    if num==0:
        break