import unittest


def sum(element1, element2):
    return element1 + element2


class BlackBoxTest(unittest.TestCase):

    def test_sum(self):
        num_1 = 10
        num_2 = 5

        answer = sum(num_1, num_2)

        self.assertEqual(answer, 15)

    def test_sum_negative(self):
        num_1 = -10
        num_2 = -7

        answer = sum(num_1, num_2)

        self.assertEqual(answer, -17)


if __name__ == '__main__':
    unittest.main()
