from abc import ABC, abstractmethod

class Bebida(ABC):

    def preparar(self):
        # Pasos para preparar
        self.hervir_agua()
        self.preparar_base()
        self.servir_en_taza()
        self.agregar_condimentos()

    def hervir_agua(self):
        print("Hirviendo agua")

    def servir_en_taza(self):
        print("Sirviendo en la taza")

    @abstractmethod
    def preparar_base(self):
        """Reemplazar"""
    
    @abstractmethod
    def agregar_condimentos(self):
        """Reemplazar"""

class Te(Bebida):

    def preparar_base(self):
        print("Infusionando el té")
    
    def agregar_condimentos(self):
        print("Agregando azucar")

class Cafe(Bebida):

    def preparar_base(self):
        print("Preparando el café")
    
    def agregar_condimentos(self):
        print("Agregando azucar y leche")


if __name__ == "__main__":
    print ("Preparando té: ")
    te = Te()
    te.preparar()
    print ("--------------")
    print("Preparando café:")
    cafe = Cafe()
    cafe.preparar()