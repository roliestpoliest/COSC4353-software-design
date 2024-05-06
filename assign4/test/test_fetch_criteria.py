import unittest
import sys
sys.path.append('src')
from fetch_criteria import fetch_criteria

class FetchCriteriaTests(unittest.TestCase):
  def test_fetch_criteria_gets_employment_criteria(self):
    self.assertIn(('employment'), fetch_criteria())

  def test_fetch_criteria_gets_criminal_record_criteria(self):    
    self.assertIn(('criminal_record'), fetch_criteria())

if __name__ == '__main__':
  unittest.main()
