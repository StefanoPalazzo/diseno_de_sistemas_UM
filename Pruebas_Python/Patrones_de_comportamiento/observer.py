from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


# Subject interface
class Product(ABC):
    @abstractmethod
    def attach(self, observer: Observer) -> None:
        """Attach an observer to the product."""
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        """Detach an observer from the product."""
        pass

    @abstractmethod
    def notify(self) -> None:
        """Notify all observers about a price change."""
        pass


# Concrete Subject
class ConcreteProduct(Product):
    
    _observers = []

    def __init__(self, name: str, price: float):
        
        self.name = name
        self._price = price

    def attach(self, observer: Observer) -> None:
        print(f"{self.name}: Attached an observer.")
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        """Notify all observers about the price change."""
        print(f"{self.name}: Notifying observers about price change...")
        for observer in self._observers:
            observer.update(self)

    def set_price(self, new_price: float) -> None:
        """Set a new price and notify observers if it changes."""
        if new_price != self._price:
            print(f"{self.name}: Price changed from {self._price} to {new_price}")
            self._price = new_price
            self.notify()

    def get_price(self) -> float:
        return self._price


# Observer interface
class Observer(ABC):
    @abstractmethod
    def update(self, product: Product) -> None:
        """Receive update from product."""
        pass


# Concrete Observers
class Customer(Observer):
    def __init__(self, name: str):
        self.name = name

    def update(self, product: Product) -> None:
        print(f"{self.name} has been notified: New price of {product.name} is ${product.get_price():.2f}")


class MarketingDepartment(Observer):
    def update(self, product: Product) -> None:
        print(f"Marketing department has been notified: Price change on {product.name}. New price is ${product.get_price():.2f}")


if __name__ == "__main__":
    # Create a product
    product = ConcreteProduct("Laptop", 1200.00)

    # Create observers
    customer1 = Customer("Alice")
    customer2 = Customer("Bob")
    marketing = MarketingDepartment()

    # Attach observers to the product
    product.attach(customer1)
    product.attach(customer2)
    product.attach(marketing)

    # Change the price
    product.set_price(1150.00)
    product.set_price(1100.00)

    # Detach an observer and change the price again
    product.detach(customer2)
    product.set_price(1050.00)
