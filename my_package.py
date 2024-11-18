'''
from .module1 import func1
from .module2 import func2'''

__all__ = ['func1', 'func2']

import unittest
from my_package.module1 import func1

class TestModule1(unittest.TestCase):
    def test_func1(self):
        self.assertEqual(func1(), "Function 1 from module 1")

if __name__ == '__main__':
    unittest.main()









