from abc import ABC, abstractmethod

class Persona(ABC):
    def _init_(self, nombre, apellido, edad, codigo):
        self.nombre = nombre
        self.apellido=apellido
        self.edad = edad
        self.codigo=codigo
        
    @abstractmethod
    def presentarse(self):
        pass

class Estudiante(Persona):
    def presentarse(self):
        return" hola soy {} {} tengo {} años soy tu compañero de clases, codigo: {} ".format(self.nombre,self.edad,self.apellido,self.codigo) 
class Compañero(Persona):
    def presentarse(self):
        return" hola soy {} {} tengo {} años soy tu compañero de clases, codigo: {} ".format(self.nombre,self.edad,self.apellido,self.codigo) 
class Compañera(Persona):
   def presentarse(self):
        return" hola soy {} {} tengo {} años soy tu compañera de clases codigo: {} ".format(self.nombre,self.edad,self.apellido,self.codigo) 
def presentarse_persona(persona):
    print(persona.presentarse())

alumno = Estudiante("roman", "Mejia", 18, "u2020202")
estudiante1 = Compañero("andrea", "martinez", 25, "u35665446")
Estudiante2 = Compañera("belinnda", "morales", 19, "U2020203")

presentarse_persona(alumno)
presentarse_persona(estudiante1)
presentarse_persona(Estudiante2)