miasto_a = input("Podaj miasto A: ")
miasto_b = input("Podaj miasto B: ")
dystans = int(input(f"Podaj dystans miedzy {miasto_a}-{miasto_b}: "))
cena_paliwa = float(input("Podaj cene paliwa: "))
spalanie = float(input("Podaj spalanie na 100 km: "))

koszt = (dystans/100)*spalanie*cena_paliwa

print(f"Koszt przejazdu {miasto_a}-{miasto_b} to {koszt:.2f} PLN")