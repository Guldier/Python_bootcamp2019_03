from copy import deepcopy
import unittest

from add import add


class AddTests(unittest.TestCase):

    """Tests for add."""

    def test_single_items(self):
        self.assertEqual(add([[5]], [[-2]]), [[3]])

   # def test_two_by_two_matrixes(self)

if __name__ == "__main__":
    unittest.main(verbosity=2)
