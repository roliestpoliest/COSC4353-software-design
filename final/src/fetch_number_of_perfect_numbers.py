from perfect_number import check_if_perfect_number

def fetch_number_of_perfect_numbers(limit):
  return sum([1 for i in range(1, limit+1) if check_if_perfect_number(i)])
