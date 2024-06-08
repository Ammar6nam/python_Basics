number1=int(input('Enter number 1: '))
number2=int(input('Enter number 2: '))
if number1>number2:
    sum=2*number1-2*number2
elif number1<=number2:
    sum=abs(number1-number2)
print(sum)