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


