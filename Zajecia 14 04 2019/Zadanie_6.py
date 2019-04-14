class Vector:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __str__(self):
        return f'Vector(x={self._x}, y={self._y})'

    def __add__(self, other):
        return Vector(self._x + other._x, self._y + other._y)

    def __mul__(self, other):
        return Vector(self._x * other, self._y * other)

    def __rmul__(self, other):
        return self * other

    def __lt__(self, other):
        return (self._x ** 2 + self._y ** 2) < (other._x ** 2 + other._y ** 2)

    def __eq__(self, other):
        return (self._x ** 2 + self._y ** 2) == (other._x ** 2 + other._y ** 2)

if __name__ == "__main__":
    v1 = Vector(1, 2)
    print(v1)

    print(v1 + v1)
    print(v1 * 3)
    print(3 * v1)
    print(v1 == Vector(2,1))
