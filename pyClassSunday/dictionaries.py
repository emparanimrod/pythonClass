# create dictionary
sportsList = ['Soccer', 'Basketball']

myDict = {
    'name':'Norman',
    'home':'Nairobi',
    'sports': sportsList
}

# print(myDict)

# retrieve value from dictionary
val = myDict.get('name')
# print(val)

# update a dictionary
myDict['favorite food'] = ['Ugali', 'chicken']
# print(myDict)

# delete a value in a dictionary
del myDict['home']

# view keys from dictionary
myKeys = myDict.keys()
# print(type(myKeys))

# get values from dict
myValues = myDict.values()
# print(myValues)

# pop item from dictionary
myDict.pop('sports')
print(myDict)

# for loop in dictionary
for key in myDict:
    print('My key is %s and value is %s' %(str(key), str(myDict.get(key))))

# clear a dictionary
myDict.clear()
print(myDict)
