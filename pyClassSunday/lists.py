# declare a list
myList = ['John','Mary', 'Peter', 1, True]
# print(myList)

# create a tuple
myTuple = ('Tom', 'Jerry', 'Peter', 23.1, False)
# print('My Tuple: %s' % str(myTuple))

# add items to a list
val = 'Home'
myList.append(val)
# print(myList)

# insert at particular index
myList.insert(2 , val)
# print(myList)


# retrieve an item from a list
val = myList[1]
# print(val)

# find length of list
length = len(myList)
# print(length)

# remove an item from list 
myList.remove('Home')
# print(myList)

# pop item from list
myList.pop()
# print(myList)

# convert list to tuple
newTuple = tuple(myList)
# print(newTuple)

# convert tuple to list 
newList = list(myTuple)
# print(newList)

# for loop in lists and tuples
for item in myList:
    print(item)