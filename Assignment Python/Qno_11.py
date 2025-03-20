# Count the Number of Digits in an Integer (Without Using Strings.  
#Write a Python program to count the number of digits in a given number using only arithmetic 
#operations.  num=54321
num=int(input('Enter any number to count the digit: '))
i=0
while True:
    mudulus=num%10
    # print(mudulus)
    i=i+1
    num=num//10
    if num==0:
        break
print('OutPut: ',i)
    


