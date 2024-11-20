from abc import ABC, abstractmethod

# Servidor Abstracto

class IServer(ABC):
    @abstractmethod
    def encender(self):
        pass

    @abstractmethod
    def apagar(self):
        pass

    @abstractmethod
    def reiniciar(self):
        pass

# Servidores concretos

class ServidorLinux(IServer):
    def encender(self):
        print("Servidor Linux: Encendiendo...")

    def apagar(self):
        print("Servidor Linux: Apagando...")

    def reiniciar(self):
        print("Servidor Linux: Reiniciando...")


class ServidorWindows(IServer):
    def encender(self):
        print("Servidor Windows: Encendiendo...")

    def apagar(self):
        print("Servidor Windows: Apagando...")

    def reiniciar(self):
        print("Servidor Windows: Reiniciando...")


# Interfaz Command

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

# Commands concretos

class EncenderServidorCommand(Command):
    def __init__(self, servidor: IServer):
        self.servidor = servidor

    def execute(self):
        print("Ejecutando comando: Encender servidor.")
        self.servidor.encender()


class ApagarServidorCommand(Command):
    def __init__(self, servidor: IServer):
        self.servidor = servidor

    def execute(self):
        print("Ejecutando comando: Apagar servidor.")
        self.servidor.apagar()


class ReiniciarServidorCommand(Command):
    def __init__(self, servidor: IServer):
        self.servidor = servidor

    def execute(self):
        print("Ejecutando comando: Reiniciar servidor.")
        self.servidor.reiniciar()


# Invocador

class Invocador:
    def __init__(self):
        self.historial = []

    def ejecutar_comando(self, comando: Command):
        comando.execute()
        self.historial.append(comando)

    def mostrar_historial(self):
        print("\nHistorial de comandos ejecutados:")
        for idx, comando in enumerate(self.historial, 1):
            print(f"{idx}. {comando.__class__.__name__}")

# Crear servidores
servidor_linux = ServidorLinux()
servidor_windows = ServidorWindows()

# Crear comandos
encender_linux = EncenderServidorCommand(servidor_linux)
apagar_windows = ApagarServidorCommand(servidor_windows)
reiniciar_linux = ReiniciarServidorCommand(servidor_linux)

# Crear invocador
invocador = Invocador()

# Ejecutar comandos
invocador.ejecutar_comando(encender_linux)
invocador.ejecutar_comando(apagar_windows)
invocador.ejecutar_comando(reiniciar_linux)

# Mostrar historial
invocador.mostrar_historial()
