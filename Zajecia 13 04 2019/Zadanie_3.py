class ElectricCar:

    def __init__(self, range):
        self.range = range
        self.passed = 0

    def drive(self, dist):
        if (self.passed + dist) > self.range:
            dist_left = self.range - self.passed
            self.passed = self.range
            return dist_left
        else:
            self.passed += dist
        return self.passed

    def charge(self):
        self.passed = 0


def test_electric_car_init():
    car1 = ElectricCar(100)
    assert car1.range == 100
    assert car1.passed == 0


def test_electric_car_drive():
    car1 = ElectricCar(100)
    assert car1.drive(70) == 70
    assert car1.drive(50) == 30
    assert car1.drive(50) == 0
    assert car1.drive(50) == 0
    assert car1.passed == 100


def test_electric_car_charge():
    car1 = ElectricCar(100)
    car1.drive(70)
    car1.drive(50)
    car1.drive(50)
    car1.charge()
    assert car1.drive(50) == 50
    car1.charge()
    assert car1.drive(200) == 100
    assert car1.passed == 100


def test_electric_car_finall():
    car1 = ElectricCar(200)
    assert car1.drive(210) == 200
    car1.charge()
    assert car1.drive(210) == 200
    assert car1.drive(2100) == 0
    car1.charge()
    assert car1.range == 200
    assert car1.passed == 0
