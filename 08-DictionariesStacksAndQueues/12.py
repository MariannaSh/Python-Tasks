import json

student = {
    "name":"Jan",
    "surname":"Kowalski",
    "index":"123456",
    "grades":[3.5,4.0,3.0,4.5],
    "group":"ZISS-2313"
}

with open('student.json','w') as file:
    json.dump(student, file,indent=4)

file.close()