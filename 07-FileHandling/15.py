# f = open("internetfile.txt")
# for line in f:
#      print(line, end="")
# f.close()

with open("internetfile.txt") as f:
    for line in f:
         print(line, end="")



     