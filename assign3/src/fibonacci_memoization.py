from validate_position import validate_position
from fibonacci_recursion import fibonacci_recursion

@validate_position
def fibonacci_memoization(position, cache=None):
  cache = {0: 1, 1: 1} if cache == None else cache
  
  if position not in cache:
    cache[position] = fibonacci_recursion(position, lambda _: fibonacci_memoization(_, cache))
  
  return cache[position]
