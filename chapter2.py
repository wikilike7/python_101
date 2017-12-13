# my_string = "I'm a Python programmer!"
otherString = 'The word "python" usually refers to a snake'
tripleString = """Here's another way to embed "quotes" in a string"""


my_string = 'hello, world'

# string concatenation
string_one = 'My dog ate '
string_two = 'my homework'
string_three = string_one + string_two
print(string_three)


# string method
print(my_string.upper())
# print('hello, world'.upper())
print(dir(my_string))  # list all of methods from string

# string slicing
print(my_string[0:2])


# string formatting
your_string = 'I like %s' % 'Python'
print(your_string)
var = 'cookies'
another_string = '%s and %s' % (your_string, var)
print(another_string)


# calc
this_string = '%i + %i = %i' % (1, 2, 3)
print(this_string)

float_string = '%.2f' % 1.23456
print(float_string)


# string templates
print('%(lang)s is fun' % {'lang': 'Python'})

print('%(value)s %(value)s %(value)s' % {'value': 'spam'})




