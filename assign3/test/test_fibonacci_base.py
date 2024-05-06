from parameterized import parameterized

class FibonacciBaseTests: 
  @parameterized.expand([
    (0, 1),
    (1, 1),
    (2, 2),
    (5, 8),
    (8, 34),
    (10, 89)
  ])
  def test_fibonacci_function(self, position, expected_fibonacci_value):
    self.assertEqual(self.get_fibonacci_function()(position), expected_fibonacci_value)

  def test_fibonacci_function_negative_position(self):
    self.assertRaises(ValueError, self.get_fibonacci_function(), -1)
