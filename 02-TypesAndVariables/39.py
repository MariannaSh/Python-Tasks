towar=float(input('Enterprice:'))
znizka=int(input('enter discount:'))*0.01

reduction=towar*znizka
price=towar-reduction

print(f'price with discount: {round(price,2)}')
print(f'reduction: {round(reduction,2)}')