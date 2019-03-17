pierwsza = float(input("Liczba 1: "))
druga = float(input("Liczba 2: "))
operacja = input("Podaj rodzaj operacji: ")

if operacja == "+":
    print("Wynik: ", pierwsza + druga)
elif operacja == "-":
    print("Wynik: ", pierwsza - druga)
elif operacja == "*":
    print("Wynik: ", pierwsza * druga)
elif operacja == "/":
    if druga == 0:
        print("Nie mozna dzielic przez zero")
    else:
        print("Wynik: ", pierwsza / druga)
else:
    print("ŻODEN")
