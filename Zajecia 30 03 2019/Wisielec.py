import random
slowa_do_odgadniecia = ["pierwsze","drugie"]
ktore_slowo = random.randint(0,len(slowa_do_odgadniecia)-1)
slowo = slowa_do_odgadniecia[ktore_slowo]
print(slowo)

zakryj=0

ukryj=list(slowo)
ile_liter = len(ukryj)

if ile_liter==3:
    zakryj=1
elif ile_liter==4:
    zakryj=2
else:
    zakryj=3

while zakryj!=0:
    ktora_litera=random.randint(0,ile_liter)
    if ukryj[ktora_litera]!="_":
        ukryj[ktora_litera]="_"
        zakryj-=1

print(ukryj,ile_liter)