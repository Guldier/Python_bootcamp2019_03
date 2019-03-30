liczby = [1, 2, 44, 8, 0, 12, 44]
print(liczby)

max = max(liczby)
min = min(liczby)

index_max = []
index_min = []

for i, v in enumerate(liczby):
    if v == max:
        index_max.append(i)
    elif v == min:
        index_min.append(i)

for i in index_max:
    liczby[i] = min
for i in index_min:
    liczby[i] = max

print(liczby)
