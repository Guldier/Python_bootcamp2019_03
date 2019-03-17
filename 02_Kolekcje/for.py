# x = [2, 3, 4, 5, 7, -3, 4, 5, -9, -20]
# dodatnie = []
# ujemne = []
# for i in x:
#     if i > 0:
#         dodatnie.append(i)
#     else:
#         ujemne.append(i)
# print(f"Dodatnie: {len(dodatnie)}")
# print(f"Ujemne: {len(ujemne)}")
ilosc = 0
for i in range(0, 101, 1):
    if i % 3 == 0 or i % 5 == 0:
        print(i)
        ilosc += 1
print(f"W przedziale 0-100 jest {ilosc} liczb podzielnych prz 3 lub 5")
