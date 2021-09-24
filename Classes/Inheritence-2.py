class Fruit:
    def __init__(self,name,taste,color,shape,size):
        self.name = name
        self.taste = taste
        self.color = color
        self.shape = shape
        self.size = size

    def show(self):
        print("Fruit details")
        print(f'name = {self.name}')
        print(f'taste = {self.taste}')
        print(f'color = {self.color}')
        print(f'shape = {self.shape}')
        print(f'size = {self.size}')
        
    def make_ripe(self,new_color):
        self.color = new_color

class Melon(Fruit):

    #OVERRIDE
    def __init__(self,name,taste,color,shape,size,region):
        super().__init__(name,taste,color,shape,size)   #super class constructor also updated
        self.region = region    #added a new property to Melon

    def sellMelon(self,price):
        print(f'Sell {self.name} for {price}')
    def purchaseMelon(self,price):
        print(f'Purchased {self.name} for {price}')
    
    def show(self):
        #override
        super().show()
        print(f'found in region= {self.region}')

print(dir(Melon)) #displays all the functions inside the class Melon

m1 = Melon('watermelon','big','Dark Green','sweet','spherical','Africa')
m1.show()
m1.purchaseMelon(200)