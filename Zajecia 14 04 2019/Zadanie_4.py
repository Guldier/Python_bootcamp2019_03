class Basket:
    def __init__(self):
        self.entries = []

    def add_produckt(self, product, qty):
        new_entry = BasketEntry(product, qty)
        nowy = True
        for element in self.entries:
            if element.product._name == new_entry.product._name:
                pos = self.entries.index(element)
                self.entries[pos].qty += new_entry.qty
                nowy = False
                break
            else:
                nowy = True
        if nowy is True:
            self.entries.append(new_entry)

    def count_total_price(self):
        total_price = 0
        for i in self.entries:
            total_price += i.entry_price()
        return total_price

    def sum(self):
        total = 0
        for i in self.entries:
            total += i.entry_price()
        return total

    def generate_report(self):
        print(f'Produkty w koszyku:')
        for entry in self.entries:
            print(f'- {entry.product._name}({entry.product._id}), cena: {entry.product._price} x {entry.qty}')
        print(f"W sumie: {basket.sum()}")


class BasketEntry:
    def __init__(self, product, qty):
        self.product = product
        self.qty = qty

    def entry_price(self):
        return self.product._price * self.qty


class Products:
    def __init__(self, id, name, price):
        self._id = id
        self._name = name
        self._price = price


basket = Basket()
product1 = Products(1, 'Woda', 10.00)
product2 = Products(2, 'Chleb', 2.3)
product3 = Products(3, 'Ser', 8)

basket.add_produckt(product2, 2)
basket.add_produckt(product1, 5)
basket.add_produckt(product1, 5)
basket.add_produckt(product2, 2)
basket.add_produckt(product3, 10)
basket.add_produckt(product3, 10)
basket.add_produckt(product3, 10)
basket.add_produckt(product3, 10)
basket.add_produckt(product3, 10)

basket.generate_report()


def test_basket_init():
    basket = Basket()
    product1 = Products(1, 'Woda', 10.00)
    assert product1._id == 1
    assert product1._name == 'Woda'
    assert product1._price == 10.00


def test_basket_add():
    basket = Basket()
    product1 = Products(1, 'Woda', 10.00)
    addproduct = BasketEntry(product1, 5)
    assert addproduct.product == product1
    assert addproduct.qty == 5


def test_add_product_to_basket():
    basket = Basket()
    product1 = Products(1, 'Woda', 10.00)
    basket.add_produckt(product1, 5)
    assert basket.count_total_price() == 50


def test_add_multiple_product_to_basket():
    basket = Basket()
    product1 = Products(1, 'Woda', 10.00)
    basket.add_produckt(product1, 5)
    basket.add_produckt(product1, 5)
    assert basket.count_total_price() == 100
