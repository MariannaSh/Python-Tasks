with open("data.txt",'r',encoding='utf-8') as file:
    count=0
    for line in file:
        if "m" in line:
            count+=1
print(count)
