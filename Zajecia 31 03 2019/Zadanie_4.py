def splaszcz(lista):
    lista_wynik = []
    for el in range(len(lista)):
        if isinstance(lista[el], list):
            for el_rek in splaszcz(lista[el]):
                lista_wynik.append(el_rek)
        else:
            lista_wynik.append(lista[el])
    return lista_wynik


print(splaszcz([1, 2, 3, [4, 5, [6]], 7]))


def test_splaszcz_zadanie():
    assert splaszcz([1, 2, 3, [4, 5, [6]], 7]) == [1, 2, 3, 4, 5, 6, 7]


def test_splaszcz_pusta():
    assert splaszcz([]) == []


def test_splaszcz_plaska():
    assert splaszcz([1, 2, 3]) == [1, 2, 3]
