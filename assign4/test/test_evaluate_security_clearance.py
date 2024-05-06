import unittest
import sys
sys.path.append('src')
from status import Status
from application import Application
from criteria.evaluate_security_clearance import evaluate_security_clearance

class SecurityClearanceCriteriaTests(unittest.TestCase):
  def test_security_clearance_criteria_passes(self):
    self.assertEqual((Status.PASS, "Applicant has security clearance."), evaluate_security_clearance(Application(has_security_clearance=True)))
    
  def test_security_clearance_criteria_fails(self):
    self.assertEqual((Status.FAIL, "Applicant has no security clearance."), evaluate_security_clearance(Application(has_security_clearance=False)))

if __name__ == '__main__':
  unittest.main()
