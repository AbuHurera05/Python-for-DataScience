#Convert a Number to Binary Without Using Built-in Functions. 
# Write a Python program to convert a given number to binary using only arithmetic operations (/ and 
# %).
num=int(input('Enter the Decimal Number: '))
binary=0
place=1
num1=num
print('Binary Number of ',num,' = ',end='')
while num1>0:
    modulus=num1%2    
    binary+=modulus*place 
    place*=10
    num1//=2
print(binary)    