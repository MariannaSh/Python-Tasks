file=open('numbers.txt','r')
# file_content = file.read()
sum=0
for i in file:
    sum+=int(i)
print(f'Sum: {sum}')