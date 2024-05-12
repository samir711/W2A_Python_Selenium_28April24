"""
TUPLES
"""
"""
TUPLE PROPERTIES -
  --> Tuples are READ ONLY version of LIST
  --> Tuples are IMMUTABLE  in nature
      1. Create
      2. Read / Access a tuple 
      3. Update a tuple   (Partially allowed)
      4. Delete a tuple   (Partially allowed)
  --> Order is also maintained
  --> Tuples are represented using ()
  --> Heterogeneous elements are allowed
  --> Indexing and Slicing are also allowed in a tuple
  
"""
"""
CREATING A TUBLR
"""
# How to create an empty tuple?
empty=()
print(type(empty))

# How to create a regular tuple?
example = ("student", 12, "Sec-A", 23.5, True, 2+6j)
print(example)

# Can we add a list inside a tuple or a different data structure?
example= ("Student", 12, "Sec-A", 23.5, True, 2+6j, [1 ,2, 3, 4, "Ashish"], ('A', "B", 1, 2, 3, 4), {"name":"Ashish"})
print(example)

# What is tuple packing?
pack = 10, 12, "Ashish", 23.44, True
print((pack))
print(type(pack))

# What is tuple unpacking?
example= ("Student", 12, "Sec-A", 23.5, True, 2+6j, [1 ,2, 3, 4, "Ashish"], ('A', "B", 1, 2, 3, 4), {"name":"Ashish"})

a, b, c, d, e, f, g, h, i = example
print(a)
print(b)
print(c)
print(e)
print(f)

"""
READING / ACCESSING  A TUPLE
"""
example= ("Student", 12, "Sec-A", 23.5, True, 2+6j, [1 ,2, 3, 4, "Ashish"], ('A', "B", 1, 2, 3, 4), {"name":"Ashish"})

print(example)
# How to access single element of a tuple?
print(example[0])
print(example[-1])
print(example[4])

# How to access multiple elements of tuple?
print(example[0:5])
print(example[8:1:-2])

"""
UPDATING A TUBLE
"""
# How to update a complete tuple?

example= ("Student", 12, "Sec-A", 23.5, True, 2+6j, [1 ,2, 3, 4, "Ashish"], ('A', "B", 1, 2, 3, 4), {"name":"Ashish"})

print(example)
example = (1, 2, 3, "Ashish")
print(example)

# How to update a single element of tuple?
example= ("Student", 12, "Sec-A", 23.5, True, 2+6j, [1 ,2, 3, 4, "Ashish"], ('A', "B", 1, 2, 3, 4), {"name":"Ashish"})

print(example)

# example[0] = "Manthan"
# TypeError: 'tuple' object does not support item assignment
print(example)

# How to update multiple elements of tuple?
# example[1:3] =

# How to delete a complete tuple?
example= ("Student", 12, "Sec-A", 23.5, True, 2+6j, [1 ,2, 3, 4, "Ashish"], ('A', "B", 1, 2, 3, 4), {"name":"Ashish"})
del example
# print(example) NameError: name 'example' is not defined










