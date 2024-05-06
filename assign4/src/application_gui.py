from dataclasses import fields
from application import Application
from fetch_criterion import fetch_criterion
from fetch_criteria import fetch_criteria
from process_application import process_application

def list_criteria():
  print("\nApplication Criteria:")

  for count, criterion in enumerate(fetch_criteria(), start=1):
    print(f"  {count}. {criterion.capitalize().replace('_', ' ')}")

def get_criteria():
  selected_criteria_numbers = select_criteria()
  criteria_names = get_criteria_names_from_numbers(selected_criteria_numbers)
  
  return [fetch_criterion(criterion) for criterion in criteria_names]

def select_criteria():
  print("\nSelect number(s) from the list of criteria separated by one space ' '.")

  while True:
    try: 
      users_selected_criteria = input("  Enter criteria to check: ").strip()
      separated_criteria = [int(criterion) for criterion in users_selected_criteria.split(" ")]

      if is_valid_criteria(separated_criteria):
        return separated_criteria
      
      raise ValueError

    except ValueError:
      print("    Invalid input. Please select valid number(s) from the list of criteria separated by one space ' '.")

def is_valid_criteria(selected_criteria):
  criteria_count = len(list(fetch_criteria()))

  return all(1 <= criterion <= criteria_count for criterion in selected_criteria)

def get_criteria_names_from_numbers(numbers):
  criteria_names = list(fetch_criteria())

  return [criteria_names[number - 1] for number in numbers]

def create_application():
  application_values = {}
  application_fields = fields(Application)

  print("\nPlease provide 'Yes' or 'No' for the following application questions:")

  for field in application_fields:
    field_value = process_field_input(field.name.replace('_', ' '))
    application_values[field.name] = field_value

  return Application(**application_values)

def process_field_input(field_name):
  while True:
    try:
      field_value = input(f"  Applicant {field_name}? ").lower().strip()

      if field_value in ['yes', 'no']:
        return field_value == 'yes'
      
      raise ValueError

    except ValueError:
      print("    Invalid input. Please provide 'Yes' or 'No'.")

def process_and_display_results(application, criteria):
  status, message = process_application(application, *criteria)

  print(f"\nApplication Results: {status.name}" + f"\n  {message}")

def continue_processing():
  while True:
    try:
      continue_processing = input("\nProcess another application (yes/no)? ").lower().strip()
      
      if continue_processing == 'yes':
        return True
      elif continue_processing == 'no':
        return False
      
      raise ValueError

    except ValueError:
      print("  Invalid input. Please provide 'Yes' or 'No'.")

def process_applications_loop():
  continue_processing_applications = True

  while continue_processing_applications:
    list_criteria()

    criteria = get_criteria()
    application = create_application()

    process_and_display_results(application, criteria)

    continue_processing_applications = continue_processing()

if __name__ == '__main__':
  process_applications_loop()
