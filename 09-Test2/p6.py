import json

def f(years,course):
    with open("data.json",'r',encoding='utf-8') as file:
        data=json.load(file)
        numberSt=0
        for item in data:
            if item['age']>=years:
                for i in item['studies']['courses']:
                    if i['name'] == course:
                        avarage=sum(i['grades'])/len(i['grades'])
                        if avarage >=4:
                            numberSt+=1
                                
        return numberSt
    


print(f(21,"statistics"))

    


