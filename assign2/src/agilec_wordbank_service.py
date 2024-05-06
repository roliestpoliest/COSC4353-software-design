import requests, random, time

def get_response():
  URL = "https://agilec.cs.uh.edu/words"

  return requests.get(URL).text.split()

def get_random_word(words, seed=time.time_ns()):
  random.seed(seed)
  
  return random.choice(words)
