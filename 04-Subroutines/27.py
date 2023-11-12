# card='3212345467540000'
# a=len(card)
# print(card[:2]+'*'*10+card[-4:])

def f(card_number):
    return (card_number[:2]+'*'*10+card_number[-4:])

print(f('5290312400019022'))