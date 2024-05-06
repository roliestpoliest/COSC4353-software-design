import unittest
import sys
sys.path.append('src')
from parameterized import parameterized
from wordle import tally, TallyMatch, play, GameStatus, GamePlay
globals().update(TallyMatch.__members__)
globals().update(GameStatus.__members__)
globals().update(GamePlay.__members__)

class WordleTests(unittest.TestCase):
  def test_canary(self):
    self.assertTrue(True)

  @parameterized.expand([
    ("FAVOR", "FAVOR", [EXACT_MATCH, EXACT_MATCH, EXACT_MATCH, EXACT_MATCH, EXACT_MATCH]),
    ("FAVOR", "TESTS", [NOT_IN_WORD, NOT_IN_WORD, NOT_IN_WORD, NOT_IN_WORD, NOT_IN_WORD]),
    ("FAVOR", "RAPID", [DIFFERENT_POSITION, EXACT_MATCH, NOT_IN_WORD, NOT_IN_WORD, NOT_IN_WORD]),
    ("FAVOR", "MAYOR", [NOT_IN_WORD, EXACT_MATCH, NOT_IN_WORD, EXACT_MATCH, EXACT_MATCH]),
    ("FAVOR", "RIVER", [NOT_IN_WORD, NOT_IN_WORD, EXACT_MATCH, NOT_IN_WORD, EXACT_MATCH]),
    ("FAVOR", "AMAST", [DIFFERENT_POSITION, NOT_IN_WORD, NOT_IN_WORD, NOT_IN_WORD, NOT_IN_WORD]),
    ("SKILL", "SKILL", [EXACT_MATCH, EXACT_MATCH, EXACT_MATCH, EXACT_MATCH, EXACT_MATCH]),
    ("SKILL", "SWIRL", [EXACT_MATCH, NOT_IN_WORD, EXACT_MATCH, NOT_IN_WORD, EXACT_MATCH]),
    ("SKILL", "CIVIL", [NOT_IN_WORD, DIFFERENT_POSITION, NOT_IN_WORD, NOT_IN_WORD, EXACT_MATCH]),
    ("SKILL", "SHIMS", [EXACT_MATCH, NOT_IN_WORD, EXACT_MATCH, NOT_IN_WORD, NOT_IN_WORD]),
    ("SKILL", "SILLY", [EXACT_MATCH, DIFFERENT_POSITION, DIFFERENT_POSITION, EXACT_MATCH, NOT_IN_WORD]),
    ("SKILL", "SLICE", [EXACT_MATCH, DIFFERENT_POSITION, EXACT_MATCH, NOT_IN_WORD, NOT_IN_WORD])
  ])
  def test_expected_tally(self, target, guess, expected_tally):
    self.assertEqual(tally(target, guess), expected_tally)

  @parameterized.expand([
    ("FAVOR", "FERVER", ValueError, "Invalid guess length. Guess must be 5 letters."),
    ("FAVOR", "FOR", ValueError, "Invalid guess length. Guess must be 5 letters.")
  ])
  def test_tally_invalid_guess_length(self, target, guess, expected_exception, expected_message):
    with self.assertRaisesRegex(expected_exception, expected_message):
      tally(target, guess)

  @parameterized.expand([
    (0, "FAVOR", "FAVOR", {
      ATTEMPTS: 1,
      TALLY_RESPONSE: [EXACT_MATCH, EXACT_MATCH, EXACT_MATCH, EXACT_MATCH, EXACT_MATCH],
      GAME_STATUS: WON,
      MESSAGE: "Amazing"
    }),
    (0, "FAVOR", "TESTS", {
      ATTEMPTS: 1,
      TALLY_RESPONSE: [NOT_IN_WORD, NOT_IN_WORD, NOT_IN_WORD, NOT_IN_WORD, NOT_IN_WORD],
      GAME_STATUS: IN_PROGRESS,
      MESSAGE: ""
    }),
    (1, "FAVOR", "FAVOR", {
      ATTEMPTS: 2,
      TALLY_RESPONSE: [EXACT_MATCH, EXACT_MATCH, EXACT_MATCH, EXACT_MATCH, EXACT_MATCH],
      GAME_STATUS: WON,
      MESSAGE: "Splendid"
    }),
    (1, "FAVOR", "TESTS", {
      ATTEMPTS: 2,
      TALLY_RESPONSE: [NOT_IN_WORD, NOT_IN_WORD, NOT_IN_WORD, NOT_IN_WORD, NOT_IN_WORD],
      GAME_STATUS: IN_PROGRESS,
      MESSAGE: ""
    }),
    (2, "FAVOR", "FAVOR", {
      ATTEMPTS: 3,
      TALLY_RESPONSE: [EXACT_MATCH, EXACT_MATCH, EXACT_MATCH, EXACT_MATCH, EXACT_MATCH],
      GAME_STATUS: WON,
      MESSAGE: "Awesome"
    }),
    (2, "FAVOR", "TESTS", {
      ATTEMPTS: 3,
      TALLY_RESPONSE: [NOT_IN_WORD, NOT_IN_WORD, NOT_IN_WORD, NOT_IN_WORD, NOT_IN_WORD],
      GAME_STATUS: IN_PROGRESS,
      MESSAGE: ""
    }),
    (3, "FAVOR", "FAVOR", {
      ATTEMPTS: 4,
      TALLY_RESPONSE: [EXACT_MATCH, EXACT_MATCH, EXACT_MATCH, EXACT_MATCH, EXACT_MATCH],
      GAME_STATUS: WON,
      MESSAGE: "Yay"
    }),
    (3, "FAVOR", "TESTS", {
      ATTEMPTS: 4,
      TALLY_RESPONSE: [NOT_IN_WORD, NOT_IN_WORD, NOT_IN_WORD, NOT_IN_WORD, NOT_IN_WORD],
      GAME_STATUS: IN_PROGRESS,
      MESSAGE: ""
    }),
    (4, "FAVOR", "FAVOR", {
      ATTEMPTS: 5,
      TALLY_RESPONSE: [EXACT_MATCH, EXACT_MATCH, EXACT_MATCH, EXACT_MATCH, EXACT_MATCH],
      GAME_STATUS: WON,
      MESSAGE: "Yay"
    }),
    (4, "FAVOR", "TESTS", {
      ATTEMPTS: 5,
      TALLY_RESPONSE: [NOT_IN_WORD, NOT_IN_WORD, NOT_IN_WORD, NOT_IN_WORD, NOT_IN_WORD],
      GAME_STATUS: IN_PROGRESS,
      MESSAGE: ""
    }),
    (5, "FAVOR", "FAVOR", {
      ATTEMPTS: 6,
      TALLY_RESPONSE: [EXACT_MATCH, EXACT_MATCH, EXACT_MATCH, EXACT_MATCH, EXACT_MATCH],
      GAME_STATUS: WON,
      MESSAGE: "Yay"
    }),
    (5, "FAVOR", "TESTS", {
      ATTEMPTS: 6,
      TALLY_RESPONSE: [NOT_IN_WORD, NOT_IN_WORD, NOT_IN_WORD, NOT_IN_WORD, NOT_IN_WORD],
      GAME_STATUS: LOST,
      MESSAGE: "It was FAVOR, better luck next time"
    })
  ])
  def test_play(self, attempt_number, target, guess, expected_result):
    self.assertEqual(play(attempt_number, target, guess), expected_result)

  @parameterized.expand([
    (0, "FAVOR", "FERVER", ValueError, "Invalid guess length. Guess must be 5 letters."),
    (0, "FAVOR", "FOR", ValueError, "Invalid guess length. Guess must be 5 letters.")
  ])
  def test_play_invalid_guess_length(self, attempt_number, target, guess, expected_exception, expected_message):
    with self.assertRaisesRegex(expected_exception, expected_message):
      play(attempt_number, target, guess)

  @parameterized.expand([
    (6, "FAVOR", "FAVOR", ValueError, "Game is over. All six attempts have been used."),
    (7, "FAVOR", "TESTS", ValueError, "Game is over. All six attempts have been used.")
  ])
  def test_play_invalid_attempt_number(self, attempt_number, target, guess, expected_exception, expected_message):
    with self.assertRaisesRegex(expected_exception, expected_message):
      play(attempt_number, target, guess)

  def test_play_throws_exception_for_attempt_1_fever_incorrect_spelling(self):
    self.assertRaisesRegex(ValueError, "Not a word", play, 0, "FAVOR", "FEVER", lambda guess: False)
        
  def test_play_returns_proper_response_for_attempt_1_fever_correct_spelling(self):
    result = play(0, "FAVOR", "FEVER", lambda guess: True)
    self.assertEqual(result, {
      ATTEMPTS: 1,
      TALLY_RESPONSE: [EXACT_MATCH, NOT_IN_WORD, EXACT_MATCH, NOT_IN_WORD, EXACT_MATCH],
      GAME_STATUS: IN_PROGRESS,
      MESSAGE: ""
    })

  def test_play_throws_exception_for_spell_check_with_attempt_1(self):
    self.assertRaisesRegex(Exception, "Network Error", play, 0, "FAVOR", "FEVER", lambda guess: exec("raise Exception('Network Error')"))

if __name__ == '__main__': 
  unittest.main()
