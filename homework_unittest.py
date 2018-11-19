# test_warikan.py

import unittest


def warikan(amount, number_of_people):
    quotient = amount // number_of_people
    remainder = amount % number_of_people

    return f"1人あたり: {quotient}円, 端数: {remainder}円"


class TestWarikan(unittest.TestCase):
    def test_割り切れるパターン(self):
        actual = warikan(amount = 1500, number_of_people = 3)


        expected = "1人あたり: 500円, 端数: 0円"
        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()
