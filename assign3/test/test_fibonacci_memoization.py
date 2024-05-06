import unittest
import sys
from time import time
sys.path.append('src')
from fibonacci_recursion import fibonacci_recursion
from fibonacci_memoization import fibonacci_memoization
from test_fibonacci_base import FibonacciBaseTests

class FibonacciMemoizationTests(FibonacciBaseTests, unittest.TestCase):
  def get_fibonacci_function(self):
    return fibonacci_memoization

  def measure_execution_time(self, fibonacci_function, position):
    start = time()
    fibonacci_function(position)

    return time() - start

  def test_memoization_at_least_ten_times_faster_than_recursion(self):
    self.assertLess((self.measure_execution_time(fibonacci_memoization, 30) * 10), self.measure_execution_time(fibonacci_recursion, 30))

  def test_memoization_not_significantly_faster_for_small_position_value(self):
    significant_difference_threshold = 0.0025

    self.assertLess(self.measure_execution_time(fibonacci_memoization, 3) - self.measure_execution_time(fibonacci_recursion, 3), significant_difference_threshold)
