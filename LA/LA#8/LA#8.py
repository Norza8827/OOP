# LA 8
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

libro = Book("Noli Me Tangere", "Jose Rizal")
libro1 = Book("How to Read a Book", "Mortimer Adler")

print("")
print(f'''Book: {libro.title}
Author: {libro.author}''')

print("")
print(f'''Book: {libro1.title}
Author: {libro1.author}''')

print("---------------------------")
print("")

del libro.author

#print(f'''Book: {libro.title}
#Author: {libro.author}''')

print("")

print(f'''Book: {libro1.title}
Author: {libro1.author}''')
