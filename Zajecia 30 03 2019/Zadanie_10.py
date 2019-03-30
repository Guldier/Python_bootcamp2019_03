#Zliczanie wystapien liter/ w zaddaniu bylo znaków
while True:
    napis = input("Wprowadz napis").lower() #dla poprawnosci zadania bez .lower()
    if napis=="k":
        break

    wystapienia = {}

    for i in napis:
        wystapienia[i] = wystapienia.get(i,0)+1

    for j in wystapienia:
        print(wystapienia[j],"-",j)