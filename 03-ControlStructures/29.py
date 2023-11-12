
wash={
    'jacket':40,
    'underwear':70,
    'shoes':20
}

washing_product = 'shoes'
rinse = True
spin =False

total=wash[washing_product]
if rinse == True:
    total+=15
if spin == True:
    total+=9

print(f'Total washing time: {total} minutes')