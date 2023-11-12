height=int(input())*0.01
weight=int(input())

bmi=weight/height**2
print(bmi)

if 18.5<bmi<25:
    print('норма')
else:
    print('NO')