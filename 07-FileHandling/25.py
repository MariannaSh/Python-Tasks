import re

message = "Tuesday: 22C, Wednesday: 21C, Thursday: 26C "
temperatures = re.findall("\d{2}",message)


summa=0
for i in temperatures:
    summa+=int(i)
print(summa)