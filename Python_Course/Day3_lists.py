"""
LISTS
"""

"""
PYTHON LISTS
           ---> Collection of heterogenous items
           ---> String, int, float, list tuple, dict etc
           ---> The order in which we add the data, that order is maintained.
           ---> Duplicate values are allowed inisde a list
           ---> Lists are implemented using []
           ---> Lists are MUTABLE in NATURE, allow CURD Operation
              1. Create a List
              2. Read / Access a list
              3. Update a list
              4. Delete a list
           ---> List operation
"""

"""
CREATING A LIST
"""
# How to define a empty list?
empty = []
print(type(empty))

# How to create a regual list?
example = ["Apples", "Mangoes", 2, 9.32, 2+4j, True,[1,2,3,4,5]]
print(example)
print(type(example))

# Can we have different data structure inside a list?
ds_list = [(1,2,3),[3, 4, 5, 6], {"name": "samir"}]
print(ds_list)
print(type(ds_list))

# Can we convert a string into a list?
institute = "Way2Automation"
print(type(institute))
converted_institute = list(institute)
print(converted_institute)
print(type(converted_institute))

print(str(converted_institute))
# Create a list using duplicate values ?
duplicate = [1,2,1,2,1,2,1,2,1]
print(duplicate)

"""
READING / ACCESSING A LIST
  --> Lists are accessed using index values only
  --> Index value starts form 0
"""
example = ["Apples", "Mangoes", 2, 9.32, 2+4j, True,[1,2,3,4,5]]

# How can we say that the order is always maintained?
print(example)
print(example[0])

# can we access a negative index?
print(example[-1])

# Is slicing in a list allowed?
print(example[1:3])
print(example[6:2:-2])

# Accessing a multi-dimensional list
multi_d = [
    [1,2,3, ["A", "B", ["C", "D",["E", "F",[True,[False]]]]]],
    ["Abhishek","AJ",["koser","Bala-raj"]],
    [2.3, 554.3, 2+7j]
]
print(multi_d[0])
print(multi_d[1][2])
print(multi_d[1][2][1])
print(multi_d[0][3][2][1])

"""
UPDATING A LIST
"""
student_data = ["Ashish", 23, "Delhi", 7011197716]

# Can we update a sing element inside a list?
print(student_data)
print(student_data[1])
student_data[1] = 2
print(student_data)

# Can we update the complete list?
student_data = [1, 2, 3, 4, 5]
print(student_data)

# Can we update multiple elements inside a list?
student_data[2:4] = ["Ashish", "Abhishek"]
print(student_data)

# How to add some data in the end of the list?
student_data.append("Kosar")
print(student_data)

# How to insert some data at a specific index position?
student_data.insert(3, "Manthan")
print(student_data)

"""
DELETING A LIST
"""

# Can we delete a single element from a list?
student_data = [1 ,2, 'Ashish', 'Manthan', 'Abhishek', 5, 'Kosar']
print(student_data[1])
del student_data[2]
print(student_data)
print(student_data[1:3])
del student_data[1:3]
print(student_data)


# Can we delete the complete list?
student_data = [1 ,2, 'Ashish', 'Manthan', 'Abhishek', 5, 'Kosar']
#del student_data
print(student_data)

# Can we delete a specific value from the list?
student_data = [1 ,2, 'Ashish', 'Manthan', 'Abhishek', 5, 'Kosar']
print(student_data)
student_data.remove("Manthan")
print(student_data)

#Difference between del and pop ?
student_data = [1 ,2]
print(student_data)
# del  stue