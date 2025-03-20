#  Check Whether a Given Number is Palindrome.  
# A number is a palindrome if it remains the same when its digits are reversed.
num=int(input('Enter the number: '))
num1=num
str2=''
while True:
    modulus=num%10
    str2+=str(modulus)
    num=num//10
    if num==0:
        break
str2=int(str2)
if str2==num1:
    print(num1,'is Palindrom..')
else:
    print(num1,'is Not a Palindrom')