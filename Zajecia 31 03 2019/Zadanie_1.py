
def zwroc_wiecej_niz(tekst, ile_wystapien):
    do_zwrocenia = set()
    for litera in set(tekst):
        if tekst.count(litera) >= ile_wystapien:
            do_zwrocenia.add(litera)
    return do_zwrocenia

    assert zwroc_wiecej_niz("aaaaabcde", 3) == {'a'}
    assert zwroc_wiecej_niz("aaabbb",2) == {'a','b'}


def test_zwroc_wiecej_niz_dla_pustego_setu():
    assert zwroc_wiecej_niz("", 1) == set()
