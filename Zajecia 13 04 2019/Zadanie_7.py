class Employee:
    __time = 0

    def __init__(self, first_name, last_name, rate_per_hour):
        self.first_name = first_name
        self.last_name = last_name
        self.rate_per_hour = rate_per_hour

    def pay_salary(self):
        if self.__time > 8:
            payment = self.rate_per_hour * 8 + self.rate_per_hour * 2 * (self.__time - 8)
        else:
            payment = self.rate_per_hour * self.__time
        self.__time = 0
        return payment

    def register___time(self, t):
        self.__time = self.__time + t


class PremiumEmployee(Employee):
    def __init__(self, first_name, last_name, rate_per_hour):
        super().__init__(first_name, last_name, rate_per_hour)
        self.bonuses = 0

    def give_bonus(self, bonus):
        self.bonuses += bonus

    def pay_salary(self):
        to_pay = super().pay_salary() + self.bonuses
        self.bonuses = 0
        return to_pay

def test_premium_employee_initialozation():
    employee = PremiumEmployee('Andrzej','Kowalski',100.0)
    assert employee.first_name == 'Andrzej'
    assert employee.bonuses == 0
    employee.give_bonus(1000)
    employee.register___time(5)
    assert employee.bonuses == 1000
    assert employee.pay_salary() == 1500


def test_employee_initialozation():
    employee = Employee('Jan', 'Nowak', 100.0)
    assert employee.first_name == 'Jan'
    assert employee.last_name == 'Nowak'
    assert employee.rate_per_hour == 100.0


def test_employee_register___time():
    employee = Employee('Jan', 'Nowak', 100.0)

    employee.register___time(5)

    employee.register___time(5)


def test_employee_pay_salary():
    employee = Employee('Jan', 'Nowak', 100.0)

    assert employee.pay_salary() == 0
    employee.register___time(5)
    assert employee.pay_salary() == 500

    assert employee.pay_salary() == 0
    employee.register___time(5)
    employee.register___time(5)
    assert employee.pay_salary() == 1200
    employee.register___time(20)
    assert employee.pay_salary() == 3200
    assert employee.pay_salary() == 0
