file = open('film_titles.txt','w')

for movie in range(5):
    y=input('Enter a title: ')
    file.write(y+'\n')
file.close()

file = open('film_titles.txt','r')
print(file.read())
file.close()