"""
OOPS CONCEPT
"""

"""
OOPS - Object Oriented Programming
   1. Class
   2. Object
   3. Inheritance
   4. Polymorphism
   5. Encapulation
   6. Abstract Classes
   7. Access Modifiers
   8. Interface
   
"""

"""
CLASS
      -->  It is a blue-print that is used to create actual items
      -->  Logical representation
      -->  It can contains multiple properties and actions
      -->  The properties are represented as variables
      -->  Actions are represented using functions
      
"""
class book:
    def __init__(self,title, author, price, shelf_number):
        self.title = title
        self.author = author
        self.price = price
        self.shelf = shelf_number
    def getTitle(self):
        return f"Title of book = {self.title}"

    def getAuthor(self):
       return f"For {self. title} author of the book = {self.author}"

    def getPrice(self):
        return f" For {self.title} Price of the book = {self.price}"

    def getShelfNumber(self):
        return f" For {self.title} Shelf of the book = {self.shelf}"


book1 = book("Title 1", "Author 1" , 100, 13.21)
book2 = book("Title 2", "Author 2", 200, 11.24)
book3 = book("Title 3", "Author 3", 500, 1.4)

print(book1.getTitle())
print(book2.getAuthor())
print(book3.getPrice())

class movies:
    """ This is a movie class """
    def __init__(self, name, actor, actress):
        self.name = name
        self.actor = actor
        self.actress = actress

    def movieInformation(self):
        print("\n########## MOVIE INFORMATION ########")
        print(f"Name of the movie - {self.name}")
        print(f"Action in the movie - {self.actor}")
        print(f"Actress in the movie - {self.actress}")


listOfMovies = []
while True:
    name = input("Enter the name of the movie - ")
    actor = input("Enter the actor in the movie - ")
    actress = input("Enter the actesss in the movie")
    movie = movies(name, actor, actress)
    listOfMovies.append(movie)
    print("Successfully Added!")
    option = input("Do you want to add more movie info? (Y or N) -")
    if option == "N":
        break

print(listOfMovies)
for i in listOfMovies:
    i.movieInformation()
















