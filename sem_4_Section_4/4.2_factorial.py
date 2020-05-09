import unittest
def factorial(n):
    if n == 0:
        return 1
    return factorial(n-1)*n
def input_test():
    
    try:
       x = int(input('Введите число'))
       f = factorial(x)
       return f
    except(ValueError):
        print('Вы ввели неправильные данные')
    except:
        print('Ошибка')
class Test_factorial(unittest.TestCase):

    def test_1(self):
        self.assertEqual(factorial(5), 120)

    def test_2(self):
        self.assertEqual(factorial(5), 10)

    def test_3(self):
        self.assertEqual(factorial(1), 1)

    def test_4(self):
        self.assertEqual(factorial(3), 6)    
        
if __name__ == "__main__":
    unittest.main()
        
