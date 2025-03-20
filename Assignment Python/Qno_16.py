# Find the Difference Between the Sum of Odd and Even Digits. 
# Modify the previous program to find the absolute difference between the sum of even and odd digits. 
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
        difference=evenSum-oddSum
        print('difference: ',evenSum,'-',oddSum,'=',difference)
        break