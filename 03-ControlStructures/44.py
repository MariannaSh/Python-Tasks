
# summa=0
# quantity=0
# while True:
#     i=int(input('Введите число: '))
#     summa+=i
#     quantity+=1
#     if i == 0:
#         quantity-=1
#         break
    

# print(quantity,summa,summa//quantity)

# print(f'RESULT: Quantity= {quantity}, Sum={summa}, Mean={summa//quantity}')
summa=0
quantity=0
while True:
    n=int(input('Enter number: '))
    if n !=0:
        summa+=n
        quantity+=1
    else:
        break
print(f'RESULT: Quantity={quantity}, Sum={summa}, Mean={summa//quantity}')
