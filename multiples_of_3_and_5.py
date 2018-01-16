import unittest

def sum_of_natural_numbers(input_num):
    sum = 0
    less_than_input = True
    multiples_of_3 = 1
    multiples_of_5 = 1
    while (less_than_input):
        if ((3 * multiples_of_3) < input_num):
            sum = sum + (3 * multiples_of_3)
            multiples_of_3 += 1
        elif ((5 * multiples_of_5) < input_num):
            sum = sum + (5 * multiples_of_5)
            multiples_of_5 += 1
        elif (((3 * multiples_of_3) >= input_num) and ((5 * multiples_of_5) >= input_num)):
            less_than_input = False

    return sum

class TestSumOfNaturalNumbers(unittest.TestCase):
    def test_input_10(self):
        result = sum_of_natural_numbers(10)
        self.assertEqual(result, 23)

    def test_input_0(self):
        result = sum_of_natural_numbers(0)
        self.assertEqual(result, 0)

    def test_input_3(self):
        result = sum_of_natural_numbers(3)
        self.assertEqual(result, 0)

    def test_input_4(self):
        result = sum_of_natural_numbers(4)
        self.assertEqual(result, 3)

    def test_input_6(self):
        result = sum_of_natural_numbers(6)
        self.assertEqual(result, 8)
        
if __name__ == "__main__":
    unittest.main()