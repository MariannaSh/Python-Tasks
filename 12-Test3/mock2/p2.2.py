def f(x,y,d):
    for i in range(x,y+1):
        str_i=str(i)
        if d in str_i:
            return True
    return False

print(f(10,15,"14"))
print(f(100,120,"11"))
print(f(205,210,"04"))