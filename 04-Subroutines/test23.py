def ilosc(n):
    text=input().lower().split()
    summa=0
    for i in text:
        summa+=i.count(n)
    return summa


    