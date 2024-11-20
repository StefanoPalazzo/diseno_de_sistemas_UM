from __future__ import annotations
from abc import ABC, abstractmethod


class IAprobador(ABC):
    """
    Interface que define el método para manejar la solicitud de aprobación y
    un método para establecer el siguiente aprobador en la cadena.
    """

    @abstractmethod
    def set_siguiente(self, aprobador: IAprobador) -> IAprobador:
        pass

    @abstractmethod
    def manejar_solicitud(self, monto: float) -> None:
        pass


class AprobadorBase(IAprobador):
    """
    Clase base para aprobadores que implementa el manejo de la cadena de responsabilidad.
    """

    def __init__(self):
        self._siguiente: IAprobador | None = None

    def set_siguiente(self, aprobador: IAprobador) -> IAprobador:
        self._siguiente = aprobador
        return aprobador

    def manejar_solicitud(self, monto: float) -> None:
        if self._siguiente:
            self._siguiente.manejar_solicitud(monto)
        else:
            print("No hay nadie disponible para manejar esta solicitud.")


class EjecutivoCuenta(AprobadorBase):
    """
    Clase para el Ejecutivo de Cuenta que maneja solicitudes de hasta $10,000.
    """

    def manejar_solicitud(self, monto: float) -> None:
        if monto <= 10000:
            print(f"Ejecutivo de cuenta aprobó el préstamo de ${monto}.")
        else:
            print("Ejecutivo de cuenta pasa la solicitud al siguiente nivel.")
            super().manejar_solicitud(monto)


class LiderEquipo(AprobadorBase):
    """
    Clase para el Líder de Equipo que maneja solicitudes entre $10,001 y $50,000.
    """

    def manejar_solicitud(self, monto: float) -> None:
        if 10000 < monto <= 50000:
            print(f"Líder de equipo aprobó el préstamo de ${monto}.")
        else:
            print("Líder de equipo pasa la solicitud al siguiente nivel.")
            super().manejar_solicitud(monto)


class Gerente(AprobadorBase):
    """
    Clase para el Gerente que maneja solicitudes entre $50,001 y $100,000.
    """

    def manejar_solicitud(self, monto: float) -> None:
        if 50000 < monto <= 100000:
            print(f"Gerente aprobó el préstamo de ${monto}.")
        else:
            print("Gerente pasa la solicitud al siguiente nivel.")
            super().manejar_solicitud(monto)


class Director(AprobadorBase):
    """
    Clase para el Director que maneja solicitudes superiores a $100,000.
    """

    def manejar_solicitud(self, monto: float) -> None:
        if monto > 100000:
            print(f"Director aprobó el préstamo de ${monto}.")
        else:
            print("Director no puede manejar la solicitud.")
            super().manejar_solicitud(monto)


# Configuración de la cadena de responsabilidad
ejecutivo = EjecutivoCuenta()
lider = LiderEquipo()
gerente = Gerente()
director = Director()

# Se establece la cadena
ejecutivo.set_siguiente(lider).set_siguiente(gerente).set_siguiente(director)

# Cliente solicita aprobación
montos = [5000, 20000, 75000, 150000]

for monto in montos:
    print(f"\nSolicitando aprobación para ${monto}:")
    ejecutivo.manejar_solicitud(monto)
