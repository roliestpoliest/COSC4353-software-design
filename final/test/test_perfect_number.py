import unittest
import sys
from parameterized import parameterized
sys.path.append('src')
from perfect_number import get_factors, check_if_twice_the_number, check_if_perfect_number

class PerfectNumberTests(unittest.TestCase):
  def test_canary(self):
    self.assertTrue(True)

  @parameterized.expand([
    (1, [1]),
    (2, [1, 2]),
    (3, [1, 3]),
    (4, [1, 2, 4]),
    (5, [1, 5]),
    (6, [1, 2, 3, 6]),
    (28, [1, 2, 4, 7, 14, 28])
  ])
  def test_get_factors_for_a_number_returns_a_list_of_factors(self, number, expected_factors):
    self.assertEqual(expected_factors, get_factors(number))

  @parameterized.expand([
    (1, 1),
    (2, 3),
    (3, 4),
    (4, 7),
    (5, 6)
  ])
  def test_check_if_twice_the_number_returns_false(self, number, sum):
    self.assertFalse(check_if_twice_the_number(number, sum))  

  @parameterized.expand([
    (6, 12),
    (28, 56)
  ])
  def test_check_if_twice_the_number_returns_true(self, number, sum):
    self.assertTrue(check_if_twice_the_number(number, sum))

  @parameterized.expand([
    (1),
    (2),
    (3),
    (4),
    (5),
  ])
  def test_check_if_perfect_number_returns_false(self, number):
    self.assertFalse(check_if_perfect_number(number))

  @parameterized.expand([
    (6),
    (28)
  ])
  def test_check_if_perfect_number_returns_true(self, number):
    self.assertTrue(check_if_perfect_number(number))
