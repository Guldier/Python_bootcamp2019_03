# slownik = dict([("a",1),("b",2)])
# slownik1 = {"a":1,"b":2}
#
# slownik1['c'] = slownik1.get('c',1)
#
# print(slownik)
# print(slownik1)

#Słowniki
produkty = {'ziemniaki': 1.99,
            'bataty': 5.99,
            'pomidory': 6}
ile_produktow = {'ziemniaki': 10,
                 'bataty': 10,
                 'pomidory': 10}
koszyk = {}
print("Start. Kasa[k]/Magazyn[m]")
while True:
    mode = input("Mode: ").lower()

    if mode=="k":
        #Wypisanie produktów
        print("Nasze produkty: ")
        for i in produkty:
            print(f"- {i} w cenie: {produkty[i]} za kg")
        #Obsługa sklepu
        while True:
            co_kupic = input("Co chesz kupic? [Koniec - k]")
            if co_kupic.upper() == 'K':
                break
            while True:
                if co_kupic in produkty:
                    ile = (int)(input("Ile chesz kupic? "))
                    if ile_produktow[co_kupic] < ile:
                        print(f"Nie mamy tyle {co_kupic}")
                        continue

                    koszyk[co_kupic] = koszyk.get(co_kupic, 0) + ile
                    print(f"Koszt za {ile} {co_kupic} wynosi: {round(ile * produkty[co_kupic],2)}")
                    break
                else:
                    print("nie ma takiego produktu")
                    break
                break

        #podsymowanie
        suma=0
        print("Koszyk:")
        for i in koszyk:
            print(f"- {i} za : {koszyk[i]*produkty[i]} zł")
            ile_produktow[i] = ile_produktow[i]-koszyk[i]
            suma+= koszyk[i]*produkty[i]
        print("=============================")
        print(f"Suma: {sum(koszyk.values())}")
        print("*****************")
        print("Bajo")



    elif mode=="m":
        produkt_do_dodania = input("Co dodajemy?: ")
        ile_dodajemy = (int)(input("Ile dodajemy?: "))
        if produkt_do_dodania not in produkty:
            cena_za_kilo = float(input("Ile za kilo?:"))
            produkty[produkt_do_dodania] = cena_za_kilo
        ile_produktow[produkt_do_dodania] = ile_produktow.get(produkt_do_dodania,0) + ile_dodajemy
        print("Stan magazynu")
        for ilosc in ile_produktow:
            print(f" -{ilosc} : {ile_produktow[ilosc]}")
    else:
        print("KOniec")