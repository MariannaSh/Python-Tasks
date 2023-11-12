# def count_of_letter(n):
#     text=input().lower().split()
#     summa=0
#     for i in text:
#         summa+=i.count(n)
#     return summa

# print('The number of letter "e":', count_of_letter('e'))
    


def f(n):
    frase=str(input('enter letter: ')).lower().split()
    summa=0
    for i in frase:
        summa+=i.count(n)
    return summa

print(f('e'))