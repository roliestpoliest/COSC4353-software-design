import unittest
import sys
sys.path.append('src')
from fibonacci_recursion import fibonacci_recursion
from test_fibonacci_base import FibonacciBaseTests

class FibonacciRecursionTests(FibonacciBaseTests, unittest.TestCase):
  def get_fibonacci_function(self):
    return fibonacci_recursion
