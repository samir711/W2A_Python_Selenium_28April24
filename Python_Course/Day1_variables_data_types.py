"""
VARIABLES
"""

# What are variables?
# --> It is just a container tosave the value inside it

# How to get the memory address of any variable?
roll_number = 12330123
print(id(roll_number))

# How does the program identifies what type of data is inside the variable?
print(type(roll_number))

# Are there any rules to declare variables?
"""
LEXICAL VARIBLES RULES

 variable ::= (letter | "_")(letter | digit | "_")
 letter ::= lowercase | uppercase
 lowercase ::= "a"..."z"
 uppercase ::= "A".."Z"
 digit ::= "0"..."9"
 """
# Some example of valid and invalid variables
# 1salary = "2000"
# print(lsalary)

salary1 = 2000
print(salary1)

name_ = "Ashsish"
print(name_)

#32 RESERVED KEYWORDS IN PYTHON WHICH CANNOT BE USED AS VARIABLES

import keyword
print(keyword.kwlist)
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except',
'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try',
 'while', 'with', 'yield']

# How do we define a variable
name = "Ashish"
name2, age = "Ashish", 22
print(name2)
print(age)

employeeID = eID = 23
print(employeeID)
print(eID)

# How do we SWAP two numbers without usin any 3rd variables?
a, b = 10, 20
print("A:", a)
print("B:", b)
a, b = b, a
print("After swap A:", a)
print("After swap B:", b)

"""
DATA TYPES IN PYTHON
1. NUMERIC
   a. INTEGER
   b. FLOAT (DECIMAL)
   C. COMPLEX NUMBER
2. STRINGS
3. LISTS
4. TUPLES
5. DICTIONARY
6. SETS
7. BOOLEAN

"""
"""
INTEGER DATA TYPE
--> A number without a decimal point
"""

# What is the limit to define an integer
# JAVA --> -2147483648 to 2147483647
# PYTHON --> NO LIMIT ON HOW LONE THE INTEGER VALUE CAN BE

# a. INTEGERS are represented in 4 types
# DECIMAL FORM (base 10) ---> any number between 0-9
a = 123234

# BINARY FORM (base 2) ---> represent the numbers - prefix Zero  and small b or capital B
b=0b1111
print(b)
b2 = 15
print(bin(b2))

# OCTAL FORM (base 8) ---> represents te between 0 -7 - prefix with Zero and small o or capital O
c=0o123
print(c)
c2 = 83
print(oct(c2))

# HEXADECIMAL FORM (base 16) ---> represents the number between 0-9 and alphabets A-F - prefix with Zero and small x or capital X
d = 0Xface
print(d)
"""
FLOAT DATA TYPE
--> A number with a decimal point is a floating point number
"""
f = -12.1223
print(type(f))

f = 1.2e3
print(f)

"""
COMPLEX DATA TYPE
---> A number which contains a real part and imaginary part
"""
x = 10 + 20j
print(x)
print(type(x))