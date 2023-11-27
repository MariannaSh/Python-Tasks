import random

array=[]
for i in range(8):
    new=random.randint(1,1000)
    array.append(new)

print('-'*42)
print('|{:4}|{:4}|{:4}|{:4}|{:4}|{:4}|{:4}|{:4}|'.format(*array))
print('-'*42)