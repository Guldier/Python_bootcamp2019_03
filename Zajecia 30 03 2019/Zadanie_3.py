text = "<kota>, a kot ma Alę"

podzielony = text.split("<")
podzielony = podzielony[1].split(">")

dlugosc_napisu = len(podzielony[0])

print(f"Napis w nawiasach: {podzielony[0]} ma {dlugosc_napisu} liter")

w_nawiasach = 0
zliczaj = False

for v in text:
    if v == "<":
        zliczaj = True
        continue
    elif v == ">":
        zliczaj = False
    if zliczaj is True:
        w_nawiasach+=1
print("Metoda 2")
print(w_nawiasach)
