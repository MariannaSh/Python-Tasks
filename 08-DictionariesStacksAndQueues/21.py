import csv
import json

with open('text.csv','r') as file:
    data=[]
    json_file=open('product.json','w')
    reader = csv.DictReader(file)
    for line in reader:
        data.append(line)
    json_file.write(json.dumps(data, indent=4))
