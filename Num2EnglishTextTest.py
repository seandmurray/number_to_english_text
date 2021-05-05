import unittest
from Num2EnglishText import Num2EnglishText


class Num2EnglishTextTest (unittest.TestCase):

    def setUp(self):
        self.__num2EnglishText = Num2EnglishText()

    def test_digit_min(self):
        value = 1
        expected = 'one'
        test = self.__num2EnglishText.process(value)
        self.assertEqual(test, expected)

    def test_digit_max(self):
        value = 9
        expected = 'nine'
        test = self.__num2EnglishText.process(value)
        self.assertEqual(test, expected)

    def test_teen_min(self):
        value = 10
        expected = 'ten'
        test = self.__num2EnglishText.process(value)
        self.assertEqual(test, expected)

    def test_teen_max(self):
        value = 19
        expected = 'nineteen'
        test = self.__num2EnglishText.process(value)
        self.assertEqual(test, expected)

    def test_twenties_min(self):
        value = 20
        expected = 'twenty'
        test = self.__num2EnglishText.process(value)
        self.assertEqual(test, expected)

    def test_twenties_max(self):
        value = 99
        expected = 'ninety nine'
        test = self.__num2EnglishText.process(value)
        self.assertEqual(test, expected)

    def test_hundreds_min(self):
        value = 100
        expected = 'one hundred'
        test = self.__num2EnglishText.process(value)
        self.assertEqual(test, expected)

    def test_hundreds_mid(self):
        value = 123
        expected = 'one hundred twenty three'
        test = self.__num2EnglishText.process(value)
        self.assertEqual(test, expected)

    def test_hundreds_max(self):
        value = 999
        expected = 'nine hundred ninety nine'
        test = self.__num2EnglishText.process(value)
        self.assertEqual(test, expected)

    def test_thousands_min(self):
        value = 1000
        expected = 'one thousand'
        test = self.__num2EnglishText.process(value)
        self.assertEqual(test, expected)

    def test_thousands_mid(self):
        value = '4,567'
        expected = 'four thousand five hundred sixty seven'
        test = self.__num2EnglishText.process(value)
        self.assertEqual(test, expected)

    def test_thousands_max(self):
        value = '999,999'
        expected = 'nine hundred ninety nine thousand nine hundred ninety nine'
        test = self.__num2EnglishText.process(value)
        self.assertEqual(test, expected)

    def test_millions_min(self):
        value = '1,000,000'
        expected = 'one million'
        test = self.__num2EnglishText.process(value)
        self.assertEqual(test, expected)

    def test_millions_mid(self):
        value = '8,123,456'
        expected = 'eight million one hundred twenty three thousand four hundred fifty six'
        test = self.__num2EnglishText.process(value)
        self.assertEqual(test, expected)

    def test_millions_max(self):
        value = '999,999,999'
        expected = 'nine hundred ninety nine million nine hundred ninety nine thousand nine hundred ninety nine'
        test = self.__num2EnglishText.process(value)
        self.assertEqual(test, expected)


if __name__ == '__main__':
    unittest.main()
