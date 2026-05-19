""""Definición (El Molde):
class Persona: ... self.nombre = nombre
Creación (El Objeto):
variable = Clase(datos) -> Ej: p1 = Persona("Juan")
Uso (El Punto):
variable.atributo -> Ej: p1.nombre"""
# CLASE CON ATRIBUTOS FIJOS
class Celular():
    marca = "Samsung"
    modelo = "Galaxy S20"
    pixeles = "64MP"
    memoria = "128GB"       
celular1 = Celular()
print(celular1.marca)


# CLASE CON ATRIBUTOS DE INSTANCIA
class guerrero():
    def __init__(self, nombre, vida, fuerza, ataque):
        self.nombre = nombre
        self.vida = vida
        self.fuerza = fuerza
    
    def atacar(self, ataque):
        self.ataque = ataque
        ataque = self.fuerza
        
warrior = guerrero("Espartaco", 100, 40, 60,)
print(warrior.nombre)

class Estudiantes():
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
        #self.estudiar() #llamar otro metodo desde dentro
        #self.mostrarDatos()#llamando al metodo mostrar de abajo
    def estudiar(self):
        print(f"el estudiante llamado; {self.nombre}, esta estudiando")
    def mostrarDatos(self):
        print(f"Sus datos son: Nombre; {self.nombre}, edad; {self.edad} y {self.grado}")

nombre, edad, grado = input("Ingrese el nombre del estudiante: "), input("Ingrese la edad del estudiante: "), input("Ingrese el grado del estudiante: ")
estudiante1 = Estudiantes(nombre, edad, grado)#CREACION DE INSTANCIA PERO CON UN INPUT SOLO RECIBIRIA UN DATO, PARA LOS OTROS DOS ATRIBUTOS SE PODRIA HACER CON OTROS INPUTS DENTRO DEL METODO __init__ O SE PODRIA HACER CON VALORES POR DEFECTO EN LOS PARAMETROS DE LA FUNCION __init__
#llamar metodo de una clase
estudiante1.estudiar()
estudiante1.mostrarDatos()

class alumno(Estudiantes):
    def __init__(self, nombre, edad, grado, materia):
        super().__init__(nombre, edad, grado)
        self.materia = materia
    def mostrarDatos1(self):
        print(f"Sus datos son: Nombre; {self.nombre}, edad; {self.edad} y {self.grado} y su materia es: {self.materia}")
        
    
materia = input("Ingrese la materia del alumno: ")
alumno1 = alumno(nombre, edad, grado, materia)
alumno1.mostrarDatos1()