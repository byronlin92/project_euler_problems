import unittest

def fib_solution_1(index):
    if (index < 0):
        return 'incorrect input'
    elif (index == 0):
        return 0
    elif (index == 1):
        return 1
    else:
        return fib_solution_1(index-1) + fib_solution_1(index-2)


def fib_solution_2(index):
    a = 0
    b = 1
    if (index < 0):
        return 'incorrect input'
    elif (index == 0):
        return a
    elif (index == 1):
        return b
    else:
        for i in range(1, index):
            c = a + b
            a = b
            b = c
        return c


def fib_solution_3(index):
    a = 0
    b = 1
    if (index < 0):
        return 'incorrect input'
    elif (index == 0):
        return 0
    elif (index == 1):
        return 1
    else:
        while (index > 1):
            c = a + b
            a = b
            b = c
            index -= 1
        return b


def even_fibonacci_numbers(index):
    a = 0
    b = 1
    sum = 0
    if (index < 0):
        return 'incorrect input'
    elif (index <= 1):
        return 0
    else:
        for i in range(1, index):
            c = a + b
            a = b
            b = c
            if (c % 2 == 0):
                sum = sum + c
        return sum


def even_fibonacci_numbers_less_than_four_million():
    a = 0
    b = 1
    c = 0
    sum = 0
    while (c <= 4000000):
        c = a + b
        a = b
        b = c
        if (c % 2 == 0):
            sum = sum + c
    return sum


class TestEvenFibonacciNumbers(unittest.TestCase):
    def test_input_10(self):
        result = even_fibonacci_numbers_less_than_four_million()
        self.assertEqual(result, 4613732)


if __name__ == "__main__":
    unittest.main()

