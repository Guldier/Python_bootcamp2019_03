komenda = ""
liczba = 0
max = None
min = None

while True:
    komenda = input("Podaj liczbe: ")
    if komenda == "k":
        break
    elif komenda == "":
        print("Nie podałeś liczby")


    else:
        try:
            liczba = int(komenda)

            if max is None:
                max = liczba
            if min is None:
                min = liczba

            if liczba > max:
                max = liczba
            if liczba < min:
                min = liczba

        except:
            print("Noppe")

print(f"Max: {max} and Min: {min}")

print("Gracias")
