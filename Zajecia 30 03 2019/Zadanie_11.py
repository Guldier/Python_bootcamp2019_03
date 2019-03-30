# zmienne

wprowadzone_liczby = set()

# Petla glowna

while True:
    wpisane = input("Wprowadz liczbe: ")  # Poddaj wartosc
    try:
        wprowadzone_liczby.add(int(wpisane))
    except:
        break
print(f"Unikalnych: {len(wprowadzone_liczby)}")
print(f"Parzystych: {len(wprowadzone_liczby & set(range(0, 100, 2)))}")
