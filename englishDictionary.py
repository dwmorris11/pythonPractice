import json

# bring the json data in as a python dictionary
data = json.load(open("data.json"))

def lookup(word):
  return data[word]

print(lookup('rain'))