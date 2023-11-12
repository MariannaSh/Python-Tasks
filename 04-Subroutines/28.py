# def f(binary_number):
#     for i in binary_number:
#         if i != '0' and i != '1':
#             return False
#     return True

# print(f('1010001a'))
# print(f('132334'))

def f(binary_number):
    for i in binary_number:
        if i!='0' and i!='1':
            return False
    return True
print(f('10100100'))
print(f('10232'))
print(f('121j23kj3'))