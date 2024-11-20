from __future__ import annotations
from abc import ABC, abstractmethod


# State: Interfaz base para los estados
class State(ABC):
    @abstractmethod
    def atende(self, context: BankCounter) -> None:
        pass


# ConcreteState: Estado Abierto
class OpenState(State):
    def atende(self, context: BankCounter) -> None:
        print("Ventanilla abierta: Atendiendo al cliente.")
        # Opcionalmente, cambiar a otro estado después de atender
        context.set_state(WaitingState())


# ConcreteState: Estado Cerrado
class ClosedState(State):
    def atende(self, context: BankCounter) -> None:
        print("Ventanilla cerrada: No podemos atender. Por favor, regrese más tarde.")


# ConcreteState: Estado En Espera
class WaitingState(State):
    def atende(self, context: BankCounter) -> None:
        print("Ventanilla en espera: Por favor, espere un momento.")
        # Simulamos que la ventanilla vuelve a abrir
        context.set_state(OpenState())


# Context: El banco
class BankCounter:
    def __init__(self):
        self._state: State = ClosedState()  # Estado inicial

    def set_state(self, state: State) -> None:
        self._state = state
        print(f"Cambio de estado: {self._state.__class__.__name__}")

    def atende(self) -> None:
        self._state.atende(self)


# Cliente: Simulación del banco
if __name__ == "__main__":
    # Creamos la ventanilla del banco
    bank_counter = BankCounter()

    # Intentamos atender (estado inicial: cerrado)
    bank_counter.atende()

    # Abrimos la ventanilla
    bank_counter.set_state(OpenState())
    bank_counter.atende()

    # La ventanilla entra en espera
    bank_counter.atende()

    # Volvemos a atender (automáticamente pasó a abierto)
    bank_counter.atende()
