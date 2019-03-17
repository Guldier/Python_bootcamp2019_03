wymiar=(input("Podaj wymiar po przeicku: "))
a,b,c = wymiar.split(",")
a,b,c = int(a),int(b),int(c)
objetosc = a*b*c

print(f"Objetosc jest wieksza od litra: {objetosc>1000} ")

