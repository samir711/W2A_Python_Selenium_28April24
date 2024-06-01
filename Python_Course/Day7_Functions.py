"""
FUNCTIONS

--> It is a sequence of statements that can be executed in a particular oder
--> This sequence of statements cn be given a logical name
--> Re-Usable code

SYNTAX:

   def functionName():
   ------------------
   ---------------------
   ---------------------
   -----------------

"""


# How to define a function ?
def greet():
    """
    This is a greeting function.
    :return:None
    """
    print("This is a greeting function.")


# How to call the function?
print("This is before calling the function")
greet()
print("This is after calling the function")


# What are functions parameters and arguments?
def studentData(studentName, studentRoll, studentSection, studentMarks):  # Function Paramter
    print(f"Hi {studentName}, your roll number is -{studentRoll}")
    print(f"Your section is - {studentSection} and marks are - {studentMarks}")


print("This is before calling the function")
studentData("Samir", 20, "A", 98)  # Function arguments
studentData("Abhinav", 21, "B", 100)  # Function arguments
print("This is after calling the function")

"""
RETUNN STATEMENT
"""
def calculate(number1, number2, operation):
    if operation == "Add":
        result = number1 + number2
        return result
    elif operation == "Sub":
        result = number1 - number2
        return result
    elif operation == "Mul":
        result = number1 * number2
        return result
    else:
         print("Incorrect Operation. Try again!")

print("\n\n######################")
# newResult = calculate(12, 12, "Add") + 20 # TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'
# print(newResult)

newResult = calculate(12, 12, "Sub") + 20
print(newResult)

"""
Different types of arguments
    1. Positional arguments
    2. Keywords arguments
    3. Default arguments
    4. Variable length arguments
"""

def welcome(name, country):
    print(f"Hi {name}, Welcome to  {country}")


print("\n\n######## POSITIONAL ARGUMENTS ##############")
welcome("Ashish","India")
# welcome("Ashish") # TypeError: welcome() missing 1 required positional argument: 'country'

print("\n\n######### KEYWORD ARGUEMENTS #############")
welcome(name="Ashish",country="India")

print("\n\n######### DEFAULT ARGUEMENTS #############")
def welcome(name,country,department="IT"):
    print(f"Hi {name}, Welcome to {country} and your department is - {department}")

welcome("Nikhil","USA")
welcome("Abhishek","CHINA", "BANK")

print("\n\n######### VARIABLE LENGTH ARGUEMENTS #############")
# ASSIGNMENT