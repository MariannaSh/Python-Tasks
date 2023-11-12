
# def f(sentence):
#     return sentence.replace(' ','')
    
    
# print(f('integrated development environment'))

def f(sentence):
    new=''
    for i in sentence.split():
        new+=i+''
    return new
        
    
print(f('integrated development environment'))