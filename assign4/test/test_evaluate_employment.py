import unittest
import sys
sys.path.append('src')
from status import Status
from application import Application
from criteria.evaluate_employment import evaluate_employment

class EmploymentCriteriaTests(unittest.TestCase):
  def test_employment_criteria_passes(self):
    self.assertEqual((Status.PASS, "Applicant has had previous employment."), evaluate_employment(Application(has_employment=True)))
    
  def test_employment_criteria_fails(self):
    self.assertEqual((Status.FAIL, "Applicant has no previous employment."), evaluate_employment(Application(has_employment=False)))

if __name__ == '__main__':
  unittest.main()
