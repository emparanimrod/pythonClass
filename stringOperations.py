myStr = "hello"

# get item from string
firstLetter = myStr[2]

print("letter is " + firstLetter)

# add letter to string

myStr = "goodbye"

print("reassigned string: " + myStr)

# convert number to string
myNumber = 20
numString = str(myNumber)
print(type(numString))

# convert list to string
myList = ['John', 'Mary', 'Peter']

listStr = str(myList)
print(type(listStr))

# string formatting
name = 'Chuck Norris'
message = 'My name is %s' % name

print(message)

# string formatting with multiple variables
age = 70
message = 'My name is %s and my age is %i' % (name , age)
print(message)


#  alternative format strings

message = "New Mesage: My name is {} and my age is {} years old ".format(name, age)
print(message)