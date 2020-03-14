myDict = {
    'country': 'Kenya',
    'county': 'Nairobi',
    'estates': ['Langata', 'Westlands', 'Buru']
}

# print(myDict)

# get value from dictionary

estates = myDict.get('estates')
# print(f"Estates: {estates[2]}")

# append a value
myDict['house'] = 'House 214'

# print(myDict)

# remove item
del myDict['house']
# print(myDict)

# for loop in dictionary
for key in myDict:
    print("Key: " + key + ", Value: " + str(myDict[key]))