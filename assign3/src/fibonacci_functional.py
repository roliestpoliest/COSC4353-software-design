from validate_position import validate_position
from functools import reduce

@validate_position
def fibonacci_functional(position):
  return reduce(lambda pair, _: (pair[1], sum(pair)), range(position - 1), [1, 1])[1]
