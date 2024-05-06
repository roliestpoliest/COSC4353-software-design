import unittest
import sys
from parameterized import parameterized
sys.path.append('src')
from fetch_number_of_perfect_numbers import fetch_number_of_perfect_numbers

class FetchPerfectNumbersTests(unittest.TestCase):
  @parameterized.expand([
    (1, 0),
    (2, 0),
    (3, 0),
    (4, 0),
    (5, 0)
  ])
  def test_count_number_of_perfect_numbers_numbers_returns_zero(self, limit, expected_number_of_perfect_numbers):
    self.assertEqual(expected_number_of_perfect_numbers, fetch_number_of_perfect_numbers(limit))

  @parameterized.expand([
    (6, 1),
    (10, 1), 
    (28, 2), 
    (30, 2)
  ])
  def test_count_number_of_perfect_numbers_returns_number_of_perfect_numbers(self, limit, expected_number_of_perfect_numbers):
    self.assertEqual(expected_number_of_perfect_numbers, fetch_number_of_perfect_numbers(limit))
