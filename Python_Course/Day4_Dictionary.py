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
    1 : "Integer",
    1.44 : "Floating",
    ("A","V"): "Tuple",
    # [1, 2, 3]: "List",
    # {1, 3}: "Dictionary"
}
print(example)
print(type(example))
"""
READING / ACCESING A DICTIONARY
"""
example = {
     "name" : "Ashish",
     "address" : "Delhi. saket",
     "marks" :[12, 23, 13, 24]
}
# How to access complete dictionary?
print(example)

# How to access an individual item of a dictionary?
#dictionaryName[keyName]
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
