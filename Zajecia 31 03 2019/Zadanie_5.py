def formatuj(*args, **kwargs):
    caly_napis = []
    for napis in args:
        for el in kwargs:
            if "$" + el in napis:
                print(napis.replace(f"${el}", str(kwargs[el])))
    return "\n".join(caly_napis)


print(formatuj("koszt $cena PLN", "kwota $brutto brutto", cena=10, brutto=12.3))


def test_formatuj():
    assert formatuj("koszt $cena PLN", "kwota $brutto brutto", cena=10,
                    brutto=12.3) == "koszt 10 PLN\nkwota 12.3 brutto"
