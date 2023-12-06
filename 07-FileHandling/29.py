import re

file = open('grades.txt','r')
reader = file.read()

grades = re.findall("\d.{2}",reader)
summa=0
for i in grades:
    summa+= float(i)
print(summa/len(grades))