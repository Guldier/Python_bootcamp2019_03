class Pies:
    # Atrybuty klasy
    liczba_nog = 4
    gatunek = "Canis Canis"

    def __init__(self, name, age, type):
        # Atrybuty instancji
        self.name = name
        self.age = age
        self.type = type
        self.behave = "friendly"

    # Metody instancji
    def human_age(self):
        return self.wiek * 7

    def say_hello(self):
        return f"Hello I'm {self.name} I'm {self.age} years old. I'm really {self.behave} like all {self.type}s are."


azor = Pies("Azor", 5, "Boxer")  # Instancja klasy Pies
reksio = Pies("Rex", 10, "Kundel")

print(azor.say_hello())


# azor.imie = "Azor"
# azor.wiek = "5"
# azor.rasa = "Bokser"
#
# reksio.imie = "Rex"
# reksio.wiek = 10
# reksio.rasa = "Kundel"
#
# print(azor.imie, azor.liczba_nog)
# print(reksio.imie, reksio.gatunek, reksio.ludzki_wiek())
