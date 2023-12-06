file=open('text.txt','r')
while file.readline():
    for i in range(5):
        print(file.readline(), end="")
    input('press to continue')
