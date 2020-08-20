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

