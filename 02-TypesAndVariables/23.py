import math
a=int(input('Enter a:'))
b=int(input('Enter b:'))
c=int(input('Enter c:'))

p=(a+b+c)//2
S=(p*(p-a)*(p-b)*(p-c))**0.5

r=S/p

lenth=2*math.pi*r

print(f'Triangle area: {S}')
print(f'Triangle circumference: {lenth}')