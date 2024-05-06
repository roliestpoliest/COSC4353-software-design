import unittest
import sys
sys.path.append('src')
from application import Application
from fetch_criterion import fetch_criterion
from criteria.evaluate_employment import evaluate_employment
from criteria.evaluate_criminal_record import evaluate_criminal_record

class FetchCriterionTests(unittest.TestCase):
  def test_fetch_criterion_gets_employment_criteria_pass(self):
    criterion = fetch_criterion('employment')(Application(has_employment=True))
    pass_has_employment = evaluate_employment(Application(has_employment=True))
    
    self.assertEqual(pass_has_employment, criterion)
    
  def test_fetch_criterion_gets_criminal_record_criteria_fail(self):
    criterion = fetch_criterion('criminal_record')(Application(has_no_criminal_record=False))
    fail_has_criminal_record = evaluate_criminal_record(Application(has_no_criminal_record=False))

    self.assertEqual(fail_has_criminal_record, criterion)

if __name__ == '__main__':
  unittest.main()
