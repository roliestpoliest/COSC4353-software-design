import unittest
import sys
sys.path.append('src')
from fibonacci_functional import fibonacci_functional
from test_fibonacci_base import FibonacciBaseTests

class FibonacciFunctionalTests(FibonacciBaseTests, unittest.TestCase):
  def get_fibonacci_function(self):
    return fibonacci_functional
