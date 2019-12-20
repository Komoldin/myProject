import unittest
from Milli import Person


class Test(unittest.TestCase):

    def test_class(self):
        p1 = Person("Kamaldin", 20)
        self.assertEqual(p1.name, "Kamaldin")
        self.assertEqual(p1.age, 20)


if __name__ == '__main__':
    unittest.main()
