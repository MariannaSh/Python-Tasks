file=open('allproducts.txt', 'w')
f1=open('MeatAndFish.txt','r')
f2=open('GrainsAndBread.txt', 'r')


for line in f1:
    file.write(line)

for line2 in f2:
    file.write(line2)