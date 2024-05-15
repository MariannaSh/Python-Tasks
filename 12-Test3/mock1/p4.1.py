def f(fnc,prods): 
    a=[]
    for i in prods:
        a.append(fnc(i))
    return ','.join(a)

prods = ["water","cheese","tomato"] 
fnc = lambda x: "id:"+x[:2] 
print(f(fnc,prods)) 

fnc2 = lambda x: (x[0]+x[-1]).upper() 
print(f(fnc2,prods)) 
