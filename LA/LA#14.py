# LA 14
# Parent class
class Spiderman():
    def __init__(self, name, age):  
        self.name = name
        self.age = age
    def describeSpiderman(self):
        print(f'''\nName: {self.name.upper()} 
Age: {self.age}''')

# Child class
class Tobey(Spiderman):
    def __init__(self, name, age, movieTitle): 
        super().__init__(name, age)
        self.movieTitle = movieTitle
    def movie_title(self):
        print(f"Movie: {self.movieTitle.upper()}")
        
class Andrew(Spiderman):
    def __init__(self, name, age, movieTitle): 
        super().__init__(name, age)
        self.movieTitle = movieTitle
    def movie_title(self):
        print(f"Movie: {self.movieTitle.upper()}")
        
class Tom(Spiderman):
    def __init__(self, name, age, movieTitle): 
        super().__init__(name, age)
        self.movieTitle = movieTitle
    def movie_title(self):
        print(f"Movie: {self.movieTitle.upper()}")
        
tobey = Tobey("Tobey Maguire", 49, "Spider-man")
andrew = Andrew("Andrew Garfield", 41, "The Amazing Spider-man")
tom = Tom("Tom Holland", 28, "Spider-man: No Way Home")

tobey.describeSpiderman()
tobey.movie_title()
andrew.describeSpiderman()
andrew.movie_title()
tom.describeSpiderman()
tom.movie_title()
