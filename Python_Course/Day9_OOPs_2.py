"""
OPPS CONTINUED....
"""

"""
INHERITANCE
 --->   When we inherit some parents properties into child
 ---> When we inherit some parents actions/methods into child
 
class a:  --> BASE CLASS OR PARENT CLASS
  var_1 = ""
  var_2 = ""
  
  def functions_1():
      ------------------------
      ------------------------

  def functions_2():
      ------------------------
      ------------------------

  class b(a/nameOfTheParentClass): --> DERIVED CLASS OR CHILD CLASSS
  var_3 = ""
  
  def function_3():
    -----------------------------
    -----------------------------
    
Different types of inheritance:
  1. Single
  2. Multiple
  3. Multi-level
  4. Hypbrid
  5. Hierarchical
"""
"""
  SINGLE INHERITANCE
    ---> This inherits teh properties / methods from teh base class directly  
  
"""

class parent:
    bookName = "WayAutomation"
    bookAuthor = "Ashish"

    def bookInfor(self):
        return f"The namd of the book is  -{self.bookName} and author is - {self.bookAuthor}"

class child(parent):
    publisherName = "XYZ Company"
    publisherAdd = "ABC Road"

    def publisherInfo(self):
        return f"the publisher nae is - {self.publisherName} situated at {self.publisherAdd}"


obj_parent = parent()
info = obj_parent.bookInfor()
print(info)

obj_child = child()
info_2= obj_child.bookInfor()
print(info_2)

"""
MULTI-LEVEL INHERITANCE
  --> Child inherits from parents, --> parent inherit from there parents
"""
print("\n\n########################## MULTIPLE INHERITANCE ###########################")
class parent:
    bookName = "WayAutomation"
    bookAuthor = "Ashish"

    def bookInfor(self):
        return f"The namd of the book is  -{self.bookName} and author is - {self.bookAuthor}"

class child(parent):
    publisherName = "XYZ Company"
    publisherAdd = "ABC Road"

    def publisherInfo(self):
        return f"the publisher nae is - {self.publisherName} situated at {self.publisherAdd}"

class grandChild(parent):
    shopName = "ABC SHOP"
    shopAdd = "WET Road"

    def shopInfo(self):
        return f"Shop name is - {self.shopName} abd address is {self.shopAdd}"


obj = grandChild()
info = obj.shopInfo()
print(info)
info_2 = obj.bookInfor()

"""
HIERARCHICAL INHERITANCE
   --> When multiple childer
"""

"""
ACCESS MODIFIERS
   1.PUBLIC
       ---> Nothing is required. By default the functions and variables are PUBLIC in nature
   2. PROTECTED
       ---> Functions and variables of the class can be used by its own objects only
       ---> We define it using (Leading underscore: _)
   3. PRIVATE
       --> Functions and variables of the class cannot be used by its own object as well.
       --> They are only accessible within the class
       --> We define it using double leading underscore (__)
"""

class Access_1:
    def __init__(self):
        self._protectedVariable = "This is a protected variable and can be used with this class objects only"
    def _protectedFunction(self):
        return f"Data = {self._protectedVariable}"

    def basicFuntion(self):
        return "Inside Access 1 , this is a public function"

class Child(Access_1):
    def childFunction(self):
        return "This is the child function"

print("\n\n\################## ACCESS MODIFIERS ####################################")
obj = Child()
obj.childFunction()
obj.basicFuntion()






