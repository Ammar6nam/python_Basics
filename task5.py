import random
x=0
randomNumber = random.randint(1,10)
# print(randomNumber)
while x==0:
    number=int(input('Guess a number between 1 and 10: '))
    if number==randomNumber:
        print('Well guessed!')
        break
    else:
        continue