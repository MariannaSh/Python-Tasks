file1=open('text.txt', 'r')
file2= open('copy.txt', 'w')

for i in file1:
    file2.write(i)

file1.close()