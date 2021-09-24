class Rectangle:

    def __int__(self,h,w):
        self.height = h
        self.width = w

    def Area(self):
        return self.height * self.width

item1 = Rectangle(10,10)
item2 = Rectangle(5,10)
item3 = Rectangle(3,50)

if item1.Area() > item2.Area() and item1.Area() > item3.Area():
    print(f'Item1 is bigger')
elif item2.Area() > item1.Area() and item2.Area()>item3.Area():
    print(f'item2 is bigger')
else:
    print(f'item3 is bigger')
