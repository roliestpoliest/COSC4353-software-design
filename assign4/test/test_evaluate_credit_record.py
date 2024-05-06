import unittest
import sys
sys.path.append('src')
from status import Status
from application import Application
from criteria.evaluate_credit_record import evaluate_credit_record

class CreditRecordCriteriaTests(unittest.TestCase):
  def test_credit_record_criteria_passes(self):
    self.assertEqual((Status.PASS, "Applicant has a good credit record."), evaluate_credit_record(Application(has_good_credit_record=True)))

  def test_credit_record_criteria_fails(self):
    self.assertEqual((Status.FAIL, "Applicant has a poor credit record."), evaluate_credit_record(Application(has_good_credit_record=False)))

if __name__ == '__main__':
  unittest.main()
