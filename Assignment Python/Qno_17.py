# Check Whether a Number is an Armstrong Number. 
# An Armstrong number is a number that is equal to the sum of its own digits raised to the power of the 
# number of digits. 
num=int(input("Enter the number: "))
num1=num
power=num%10
num2=0
while True:
    modulus=num%10
    num2+=modulus**power
    num=num//10
    if num==0:
        break
print(num2)
if num2==num1:
    print(num1,' is Armstrong Number')
else:
    print(num1,' is Not a Armstrong Number')