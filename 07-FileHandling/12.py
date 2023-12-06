file=open('student.txt','w')

name=str(input('Name: '))
file.write(name+"\n")

uni=str(input('University: '))
file.write(uni+"\n")

field=str(input('Field: '))
file.write(field+"\n")

file.close()