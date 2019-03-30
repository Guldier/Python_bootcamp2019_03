text = input("Give a text: ")

SAMOGLOSKI = "aeiouy"
licznik=0
for i in text.lower():
    if i in SAMOGLOSKI:
        licznik+=1
print("W tekscie: ",text,". Znajduje się: ",licznik, "samoglosek")