
# def f(detector):
#     counter = 0
#     max_count = 0
#     for c in detector:
#         if c == '+':
#             counter += 1
#             max_count = max(max_count, counter)
#         elif c == '-':
#             counter -= 1
#     return max_count >= 3

# print(f('+-+++-+---'))
# print(f('+-+-+-+-'))

# def f(detector):
#     count=0
#     max_count=0
#     for i in detector:
#         if i == '+':
#             count+=1
#             max_count=max(count,max_count)
#         else:
#             count-=1
#     if max_count >= 3:
#         return True
#     else:
#         return False
    
# print(f('+-+++-+---'))
# print(f('+-+-+-+-'))
# print(f("+-++-+--"))
# print(f("+-++-++-+---"))

def f(n):
    count=0
    max_count=0
    for i in n:
        if i=="+":
            count+=1
            max_count=max(count,max_count)
        else:
            count-=1
    if max_count>=3:
        return True
    else:
        return False
 
