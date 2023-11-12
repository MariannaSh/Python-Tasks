number=int(input('Number of products purchased: '))
price=float(input('Product price: '))

fullprice=2*price
amount=(number-2)*(price-(price*25)//100)+fullprice
print(f'Amount to pay: {amount:.2f}')