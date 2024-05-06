import unittest
import sys
sys.path.append('src')
from fibonacci_imperative import fibonacci_imperative
from test_fibonacci_base import FibonacciBaseTests

class FibonacciImperativeTests(FibonacciBaseTests, unittest.TestCase):
  def test_canary(self):
    self.assertTrue(True)

  def get_fibonacci_function(self):
    return fibonacci_imperative
