# ANTES: hay que modificar la clase calculadora para agregar ooperaciones

class Calculadora:
    def calcular(self, tipo, a, b):
        if tipo == "suma":
            return a + b
        elif tipo == "resta":
            return a - b
        
# DESPUES: se pueden agregar mas operaciones sin modificar la calculadora

from abc import ABC, abstractmethod

class Operacion(ABC):
    @abstractmethod
    def calcular(self, a, b):
        pass


class Suma(Operacion):
    def calcular(self, a, b):
        return a + b


class Resta(Operacion):
    def calcular(self, a, b):
        return a - b


class Calculadora:
    def calcular(self, operacion: Operacion, a, b):
        return operacion.calcular(a, b)


# Agrego una como ejempl

class Multiplicacion(Operacion):
    def calcular(self, a, b):
        return a * b
    
calcu = Calculadora()

print (calcu.calcular(Multiplicacion(),5,6))