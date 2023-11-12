# fibonaczi=[0,1]
# for i in range(2,20):
#     new_fib=fibonaczi[i-1]+fibonaczi[i-2]
#     fibonaczi.append(new_fib)

# for num in fibonaczi:
#     print(num, end=" ")

# def fibonaczi(n):
#     fibonaczi=[0,1]
#     for i in range(2,n):
#         new_fib=fibonaczi[i-1]+fibonaczi[i-2]
#         fibonaczi.append(new_fib)
    
#     return fibonaczi


# print(fibonaczi(20))
def f(n):
    fibonaczi=[0,1]
    f=0
    for i in range(2,21):
        f=fibonaczi[i-1]+fibonaczi[i-2]
        fibonaczi.append(f)
    return fibonaczi[n]

print(f(3)) #третий символ фибоначи
