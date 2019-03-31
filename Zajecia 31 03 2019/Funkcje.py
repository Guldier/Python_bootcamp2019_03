# def hello():
#     return True
#
#
# imie = ["d", "r", "t"]
#
# if hello():
#     print("tak")


def czy_jest_pierwsza(liczba):
    for i in range(2, liczba):
        if liczba % i == 0:
            return False
    return True


def test_czy_jest_pierwsza_dla_liczby_pierwszej():
    assert czy_jest_pierwsza(5) is True
    assert czy_jest_pierwsza(1) is True


def test_czy_jest_pierwsza_dla_niepierwszych():
    assert czy_jest_pierwsza(4) is False
