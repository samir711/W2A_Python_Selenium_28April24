"""
DAY: STRINGS AND LISTS
"""
"""
--> A sequence of characters
"""
school = "Delhi Public School"
print(type(school))

# How to access individual elements of a string ?
print(len(school))
print(school[1])
print(school[4])
print(school[8])
print(school[-2])
"""
SELICING OPERATION
--> Getting a substring out of the main string

   variableName[begin:end:step]
   begin ::= The index value to start slicing.
   end   ::= The index until where slicing to be done.
   step  ::= It determine the increment / decrement for each index of slice
"""
example = "abcdefgij"
print(example[1:7])
print(example[1:8:1])
print(example[1:8:2])
print(example[:7])
print(example[::])
print(example[::-1])
print(example[7:1:-1])
print(example[1:8:-1])

"""
String formatters

    1. using format()
    2. % Operator
         String ---> %s
         int    ---> %d
         float  ---> %f
    3. f-stings


"""
# name = input("Enter your name : ")
# designation = input("Enter your designation : ")
name = "Samir"
designation = "Student"
print("Hey {0}, Welcome to Way2Automation !. Your are enrolled as a {1}".format(name, designation))
print("Hey %s, Welcome to Way2Automation !. Your are enrolled as %s" %(name, designation))
print(f"Hey {name}, welcom to Way2Automation!. Your are enrolled as {designation}")


"""
STRINGS FUNCTION AND OPERATIONS
"""
string_1 = "Welcome"
string_2 = "to Way2Automation!"

# How to get the len ?
print(len(string_2))

#Convert stirng to different types of cases?
print(string_2.upper())
print(string_2.lower())
print(string_2.title())

print('10' + '10')
print(string_1 + " " + string_2)
print('ba' + 'na' * 2)

# How to verify if a substring is a part of a string?
# in is the membership operation
print('come' in string_1)
print('Wel' not in string_1)




