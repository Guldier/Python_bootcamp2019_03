imie = str.capitalize(input("Podaj imie: "))
wzrost = float(input("Podaj wzrost: "))
waga = int(input("Podaj wage: "))

bmi = waga / (wzrost / 100) ** 2

print(imie)
print(wzrost)
print(bmi)
