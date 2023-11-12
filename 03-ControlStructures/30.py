time=str(input())

twelhour={
    '00': 12,
    '12': 12,
    '13': 1,
    '14': 2,
    '15': 3,
    '16': 4,
    '17': 5,
    '18': 6,
    '19': 7,
    '20': 8,
    '21': 9,
    '22': 10,
    '23': 11,
    '24': 12
}

a=time[0:2]
print(f'Time in 12-hour format: {twelhour[a]}{time[2:5]}pm')