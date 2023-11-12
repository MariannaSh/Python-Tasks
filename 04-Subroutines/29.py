

def f(amount_to_pay):
    m_5=amount_to_pay//5
    m_2=(amount_to_pay-5*m_5)//2
    m_1=(amount_to_pay-5*m_5-2*m_2)
    summa=m_2+m_1+m_5
    return summa

print(f(23))
print(f(8))
print(f(0))
