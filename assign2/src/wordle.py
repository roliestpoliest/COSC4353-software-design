from enum import Enum

class TallyMatch(Enum):
  EXACT_MATCH = 0
  DIFFERENT_POSITION = 1
  NOT_IN_WORD = 2

class GameStatus(Enum):
  WON = 0
  LOST = 1
  IN_PROGRESS = 2

class GamePlay(Enum):
  ATTEMPTS = 0
  TALLY_RESPONSE = 1
  GAME_STATUS = 2
  MESSAGE = 3

def tally(target, guess):
  check_guess_length(target, guess)
  return [tally_for_position(position, target, guess) for position in range(len(target))]

def tally_for_position(position, target, guess):
  if target[position] == guess[position]:
    return TallyMatch.EXACT_MATCH
  
  letter_at_position = guess[position]

  positional_matches = count_positional_matches(target, guess, letter_at_position)
  non_positional_occurrences_in_target = count_number_of_occurrences_until_position(len(target) - 1, target, letter_at_position) - positional_matches

  number_of_occurrences_in_guess_until_position = count_number_of_occurrences_until_position(position, guess, letter_at_position)

  if non_positional_occurrences_in_target >= number_of_occurrences_in_guess_until_position:
    return TallyMatch.DIFFERENT_POSITION
  
  return TallyMatch.NOT_IN_WORD

def count_positional_matches(target, guess, letter):
  return sum(1 for target_ch, guess_ch in zip(target, guess) if target_ch == guess_ch == letter)

def count_number_of_occurrences_until_position(position, word, letter):
  matches = word[:position + 1].count(letter)
  return matches if matches is not None else 0

def play(attempt_number, target, guess, is_spelling_correct=lambda word: True):
  check_attempt_number(attempt_number)

  if not is_spelling_correct(guess):
    raise ValueError("Not a word")

  tally_response = tally(target, guess)
  game_status = get_game_status(tally_response, attempt_number)
  message = get_game_message(game_status, attempt_number, target)

  return {
    GamePlay.ATTEMPTS: attempt_number + 1,
    GamePlay.TALLY_RESPONSE: tally_response,
    GamePlay.GAME_STATUS: game_status,
    GamePlay.MESSAGE: message
  }

def get_game_status(tally_response, attempt_number):
  if all(match == TallyMatch.EXACT_MATCH for match in tally_response):
    return GameStatus.WON 
  
  return GameStatus.LOST if attempt_number >= 5 else GameStatus.IN_PROGRESS

def get_game_message(game_status, attempt_number, target):
  if game_status == GameStatus.WON:
    feedback = {
      0: "Amazing",
      1: "Splendid",
      2: "Awesome"
    }
    return feedback.get(attempt_number, "Yay")
  
  return f"It was {target}, better luck next time" if game_status == GameStatus.LOST else ""

def check_attempt_number(attempt_number):
  if attempt_number >= 6:
    raise ValueError("Game is over. All six attempts have been used.")

def check_guess_length(target, guess):
  if len(guess) != len(target):
    raise ValueError(f"Invalid guess length. Guess must be {len(target)} letters.")
