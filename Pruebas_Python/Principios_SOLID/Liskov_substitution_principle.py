# ANtes: las subclases deben poder sustituir a sus clases base sin alterar el comportamiento del programa.
# Acá si altera el comportamiento, da error
class Ave:
    def volar(self):
        print("Volando")

class Pinguino(Ave):
    def volar(self):
        raise Exception("Los pingüinos no pueden volar")
    
def hacer_volar_pajaro(pajaro):
    pajaro.volar() 


# hacer_volar_pajaro(Pinguino()) 

#DESPUES: 

class Ave1:
    def volar(self):
        pass

class AveQueVuela1(Ave1):
    def volar(self):
        print("Volando")

class Pinguino1(Ave1):
    def caminar(self):
        print("Caminando en la nieve")

def hacer_volar_pajaro(pajaro):
    pajaro.volar() 


hacer_volar_pajaro(Pinguino1()) # No pasa nada por el pass
