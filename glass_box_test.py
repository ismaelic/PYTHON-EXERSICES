import unittest


def he_is_older(age):
    if age >= 18:
        return True
    else:
        return False


class GlassBoxTest(unittest.TestCase):

    def he_is_older_test(self):
        age = 20

        answer = he_is_older(age)

        self.assertEqual(answer, True)

    def he_a_minor_test(self):
        age = 15

        answer = he_is_older(age)

        self.assertEqual(answer, False)


if __name__ == '__main__':
    unittest.main()
