basic_data = {
    "name":"Barbara",
    "age":21
}

advanced_data = {
    "status":"student",
    "married":False,
    "interest":["reading","swimming"]
}

person={}
person.update(basic_data)
person.update(advanced_data)

for key,value in person.items():
    print(key,value)