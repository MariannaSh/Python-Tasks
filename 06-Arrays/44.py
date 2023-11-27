import matplotlib.pyplot as plt

x = []
y = []

# create x values
for n in range(-100,101):
    x.append(n)

# create y values
for n in x:
    y.append(n**2-3)

# display chart
plt.plot(x, y) #Эта строка, чтобы создать линейный график
plt.title('Graph of f(x) = x^2 - 3') #заголовок графика
plt.xlabel('x') #ось х
plt.ylabel('f(x)') #ось у
plt.grid(True) #добавляет сетку на график
plt.show()
