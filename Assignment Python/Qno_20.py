# Find the Smallest Digit in a Given Number. 
# Write a program to find the smallest digit in a given number.
num=int(input('Enter Number: '))
smallest=num%10
while num>0: 
    modulus=num%10
    num=num//10
    if smallest>modulus:
        smallest=modulus
print(smallest,' is smallest number')