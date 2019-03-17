liczba = float(input("Podaj liczbe: "))

print(f"Podzielna przez 2,3 i wieksza od 10 lub jest to 7: {(liczba%2==0 and liczba%3==0 and liczba>10) or liczba==7}")