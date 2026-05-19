import random

class Personajes:
    def __init__(self, nombre, vida, fuerza, defensa):
        self.nombre = nombre
        self.vida = vida
        self.fuerza = fuerza
        self.defensa = defensa
        
    def atacar(self, enemigo):
        daño = self.fuerza - enemigo.defensa
        enemigo.vida -= daño
        print(f"{self.nombre} ataca a {enemigo.nombre} y causa {daño} de daño.")
        
    def __str__(self):
        return f"su nombre es {self.nombre}, su vida es {self.vida}, su fuerza es {self.fuerza} y su defensa es {self.defensa}"

class Guerrero(Personajes):
    def __init__(self, nombre, vida, fuerza, defensa):
        super().__init__(nombre, vida, fuerza, defensa)
        self.nombre = "warrior"
        
numero = random.randint(1, 100)        

