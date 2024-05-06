from validate_position import validate_position

@validate_position
def fibonacci_recursion(position, fibonacci_function=lambda _: fibonacci_recursion(_)):
  return 1 if position < 2 else fibonacci_function(position - 1) + fibonacci_function(position - 2)
