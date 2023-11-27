
import random
def rand_elem(array):
    a=len(array)
    ran=random.randint(0,a-1)
    return array[ran]

print(rand_elem([3,23,45]))
