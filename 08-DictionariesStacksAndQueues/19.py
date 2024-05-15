import json

with open("students.json", 'r') as file:
    data=json.load(file)

limited_students=[]
for student in data:
    limited_student={
        'id': student['id'],
        'first name' : student['first_name'],
        'last name' : student['last_name']
    }
    limited_students.append(limited_student)


with open('limited.json', 'w') as file:
    json.dump(limited_students, file, indent=4)