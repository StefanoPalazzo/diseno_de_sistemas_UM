from abc import ABC, abstractmethod

# Producto base
class Button(ABC):
    @abstractmethod
    def render(self):
        pass

# Productos concretos
class WindowsButton(Button):
    def render(self):
        print("Renderizando un botón de Windows")

class MacOSButton(Button):
    def render(self):
        print("Renderizando un botón de MacOS")

# Creador base
class Dialog(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    def render(self):
        button = self.create_button()
        button.render()

# Creadores concretos
class WindowsDialog(Dialog):
    def create_button(self) -> Button:
        return WindowsButton()

class MacOSDialog(Dialog):
    def create_button(self) -> Button:
        return MacOSButton()

# Uso
dialog = WindowsDialog()
dialog.render()  # Output: Renderizando un botón de Windows

