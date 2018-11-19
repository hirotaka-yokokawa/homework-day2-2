import unittest

from warikan import warikan


class TestWarikan(unittest.TestCase):
    def test_割り切れるパターン(self):
        self.assertEqual("1人あたり: 500円, 端数: 0円", warikan(amount=1500, number_of_people=3))

    def test_端数がでるパターン(self):
        self.assertEqual("1人あたり: 666円, 端数: 2円", warikan(amount=2000, number_of_people=3))


if __name__ == "__main__":
    unittest.main()
