"""
DICTIONARY
"""
"""
PYTHON DICTIONARY
  --> A dictionary is a combination of key and value. It is a key value pair
  --> nameOfTheWord     --> Key
  --> meaningOfTheWord  --> value
  --> The order of the pair is NOT MAINTAINED
  --> Indexing and Slicing is NOT ALLOWED
  --> Dictionary are implemented using {}
  --> Dictionary are MUTABLE in nature
      1. Create
      2. Read / Access
      3. Update
      4. Delete
  --> Heterogenous values are allowed
  --> Duplicate values are allowed, but duplicate KEYS are NOT ALLOWED
"""

"""
CERATING A DICTIONARY
"""
# How to cerate an empty dictionary?
empty = {}
print(type(empty))

# How to create a regular diectionary ?
example = {
    "name": "Ashish",
    "address": "Delhi, Saket",
    "marks": [12, 23, 12, 24]
}
print(example)
print(type(example))

# Can we only give the key as a string? or other data structure are also allowed in the key?
example = {
    "name": "Manthan",
    1: "Integer",
    1.44: "Floating",
    ("A", "V"): "Tuple",
    # [1, 2, 3]: "List",
    # {1, 3}: "Dictionary"
}
print(example)
print(type(example))
"""
READING / ACCESING A DICTIONARY
"""
example = {
    "name": "Ashish",
    "address": "Delhi. saket",
    "marks": [12, 23, 13, 24]
}
# How to access complete dictionary?
print(example)

# How to access an individual item of a dictionary?
# dictionaryName[keyName]
print(example["marks"])
print(example["name"])
# print(example["age"]) # KeyError: 'age'

# How to acces multiple values?
# using loops

# How to access all the keys of the dictionary?
print(example.keys())

# How to access all the values of the dictionary?
print(example.values())

# How to access all the key values pairs of a dictionary?
print(example.items())

"""
UPDATING A DICTIONARY
"""

# How to update a complete dictionary
example = {
    "name": "Ashish",
    "address": "Delhi, Saket",
    "marks": [12, 23, 12, 24]
}

print(example)
example = {
    1: 2,
    "name": "Pradeep"

}
print(example)
# How to update a single element in the dictionary?
# dictionaryName[key] = value
example = {
    "name": "Ashish",
    "address": "Delhi, Saket",
    "marks": [12, 23, 12, 24]
}
example["address"] = "Juhu Mumbai"
print(example)

# How to update multiple elements in the dictionary ?
# For Loop | While loops

# Can we add new key value pairs inside a dictionary?
example["rollNumber"] = 23
print(example)

"""
DELETING A DICTIONARY
"""
# How to delete a complete dictionary ?
test = {'name': 'Ashish', 'address': 'Juhu Mumbai', 'marks': [12, 23, 12, 24], 'rollNumber': 23}
print(f"Test  = {test}")
del test
# print(test) NameError: name 'test' is not defined

# How to delete a single item?
# del dictionaryName[keyName]
test = {'name': 'Ashish', 'address': 'Juhu Mumbai', 'marks': [12, 23, 12, 24], 'rollNumber': 23}
del test["address"]
print(f"Test  = {test}")

# What is the difference between pop() and popItem()
test = {'name': 'Ashish', 'address': 'Juhu Mumbai', 'marks': [12, 23, 12, 24], 'rollNumber': 23}
# del test["section"] KeyError: 'section'
# print(f"Using DEL function, test - {test}")

# test.pop("section") KeyError: 'section'
# print(f"Using Pop function, test - {test}")

test.pop("name") # Remove the entry or key mentioned in pop() function
print(f"Using Pop function, test - {test}")
test.popitem() # Remove the last entry
print(f"Using Pop function, test - {test}")