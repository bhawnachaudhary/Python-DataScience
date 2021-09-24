class Material:
    def __init__(self,name):
        self.name = name
    def Calculate_volume(self,h,w,l):
        return h * w * l

class MetalMaterial(Material):
    pass


m1 = Material('Wood')
m2 = MetalMaterial('steel')


vol = m1.Calculate_volume(100,20,300)
print(m1.name,vol)

vol2 = m2.Calculate_volume(10,200,50)
print(m2.name,vol2)