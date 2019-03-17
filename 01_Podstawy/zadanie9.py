import datetime
rok = int(input("Podaj rok urodzenia: "))
wiek = datetime.datetime.now().year - rok

if wiek >= 18:
    print("Jesteś pełnoletni")
else:
    print("Nie jesteś pełnopletni")
