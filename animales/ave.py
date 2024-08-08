from animales import animales
class ave(animales):
    pass

    def __init__(self, nombre, peso, año_nacimiento, propietario):
        super().__init__(nombre, peso)
        
        self.año_nacimiento = año_nacimiento
        self.propietario = propietario
        
    def calcular_edad(self):
        año_actual = 2024 
        edad = año_actual- self.año_nacimiento
        if edad > 5:
            return "MAYOR DE EDAD"
        else:
            return "MENOR DE EDAD"
    
        

MiAve= ave("Guacamayo", "1Kg", 2017, "Jose")

print("El animal es un",MiAve.nombre, "pesa",MiAve.peso, "nacio en el",MiAve.año_nacimiento, "y su propietario es", MiAve.propietario, "es", MiAve.calcular_edad())