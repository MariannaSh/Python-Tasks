import matplotlib.pyplot as plt
import math

x=[]
y=[]

for n in range(0,361):
    x.append(n)

for n in x:
    y.append(math.sin(math.radians(n)))

#Функция math.sin() из модуля math ожидает аргумент в радианах, а не в градусах. 
# Нужно конвертировать градусы в радианы, используя функцию math.radians()

plt.plot(x,y)
plt.title('function y = sin(x)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.show()