tekst = '<<ala ma <kota> a kot> ma ale'
def zliczanie_w_nawiasach(tekst, nawias_otwierajacy='<', nawias_zamykajacy='>'):

    while tekst.count(nawias_otwierajacy) != tekst.count(nawias_zamykajacy):
        while True:
            if tekst.count(nawias_otwierajacy) > tekst.count(nawias_zamykajacy):
                for i in range(len(tekst)):
                    if tekst[i-1] == nawias_otwierajacy:
                        tekst= tekst[:i-1] + tekst[i:]
                        break
            elif tekst.count(nawias_otwierajacy) < tekst.count(nawias_zamykajacy):
                for j in range(len(tekst),1,-1):
                    if tekst[j-1] == nawias_zamykajacy:
                        tekst = tekst[:j-1] + tekst[j:]
                        break
            else:
                break


    poziom_zagniezdzenia = tekst.count(nawias_otwierajacy)

    zliczone = 0
    poziom = 0

    for litera in tekst:
        if litera == nawias_otwierajacy:
            poziom += 1
            continue
        elif litera == nawias_zamykajacy:
            poziom -= 1
            continue
        if poziom > 0:
            zliczone += poziom
    return zliczone

print(zliczanie_w_nawiasach(tekst),tekst)

def test_zliczanie_w_nawiasach():
    assert zliczanie_w_nawiasach('ala ma <kota> a kot ma ale') == 4


def test_zliczanie_w_nawiasach_2():
    assert zliczanie_w_nawiasach('ala[kota [a kot]] ma [ale]', '[', ']') == 18


def test_zliczanie_w_nawiasach_3():
    assert zliczanie_w_nawiasach('a <a<a<a>>>') == 6
