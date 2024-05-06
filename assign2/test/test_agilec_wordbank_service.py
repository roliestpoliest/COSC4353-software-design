import unittest
import random
import sys
sys.path.append('src')
from unittest.mock import patch
from agilec_wordbank_service import get_response, get_random_word

class AgilecWordbankServiceTests(unittest.TestCase):
  def test_get_words_returns_a_list_of_words(self):
    self.assertTrue(len(get_response()) > 0)
  
  def test_get_random_word_given_a_list_of_words(self):
    words = ["favor", "smart", "guide", "tests"]
    
    self.assertIn(get_random_word(words), words)

  def test_get_random_word_returns_two_different_words_given_the_same_list(self):
    words = ["favor", "smart", "guide", "tests"]

    self.assertNotEqual(get_random_word(words, 1000), get_random_word(words, 1001))

if __name__ == '__main__':
  unittest.main()
