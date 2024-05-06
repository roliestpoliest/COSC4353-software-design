import unittest
from unittest.mock import patch
import sys
sys.path.append('src')
from agilec_spellcheck_service import get_response, parse, is_spelling_correct

class AgilecSpellCheckServiceTests(unittest.TestCase):
  def test_get_response_returns_true_for_favor(self):
    self.assertEqual(get_response("favor"), "true")

  def test_get_response_returns_false_for_favro(self): 
    self.assertEqual(get_response("favro"), "false")
  
  def test_parse_response_returns_true_for_true(self):
    self.assertTrue(parse("true"))
  
  def test_parse_response_returns_false_for_false(self):
    self.assertFalse(parse("false"))
  
  def test_parse_response_raises_value_error_for_invalid_response(self):
    self.assertRaisesRegex(ValueError, "Invalid response", parse, "")  

  @patch('agilec_spellcheck_service.get_response', return_value="true")
  @patch('agilec_spellcheck_service.parse', return_value=True)
  def test_is_spelling_correct_returns_true_if_get_response_true(self, mock_parse, mock_get_response):
    self.assertTrue(is_spelling_correct("FAVOR"))
    mock_get_response.assert_called_once_with("FAVOR")
    mock_parse.assert_called_once_with("true")

  @patch('agilec_spellcheck_service.get_response', return_value="false")
  @patch('agilec_spellcheck_service.parse', return_value=False)
  def test_is_spelling_correct_returns_false_if_get_response_false(self, mock_parse, mock_get_response):
    self.assertFalse(is_spelling_correct("FAVOR"))
    mock_get_response.assert_called_once_with("FAVOR")
    mock_parse.assert_called_once_with("false")

  @patch('agilec_spellcheck_service.get_response', side_effect=Exception("Network Error"))
  def test_is_spelling_correct_throws_network_error_if_get_response_throws_exception(self, mock_get_response):
    self.assertRaisesRegex(Exception, "Network Error", is_spelling_correct, "FAVOR")
    mock_get_response.assert_called_once_with("FAVOR")

if __name__ == '__main__': 
  unittest.main()
