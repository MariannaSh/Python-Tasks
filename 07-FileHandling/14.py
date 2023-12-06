file = open("shopping.txt", 'a') #Откроет для добавления нового содержимого. Создаст новый файл для записи, если не найдет с указанным именем.
read_product = True
counter = 0
while read_product:
    product = input("Enter product name: ")
    if product != "": #если вводимое число в кл не пустое, то добавляем
        counter += 1
        file.write(f"{counter}. {product}\n")
    else:
        read_product = False
file.close()
