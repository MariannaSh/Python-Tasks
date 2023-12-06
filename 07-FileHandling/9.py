file = open('countries.txt','r')
# file_content=file.read()

count=0
for line in file:
    count+=1
    print(f'{count}. {line}', end="")

file.close()
