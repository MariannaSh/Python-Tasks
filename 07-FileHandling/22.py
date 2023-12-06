import random

with open('intNumbers2.0.txt','w') as file:
    for rd in range(1,51):
        rd=random.randint(100,999)
        file.write(f"{rd}\n")

