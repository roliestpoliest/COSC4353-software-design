import requests

def get_response(word):
  URL = "http://agilec.cs.uh.edu/spellcheck?check="

  return requests.get(f"{URL}{word}").text

def parse(response):
  if response not in ["true", "false"]:
    raise ValueError("Invalid response")
  
  return response == "true"

def is_spelling_correct(word):
  return parse(get_response(word))
