

def f(first_letter,last_letter):
    file = open("data.txt",'r', encoding='utf-8') 

    count=0
    for line in file:
        line=line.lower().split()
        for i in line:
            if (i[-1]=='.' or i[-1]==',' or i[-1]=='!' or i[-1]=='?' or i[0]=='.' or i[0]==','):
                if(i[0]==first_letter and i[-2]==last_letter):
                    count+=1
            else:
                if(i[0]==first_letter and i[-1]==last_letter):
                    count+=1

    return count

print(f("w","d"))


