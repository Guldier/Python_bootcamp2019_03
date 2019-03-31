def silnia(a):
    if a <= 0:
        return 1
    else:
        return silnia(a - 1) * a


print(f"Silnia = {silnia(3)}")


def test_silnia_1():
    assert silnia(5) == 5 * 4 * 3 * 2 * 1
    assert silnia(9) == 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1


def test_silnia_0():
    assert silnia(0) == 1
#
#
# def pri(lista):
#     if len(lista) == 1:
#         print(lista[0])
#     else:
#         print(lista[0])
#         pri(lista[1:])
#
# pri([10,20,30,40])