
def f(word):
    wave=''
    for i in range(len(word)):
        wave+=word[:i].lower()+word[i].upper()+word[i+1:].lower()
        wave+="-"
    return wave[:-1]

print(f("book"))
