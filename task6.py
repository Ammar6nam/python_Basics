i=int(input('Enter the temperature: '))
c=0
f=0
type=input('In which measuring unit this scale? c for Celsius and f for Fahrenheit: ')
match type:
    case 'f':
        c=5/9*(i-32)
        print(f'The temperature in Celsius is {c} degrees.')
    case 'c':
        f=9/5*i+32
        print(f'The temperature in Fahrenheit is {f} degrees.')
    case _:
        print('Error!')