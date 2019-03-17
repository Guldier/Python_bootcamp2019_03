# spis_liczb = (11,21,31,41,51,61,71,81,91,111)
#
# print(spis_liczb[1])
# print(spis_liczb[-2])
# print(spis_liczb[2:7])
# print(spis_liczb[::3])
# print(spis_liczb[::-2])

x = []

while True:
    
    try:
        x.append(int(input("Wprowadz liczbe: ")))
        print("Lista: ", x)
    except:
        print()
    if len(x) >= 10:
        break

print(f"Suma = {sum(x)}")
