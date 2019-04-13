class Product:

    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    def print_info(self):
        print(f'Product "{self.name}", id: {self.id}, price: {self.price} PLN')


product = Product(1, 'Water', 10.99)
product.print_info()


def test_product():
    product = Product(1, 'Water', 10.99)
    assert product.id == 1
    assert product.name == 'Water'
    assert product.price == 10.99

def test_product_product_info(capsys):
    product = Product(1, 'Water', 10.99)
    product.print_info()
    captured = capsys.readouterr()
    assert captured.out == 'Product "Water", id: 1, price: 10.99 PLN\n'