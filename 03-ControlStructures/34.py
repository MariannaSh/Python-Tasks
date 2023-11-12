# amount=int(input())
# five=amount//5
# two=(amount-5*five)//2
# one=(amount-5*five-2*two)//1
# print(five, two,one)

n=int(input('Enter the amount in PLN: '))
n5=n//5
n2=(n-5*n5)//2
n1=(n-5*n5-2*n2)

print(f'The amount of PLN {n} in coins: 5 zł - {n5}, 2 zł - {n2}, 1 zł - {n1}')