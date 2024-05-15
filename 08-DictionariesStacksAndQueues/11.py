import json

movie = {
    "title" : "Harry Potter",
    "year" : "2001",
    "actor" : ["Daniel Radcliffe","Emma Woston","Rupert Grint"],
    "oscar" : False,
    "type" : "fantasy"
}

with open("favourite.json", 'w') as file:
    json.dump(movie,file,indent=4) 
# json.dump() для записи содержимого словаря Python movie в файл, указанный переменной file. Параметр indent установлен в 4, что означает, что данные JSON будут отформатированы с отступом в 4 пробела

file.close()