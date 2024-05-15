
def f(player1,player2):

    cards={
    "A":10,
    'K':10,
    'Q':10,
    'J':10,
    'T':10,
    '10':10,
    '9':9,
    '8':8,
    '7':7,
    '6':6,
    '5':5,
    '4':4,
    '3':3,
    '2':2
}

    summa1=0
    for i in range(len(player1)):
        summa1+=cards[player1[i]]
    
    summa2=0
    for i in range(len(player2)):
        summa2+=cards[player2[i]]

    if summa1<summa2:
        return False
    else:
        return True
    
    
print(f("AJ972","AQT72"))
print(f("9532","K8"))