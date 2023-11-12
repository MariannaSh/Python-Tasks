from math_1 import *

b=mykeyboard()
a=generate_number()


print(f'Computer number: {a}')

if b==int(a):
    print('you win')
else:
    print('You lose')