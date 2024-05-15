countries = [
    {"name":"Poland", "population":38000000},
    {"name":"USA", "population":331000000},
    {"name":"China", "population":1400000000},
    {"name":"India", "population":1366000000},
    {"name":"Russia", "population":145000000}
]

print("COUNTRY POPULATION")
i=0
while i<len(countries):
    print(f"{countries[i]['name']} {countries[i]['population']}")
    i+=1
    
