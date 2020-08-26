import datetime
print("The date and time is")
print(datetime.datetime.now())
print("The date and time is", datetime.datetime.now())

mynow = datetime.datetime.now()
print(mynow)

x = 10
y = "10"

sum1 = x + x
sum2 = y + y
z = 10.1

print(sum1, sum2)
print(type(x), type(y), type(z))

student_grades = [9.1, 8.8, 7.5]

print(list(range(1, 10)))
# [1, 2, 3, 4, 5, 6, 7, 8, 9] one less than 10
print(list(range(1, 10, 2)))
# [1, 3, 5, 7, 9] step by 2

# dir shows list of attributes
dir(list)
dir(int)
dir(float)
dir(str)

# help gives instructions on how to use the attribute
help(str.upper)

"hello".upper()
"hello".title()

# built in python functions and types
dir(__builtins__)

mysum = sum(student_grades)
length = len(student_grades)
mean = mysum / length
print(mean)

# dictionaries
student_grades = {
  "Mary": 9.1,
  "Sim": 8.8,
  "John": 7.5
  }

dir(dict)
student_grades.values()
student_grades.keys()

#tuples (immutable)
color_codes = ('5', 123)

monday_temperatures = [9.1, 8.8, 7.5]
monday_temperatures.append(8.1)
monday_temperatures.index(8.8)

seconds = [1.2323442655, 1.4534345567, 1.023458894, 1.10001399445]
seconds.pop(1)

# python slice, last one is not included
monday_temperatures[0:2]
# shorthand
monday_temperatures[:2]
# to the last item of list
monday_temperatures[2:]
# use negative numbers to count from right
monday_temperatures[-2]
# negative slicing
monday_temperatures[-2:]
monday_temperatures[-4:-2]

mystring = 'hello'
mystring[1]
mystring[-1]
mystring[:3]
monday_temperatures = ['hello', 1, 2, 3]
# return 'e'
monday_temperatures[0][1]

# function definition
def mean(mylist):
  the_mean = sum(mylist) / len(mylist)
  return the_mean

print(mean([1, 4, 5]))

# conditionals (can use and and or as well)
def newMean(value):
  if type(value) == dict:
    the_mean = sum(value.values()) / len(value)
  else:
    the_mean = sum(value) / len(value)

  return the_mean

  # isinstance(value, type) is recommended for checking type

  # returns only numbers of an input with strings and numbers
def only_numbers(lst):
  return [val for val in lst if not isinstance(val, str)]

def only_positive(lst):
  return [i for i in lst if i > 0]

# move the for loop to the end when using list comprehension and else statements
def zero_not_strings(lst):
    return [i if not isinstance(i, str) else 0 for i in lst]

def string_to_float_sum(lst):
    return sum([float(i) for i in lst])

def to_upper(*args):
    return sorted(list([i.upper() for i in args]))

# reading a file in python
myfile = open("test.txt")
print(myfile.read())
myfile.close()

# open file with 'with' context manager
# with context manager automatically uses the close method
with open("text.txt") as myfile:
    content = myfile.read()
print(myfile)

# writing a file
with open("newTest.txt", "w") as myfile:
  myfile.write("tomato\ngarlic")

# printing the first 90 chars
with open("bear.txt") as file:
    content = file.read()
print(content[:90])

def count_chars(char, fp):
    summation = 0
    with open(fp) as file:
        content = file.read()
    for i in content:
        if i == char:
            summation = summation + 1
    return summation

def foo(character, filepath="bear.txt"):
    file = open(filepath)
    content = file.read()
    return content.count(character)

with open("bear.txt") as rd_file:
    content = rd_file.read()
content = content[:90]

with open("first.txt", "w") as wr_file:
    wr_file.write(content)