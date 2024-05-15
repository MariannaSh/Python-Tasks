import re

def f(mnumbers):
    pattern = re.compile(r'^[+-]?[1-7a-dA-D]*$')
    count = 0
    for number in mnumbers:
        if pattern.search(number):
            count += 1
    return count

print(f(["A15", "-31", "7abC", "+D1", "-gH"]))  
print(f(["A05", "-3+1", "7ab8C", "+D1", "-22k"]))  

