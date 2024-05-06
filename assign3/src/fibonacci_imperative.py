from validate_position import validate_position

@validate_position
def fibonacci_imperative(position):
  previous, current = 1, 1
  
  for _ in range(1, position):
    previous, current = current, previous + current

  return current
