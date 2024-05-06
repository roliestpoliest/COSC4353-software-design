from fetch_number_of_perfect_numbers import fetch_number_of_perfect_numbers

def get_number_from_user():
  while True:
    try:
      number = int(input("Please enter a number greater than or equal to 1: "))
      return number
    except ValueError:
      print("Please enter a whole number")

def print_number_of_perfect_numbers(limit):
  number_of_perfect_numbers = fetch_number_of_perfect_numbers(limit)

  print(f"Here are the number of perfect numbers from 1 to {limit}: {number_of_perfect_numbers}")

if __name__ == "__main__":
  limit = get_number_from_user()
  print_number_of_perfect_numbers(limit)
