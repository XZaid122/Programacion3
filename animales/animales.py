class animales:
    
    def __init__(self, nombre, peso):
        
        self.nombre = nombre
        self.peso = peso
        
    def printanimal(self):
        print(self.nombre, self.peso)
    

x = animales("Doky","30kg")
x.printanimal()

