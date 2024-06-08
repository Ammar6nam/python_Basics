number1=int(input('Enter number 1: '))
number2=int(input('Enter number 2: '))
number3=int(input('Enter number 3: '))
sum1=input('normal sum "n" or triple sum "t"?  ')
if sum1 =='n':
    sum=number1+number2+number3
    print(sum)
elif sum1== 't':
    sum=3*(number1+number2+number3)
    print(sum)
else:
    print('Error !!')