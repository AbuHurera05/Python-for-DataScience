a=6

try:
    print('Resource open')
    b=int(input('Enter a number'))
    print(a/b)
    print('Resource close')

except ZeroDivisionError as e:
    print("number can not diveided by 0",e)
except ValueError as e:
    print('please enter a valid valued',e)

finally:
    print('Resource close')
