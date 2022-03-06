import unittest

from ..equation_solver import solve_equation
from ..equation_solver import check_equation


class SolveEquationTestCase(unittest.TestCase):
    def test_one_root(self):
        self.assertEqual(solve_equation(1, 2, 1), [-1, -1])

    def test_check_equation(self):
        self.assertTrue(check_equation('x+1=0'))
        self.assertFalse(check_equation('x+y=1'))
        self.assertFalse(check_equation('=1'))
        self.assertFalse(check_equation('x+1='))


if __name__ == '__main__':
    unittest.main()
