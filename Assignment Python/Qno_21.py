#. Write a Python program to check whether a given number is even or odd using the modulus operator.
num=int(input('Enter Number: '))
modulus=num%2
if modulus==0:
    print(num,' is even number')
else:
    print(num,' is odd number')