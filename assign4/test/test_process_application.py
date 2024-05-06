import unittest
import sys
sys.path.append('src')
from status import Status
from application import Application
from process_application import process_application

class ProcessApplicationTests(unittest.TestCase):    
  def test_canary(self):
    self.assertTrue(True)

  def test_process_application_with_no_criteria_passes(self):
    self.assertEqual((Status.PASS, "Nothing to check"), process_application(Application())) 
    
  def test_process_application_with_employment_passes(self):
    pass_has_employment = lambda _: (Status.PASS, "Applicant has had previous employment.")
    
    self.assertEqual((Status.PASS, "Applicant has had previous employment."), process_application(Application(), pass_has_employment))
  
  def test_process_application_with_no_employment_fails(self):
    fail_has_no_employment = lambda _: (Status.FAIL, "Applicant has no previous employment.")

    self.assertEqual((Status.FAIL, "Applicant has no previous employment."), process_application(Application(), fail_has_no_employment))

  def test_process_application_with_employment_and_no_criminal_records_passes(self):
    pass_has_employment = lambda _: (Status.PASS, "Applicant has had previous employment.")
    pass_has_no_criminal_record = lambda _: (Status.PASS, "Applicant has no criminal records.")

    self.assertEqual((Status.PASS, "Applicant has had previous employment. Applicant has no criminal records."), process_application(Application(), pass_has_employment, pass_has_no_criminal_record))

  def test_process_application_with_no_employment_and_no_criminal_records_fails(self):
    fail_has_no_employment = lambda _: (Status.FAIL, "Applicant has no previous employment.")
    pass_has_no_criminal_record = lambda _: (Status.PASS, "Applicant has no criminal records.")

    self.assertEqual((Status.FAIL, "Applicant has no previous employment. Applicant has no criminal records."), process_application(Application(), fail_has_no_employment, pass_has_no_criminal_record))

  def test_process_application_with_employment_and_criminal_records_fails(self):
    pass_has_employment = lambda _: (Status.PASS, "Applicant has had previous employment.")
    fail_has_criminal_record = lambda _: (Status.FAIL, "Applicant has criminal records.")

    self.assertEqual((Status.FAIL, "Applicant has had previous employment. Applicant has criminal records."), process_application(Application(), pass_has_employment, fail_has_criminal_record))

if __name__ == '__main__': 
  unittest.main()
