tablica = [9,1,6,8,4,3,2,0]

for i in range(0,len(tablica),1):
    minimum = min(tablica[i:])
    tablica.remove(minimum)
    tablica.insert(i,minimum)
    print(tablica)
#assert lista ==[0,1,2,3,4,6,8,9]

print("INNA OPCJA")
print("======================================")
tablica = [9,1,6,8,4,3,2,0]
tablica1=[]

indeks = 0
for i in tablica:
    minimum = i
    for j in tablica:
        if j<i:
            minimum = tablica[j]
    tablica.remove(minimum)
    tablica.insert(indeks,minimum)
    indeks+=1
    print(tablica)