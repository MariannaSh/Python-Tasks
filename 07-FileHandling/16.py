name=str(input('File name: '))
count=0
with open(name, 'r') as file:
    for i in file:
        count+=1
print(count)