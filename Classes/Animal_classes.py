class Dog:
    #class variable
    age = 0
    color = 'brown'
    breed = 'german shepard'
    eyecolor = 'black'
    height = 10
    weight = 15
    kind = 'pet'
    
    #instance method
    def bark(self):  #'self' indicates that bark function belongs to class 'Dog'
        print('bow bow'*3)
    def eat(self,food):
        print(f'dog eats{food}')




class Goat:
    #classs variable
    age = 0
    color = 'black'
    height = 10

    #instance method
    def eat_leaves(self):
        print('the goat eats some leaves')





moti = Dog()
moti.breed = 'hybrid'
moti.age = 5
moti.color = 'multicolor'

tiger = Dog()

moti.bark()
tiger.bark()
print("moti details>> ",moti.age,moti.breed,moti.color)
print("tiger details>> ",tiger.age,tiger.breed,tiger.color)

malti = Goat()
malti.eat_leaves()