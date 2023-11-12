number=str(input())

if number[:2]=='KR' or number[:2]=='KK' and len(number)==7:
    print(True)
else:
    print(False)