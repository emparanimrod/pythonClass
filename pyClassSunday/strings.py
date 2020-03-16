# Create string
myString = 'this is my string'
otherString = "Another String"
multiLine = '''Multiline string

new line
'''
# retrieve first letter of string

firstLetter = myString[0]
# print(firstLetter)

# retrieve index that does not exist
# print(len(myString))
# notInString  = myString[40-30]
# print(notInString)

# attempt to mutate string
# myString[2] = 'a'
# print()

# concatenate string

newString = myString + ': new characters' 

# concatenate multiple copies of string
newString = myString*(3+2)
# print(newString)


# fetch range of characters
newString = myString[1:12]
# print(newString)

# check if value in string
isValuePresent = 'This' in myString
# print(isValuePresent)

# check if value is not in string
isValuePresent = 'Marcus' not in myString
# print(isValuePresent)

# string formatting
formattedString = 'My string is: %s' %myString
# print(formattedString)

# multiple var string placeholders
number = 1
multipleVarsString = 'Multi-var string: %s Number: %i' %(myString, number)
# print(multipleVarsString)

# alternative method
message = 'My string: {} , Number {}'.format(myString, number)
# print(message)

# capitalize string
capitalized = myString.capitalize()
# print(capitalized)

# convert to upper case
uppercase = myString.upper()
# print('Uppercase: %s' %uppercase)

# find in string
value = myString.find('s')
# print(value)

# count number of desired items in string
totalS = myString.count('t')
print(totalS)