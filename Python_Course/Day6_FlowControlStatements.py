"""
FLOW CONTROL STATMENTS
"""

"""
PYTHON FLOW CONTROL STAEMENTS

   1. SELECTION STATEMENTS
       --> IF BLOCK
       --> IF ELSE BLOCK
       --> IF ELIF BLOCK
       --> IF ELIF ELSE BLOCK
       
   2. INTERACTIVE STATEMENTS
      --> FOR LOOPS
      --> WHILE LOOPS
      
   3. TRANSFER STATEMENTS
     --> BREAK
     --> CONTINUE
     ---> PASS
"""
"""
SELECTION STATEMENTS
"""
print("######################### SELECTION STATEMENTS ######################### ")
print("-----------------------IF BLOCK -------------------------------")
# studentMarks = int(input("Enter student's marks - "))
studentMarks = 95
if studentMarks > 91:
    print("Congratulation, The student has pass with A+ grade!")

print("This is out of the IF block.")

print("-----------------------IF ELSE BLOCK -------------------------------")
# studentMarks = int(input("Enter student's marks - "))
studentMarks = 95
if studentMarks > 91:
    print("Congratulation, The student has pass with A+ grade!")
else:
    print("Student nees more practise! ")

print("This is out of the IF block.")

print("-----------------------IF ELIF BLOCK -------------------------------")
# studentMarks = int(input("Enter student's marks - "))
studentMarks = 95
if studentMarks > 91:
    print("Congratulation, The student has pass with A+ grade!")
elif 80 < studentMarks <=90:
    print("Student has passed with B+ grade!  Needs more practise! ")
elif 70 < studentMarks <=80:
    print("Student has passed with C+ grade!  Needs more attention and focus. ")
elif 60 < studentMarks <=70:
    print("Student is at the border line with D+ grade. Needs a lot of practise and attention. ")

print("This is out of the IF block.")


print("-----------------------IF ELIF ELSE BLOCK -------------------------------")
# studentMarks = int(input("Enter student's marks - "))
studentMarks = 66
if studentMarks > 91:
    print("Congratulation, The student has pass with A+ grade!")
elif 80 < studentMarks <=90:
    print("Student has passed with B+ grade!  Needs more practise! ")
elif 70 < studentMarks <=80:
    print("Student has passed with C+ grade!  Needs more attention and focus. ")
elif 60 < studentMarks <=70:
    print("Student is at the border line with D+ grade. Needs a lot of practise and attention. ")
else:
    print('Student FAILED!')

print("This is out of the IF block.")

print("\n\n######################### INTERACTIVE STATEMENTS ######################### ")
print("\n\n-----------------------FOR LOOP -------------------------------")

"""
FOR LOOPS
  --> Executing a group of statements in a order, multiple times.
  --> SYNTAX:
        FOR X IN SEQUENCE:
            -----------------------------
            -----------------------------
            -----------------------------
            -----------------------------
 --> SEQUENCE:
     1. List
     2. Dictionary
     3. String
     4. Tuple
     5. Set
     6. Range()
"""
print("\n************** FOR LOOPS --> STRING SEQUENCE ************** ")

for loopVariable in "Way2Automation":
    print(f'Valuf of loopVariable is - {loopVariable}')

print("\n************** FOR LOOPS --> STRING SEQUENCE ************** ")

for loopVariable in "Way2Automation":
    print(f'Valuf of loopVariable is - {loopVariable}')

print("\n************** FOR LOOPS --> LIST SEQUENCE ************** ")

for loopVariable in [1, 2, 3, 4, 5, 6, "Ashist", "Samir", True, 6+3j, ("Apple", "Mango")]:
    print(f'Valuf of loopVariable is - {loopVariable}')

for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
    if i %  2 == 0:
        print(f"The number - {i} is an even number. ")
    else:
        print(f"The number - {i} is an odd number. ")

print("\n************** FOR LOOPS --> TUPLE SEQUENCE ************** ")
count = 0
for i in (1, 2, "Ashish", "Address", 12312, 67.8, "D"):
    print(f" for index - {count}, the value is - {i}")
    count = count + 1

print("\n************** FOR LOOPS --> DICTIONARY SEQUENCE ************** ")

example = {
    "studentName" : "Ashish",
    "studentAge" : 20,
    "studentMarks" : [10, 20, 30, 40],
    "Address": {
        "City": "New delhi",
        "State": "Delhi",
        "HNo":   30
    },
    45: 10
}

# How to get all the keys of the dictionary?
for keys in example:
    print(f"The key is - {keys}")

# How to get all the values of the dictionary?
for values in example.values():
    print(f"The value is - {values}")

print("\n************** FOR LOOPS --> SET SEQUENCE ************** ")





