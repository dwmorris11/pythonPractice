import json
from difflib import get_close_matches

# bring the json data in as a python dictionary
data = json.load(open("data.json"))

def optimize(lst):
  count = 0
  output = ''
  for definition in lst:
    count = count + 1
    output = output + f"{count}. {definition}\n"
  return output

def lookup(word):
  word = word.lower()
  if word in data:
      return optimize(data[word])
  else:
      close_match = get_close_matches(word,data.keys())[0]
      if len(close_match) > 0:
          print(f"{close_match}:\n{optimize(data[close_match])}\n")
          user_verify = input(f"Did you mean {close_match}?(Y/n)")
          if user_verify.lower() == 'n':
            return "Word is not found."
          elif user_verify.lower() == 'y':
            return ''
          else:
            return "We didn't understand."
      else:
          return "Word is not found."

word = input("Enter word: ")
print(lookup(word))