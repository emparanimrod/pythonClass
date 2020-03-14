# defining a list

myList = ['John', 'Mary', 23, True]
newList = ['Tom', 'Njugush']
myTuple = ('John', 'Mary', 23, True)

# add item to list

myList.append('Norman')
print(f"List:{myList}")
# get item from list

secondName = myList[1]
print(myList[1])

# concatenate lists
concList = myList + newList
print(concList)

# find if John is in list 

isJohnPresent = 'John' in concList
print(f"Is John Present: {isJohnPresent}")
print(f"{'John' not in concList}")
# find if Abbas is not in list 

isAbbasPresent = 'Abbass' not in concList
print(f"Is Abbass Present: {isAbbasPresent}")

#remove item from list
concList.remove(23)
print(concList)

# reverse list
concList.reverse()
print(concList)

#sort list
concList.sort()
print(concList)

