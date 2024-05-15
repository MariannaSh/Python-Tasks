class C:
    def __init__(self,value=0) :
        self.counter=value
#Метод __init__ является специальным методом, который вызывается при создании нового объекта класса C.

    def m1(self):
        return self.counter
    
    def m2(self):
        self.counter+=1

    def m3(self):
        self.counter-=1

    def m4(self,n):
        self.counter += n

    def __str__(self): #вызывается при попытке преобразовать объект к строке.
        return str(self.counter)
    

c=C(5) 
print(c.m1())
c.m2()
print(c.m1())
c.m4(-8)
print(c.m1()) 
c.m3()
print(c.m1())
c.m4(10)
print(c.m1())
c.__str__() 
print(c.__str__() )
