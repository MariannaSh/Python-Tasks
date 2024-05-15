#####
# Stack definition
##

stack = []

# добавить значение в начало стека
def push(value):
    stack.append(value)
    
# удаляет самый верхний элемент стека
# и вщзвращает его значение 
def pop():
    if not empty():
        return stack.pop()
    else:
        return None
    
# return true if the stack is empty
def empty():
    return len(stack) == 0

# display stack
def display():
    for i in range(len(stack)-1,-1,-1):
        print(stack[i])
    print()

display()
push(2)
push(14)
push(9)
display()
pop()
display()
push(31)
push(6)
display()
pop()
pop() 
display()