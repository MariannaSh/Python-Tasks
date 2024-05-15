import json

with open('euro.json','r') as file:
    data=json.loads(file.read())
file.close()

print("Date        Buying Rate     Selling Rate")
print("========================================")

for line in data["rates"]:
    print(line["effectiveDate"], "  ",line["ask"],  "       ", line["bid"])