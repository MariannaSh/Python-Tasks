a=str(input())
if len(a)==9:
    print(f'{a[0:3]}-{a[3:6]}-{a[6:9]}')
else:
    print('Not in range')