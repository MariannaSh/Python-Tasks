
def phone_keyboard():
    keyboard = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    a=len(keyboard)
    for i in range(a):
        print(*keyboard[i])
        
phone_keyboard()