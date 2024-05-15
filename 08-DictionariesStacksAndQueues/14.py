winter_semester = {
    "math":60,
    "programming":30,
    "history":15
}

summa=0
for key,value in winter_semester.items():
    summa+=value
print(f"The total number of hours in the winter semester is {summa}")