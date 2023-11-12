# a='Gjnsj JH jsjn'
# b=len(a)
# for i in a.split():
#     print(i[0],end='')

def f(name):
    a=name.split()
    new=''
    for i in a:
        new+= ''.join(i[0])
    return new
    
print(f('Internet of Things'))
print(f('Python'))
print(f('For Your Information'))