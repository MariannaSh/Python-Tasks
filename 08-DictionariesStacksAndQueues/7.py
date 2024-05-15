person = {
    "name": "Marek",
    "surname": "Banach",
    "age": 25,
    "hobby": ["swimming","excursions"],
    "married": True,
    "phone":{"landline":"123444321","mobile":"777888999"}
}

for key,value in person.items():
    print(key,value)

print(person['name'])
print(person['hobby'])

person['surname']="Nowak"
person['married']=False;
person['gender'] ="male"
person["hobby"].append("bicycle")
person['phone']['home']="313131444"


print()
for key,value in person.items():
    print(key,value)
