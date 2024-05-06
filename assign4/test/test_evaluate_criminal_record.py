import unittest
import sys
sys.path.append('src')
from status import Status
from application import Application
from criteria.evaluate_criminal_record import evaluate_criminal_record

class CriminalRecordCriteriaTests(unittest.TestCase):
  def test_criminal_record_criteria_passes(self):
    self.assertEqual((Status.PASS, "Applicant has no criminal record."), evaluate_criminal_record(Application(has_no_criminal_record=True)))
    
  def test_criminal_record_criteria_fails(self):
    self.assertEqual((Status.FAIL, "Applicant has a criminal record."), evaluate_criminal_record(Application(has_no_criminal_record=False)))

if __name__ == '__main__':
  unittest.main()
