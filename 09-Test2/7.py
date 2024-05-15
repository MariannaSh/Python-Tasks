import re

def f(arr):
    count=0
    for i in arr:
        if 4<= len(i) <=12:
            if re.findall('[a-z0-9]_',i):
                count+=1
    return count
        

print(f(["uek","water_7_x","anna.may","a_b_c_d_e_f"]))