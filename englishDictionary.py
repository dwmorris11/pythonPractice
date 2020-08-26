import json
from difflib import get_close_matches

# bring the json data in as a python dictionary
data = json.load(open("data.json"))

def lookup(word):
  word = word.lower()
  if word in data:
      return data[word]
  else:
      close_match = get_close_matches(word,data.keys())[0]
      return f"Word not found. Did you mean {close_match}?"

word = input("Enter word: ")
print(lookup(word))