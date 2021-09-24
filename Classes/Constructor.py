class Movie:
    #constructor
    def __init__(self,title,duration,year,director,cast=[],genre=[]): 
        # instance variables
        self.title = title
        self.duration = duration
        self.year = year
        self.director = director
        self.cast = cast
        self.genre = genre
        print('yo subject completed')


    # instance method
    def info(self):
         print(f'Movie Details>> {self.title}')
         print(f'Release Year>> {self.year}')
         print(f'Duration>> {self.duration}')   
         print(f'director>> {self.director}')
         print(f'Caste>> ')
         for people in self.cast:
             print(f'-->>{people.genre}')
         print(f"Genre>> {'/'.join(self.genre)}")




m1 = Movie('Rainmaker','95 mins',1997,'Francis Ford Coppola',genre = ['Crime','Drama'])
m2 = Movie('Avenger','100 mins',2015,'Josh Whedon')
# print(m1)
# print(m2)

m1.info()
m2.info()