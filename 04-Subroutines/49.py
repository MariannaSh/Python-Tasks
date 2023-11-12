# def f(dice):
#     max_dice=0
#     n=0
#     for i in dice:
#         count=dice.count(i)
#         max_dice=max(count,max_dice)
#         if count==max_dice:
#             n=i
#     return n


# def f(dice):
#     freq={}
#     max_freq=0
#     digit=''
#     for i in dice:
#         if i not in freq:
#             freq[i]=1
#         else:
#             freq[i]+=1
#         if freq[i]>max_freq:
#             max_freq = freq[i]
#             digit = i
#     return int(digit)
# def f(s):
#     max_digit = s[0]
#     max_count = 1
#     current_count = 1

#     for i in range(1, len(s)):
#         if s[i] == s[i-1]:
#             current_count += 1
#         else:
#             current_count = 1

#         if current_count > max_count:
#             max_count = current_count
#             max_digit = s[i]

#     return int(max_digit)

# # Примеры использования:
# print(f('5233165554211'))  # Вывод: 5
# print(f('2133'))  # Вывод: 3
# print(f('12355666'))  # Вывод: 6
# print(f('2321111'))  # Вывод: 1
# print(f("543422224555"))  # Вывод: 2
# print(f('544555552643444'))  # Вывод: 5
# print(f('58373336644443'))  # Вывод: 4
# print(f('537273322227443'))
# print(f('48737272225633335422'))


# print(f('5233165554211')) => 5
# print(f('2133')) => 3
# print(f('12355666')) => 6
# print(f('2321111')) => 1
# print(f("543422224555")) => 2
# print(f('544555552643444')) => 5
# print(f('58373336644443')) => 4




def f(dice):
    maximum = 0
    # a=len(dice)
    for i in range(10):
        count = dice.count(str(i))
        if count>maximum:
            maximum=count
            x_odp = i
    return x_odp



print(f('5233165554211'))
print(f('2133'))
print(f('12355666'))
print(f('2321111'))
print(f("543422224555"))
print(f('5436455574345'))

# prime number print(f(1))
# def f(n):
#     new=[1]
#     for i in range(2,10000):
#         k=0
#         for j in range(1,i+1):
#             if i%j==0:
#                 k+=1
#         if k==2:
#             new.append(i)
#     return new[n]

# print(f(1))
# print(f(5))



