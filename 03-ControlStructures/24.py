current=float(input('Current product price:'))
previous=float(input('Previous product price: '))

procent=100-(current*100)//previous

if procent>=10:
    print(f'Buy the product!!')
    print(f'Product price reduced by {int(procent)}%')
else:
    print('Not now')
