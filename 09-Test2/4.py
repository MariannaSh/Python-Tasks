def f(subjects):
    max_key=None
    max_av=0
    for key,value in subjects.items():
        if value:
            av=sum(value)/len(value)
            if av>max_av:
                max_av=av
                max_key=key
    return max_key



print(f({"math":[3,4,4],"geo":[5,4,4,4],"comp":[5,4]}))

