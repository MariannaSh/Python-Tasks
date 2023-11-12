# def f(number):
#     summa=0
#     number=str(number)
#     for i in number:
#         if number.count(i)>1:
#             summa+=int(i)
#     return summa

# print(f(1027))
# print(f(10222))
# print(f(230335))
# print(f(513553007))

def f(number):
    number=str(number)
    summa=0
    for i in number:
        if number.count(i)>1:
            summa+=int(i)
    return summa

print(f(1027))
print(f(230335))
