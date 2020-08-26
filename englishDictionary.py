import json

# bring the json data in as a python dictionary
data = json.load(open("data.json"))

def lookup(word):
  word = word.lower()
  if word in data:
      return data[word]
  else:
      return "Word not found."

word = input("Enter word: ")
print(lookup(word))