"""
DATA STRUCTURE - SET
"""
"""
SET
   --> Set can contains different types of elements
   --> ORDER is NOT MAINTAINED
   --> Set are NOT represented using key value pairs
   --> CRUD operations are allowed
        1. Create a set
        2. Read / Access a set
        3. Update a set
        4. Delete a set
   --> DUBLICATES values are NOT ALLOWED
   --> Indexing and Slicing is also NOT SUPPORTED
   --> SET are represented using {}
"""

"""
CREATING A SET
"""
# How to create an empty set?
example = {}
print(type(example))

# How to create a regular set ?
example = {"Ashish", 1, 2, True, 3 + 4j, 1, 2, "Ashish"}
print(example)
print(len(example))

# Can we add mutable data in a set?
# example = {1, 2, 3, ["Ashish", "Kosar"], {"name":"Abhishek"}}
# print(example) TypeError: unhashable type: 'list'

# example = {1, 2, 3, {1, 2, 3}}
# print(example) TypeError: unhashable type: 'list'

example = {1, 2, 3, (1, 2, 3)}
print(example)

"""
READING / ACCESSING A SET
"""
example = {"Ashish", 1, 2, True, 3 + 4j, 1, 2, "Ashish"}
print(f"Complete set,example = {example}")

# How to read a single element of a set ?
example = {"Ashish", 1, 2, True, 3 + 4j, 1, 2, "Ashish"}
# print(f"Single element of a set,example = {example[1]}") TypeError: 'set' object is not subscriptable

# How to read multiple element of a set?
# Using loops only

"""
UPDATING A SET
"""
example = {"Ashish", 1, 2, True, 3 + 4j, 1, 2, "Ashish"}
print(f"Complete set  example = {example}")

# example[0] = "Abhishek"
# print(f"Complete set  example = {example}") TypeError: 'set' object does not support item assignment
example.add("Abhishek")
print(f"Complete set  afte updateing , example = {example}")

# How to update multiple values inside a set?
example.update([1, 2, "Salary", "Kosar"])
print(f"Complete set  afte updateing , example = {example}")

"""
DELETING A SET 
"""

example = {"Ashish", 1, 2, True, 3 + 4j, 1, 2, "Ashish"}
print(f"Complete set  example = {example}")
del example
# print(example) NameError: name 'example' is not defined
#  How to delete single element inside a set?
example = {"Ashish", 1, 2, True, 3 + 4j, 1, 2, "Ashish"}
print(example)
example.pop()
print(example)

example.remove(2)
print(example)

# example.remove(21) KeyError: 21 - Gives key error if key is not present
# print(example)

example.discard("Ashish")
print(example)

example.discard(21) # No key error even if the key is not present
print(example)