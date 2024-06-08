i=int(input('Enter the number of the stars u need them '))
l=[]
for x in range(-i,i+1):
    if x<=0:
        print((x+i)*' *')
    if x>0:
        print(-(x-i)*' *')