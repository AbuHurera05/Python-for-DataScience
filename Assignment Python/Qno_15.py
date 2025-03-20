#  Sum of Even and Odd Digits Separately in a Number 
# Write a program to find the sum of even and odd digits separately in a given number.
num=int(input('Enter any Number: '))
evenSum=0
oddSum=0
while True:
    modulus=num%10
    num=num//10
    if modulus%2==0:
        evenSum+=modulus   
    else:
        oddSum+=modulus
    if num==0:
        print('Even Sum: ',evenSum)
        print('Odd Sum: ',oddSum)
        break
