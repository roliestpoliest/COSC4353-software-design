def get_factors(number):
  return [i for i in range(1, number+1) if number % i == 0]

def check_if_twice_the_number(number, factor_sum):
  return factor_sum/number == 2

def check_if_perfect_number(number):
  return check_if_twice_the_number(number, sum(get_factors(number)))
