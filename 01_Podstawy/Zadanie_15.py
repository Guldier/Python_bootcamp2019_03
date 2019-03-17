from random import randint

liczba_ruchow = 0
liczba_ruchow_cala = 0
x_gracza = randint(1, 10)
y_gracza = randint(1, 10)
x_skarbu = randint(1, 10)
y_skarbu = randint(1, 10)

min_liczba_ruchow = abs(x_skarbu - x_gracza) + abs(y_skarbu - y_gracza)

print(f"Pozycja: {x_gracza},{y_gracza}")

while True:
    ruch = input("Podaj ruch: ")

    odleg_przed = abs(x_skarbu - x_gracza) + abs(y_skarbu - y_gracza)

    if ruch == "w":
        y_gracza += 1
    elif ruch == "a":
        x_gracza -= 1
    elif ruch == "s":
        y_gracza -= 1
    elif ruch == "d":
        x_gracza += 1
    else:
        continue

    liczba_ruchow += 1
    liczba_ruchow_cala += 1

    if liczba_ruchow > 2 * min_liczba_ruchow:
        x_skarbu = randint(1, 10)
        y_skarbu = randint(1, 10)
        min_liczba_ruchow = abs(x_skarbu - x_gracza) + abs(y_skarbu - y_gracza)
        liczba_ruchow = 0
        print("Skarb zmienił położenie")

    print(f"Pozycja: {x_gracza},{y_gracza}")
    odleg_po = abs(x_skarbu - x_gracza) + abs(y_skarbu - y_gracza)

    if x_gracza < 0 or x_gracza > 10 or y_gracza < 0 or y_gracza > 10:
        print("Jestes po za planszą")
        break

    if x_gracza == x_skarbu and y_gracza == y_skarbu:
        print(f"Znalazłeś skarb. Liczba ruchów: {liczba_ruchow_cala}")
        break

    if odleg_przed < odleg_po:
        print("zimno")
    else:
        print("cieplo")


