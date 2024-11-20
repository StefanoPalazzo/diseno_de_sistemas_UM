from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any

class House:
    def __init__(self):
        self.walls = None
        self.windows = None
        self.doors = None
        self.garage = None
        self.swimming_pool = None
        self.garden = None
    def __str__(self):
        return (f"House with: \n"
                f"- Walls: {self.walls}\n"
                f"- Doors: {self.doors}\n"
                f"- Windows: {self.windows}\n"
                f"- Garage: {'Yes' if self.garage else 'No'}\n"
                f"- Swimming Pool: {'Yes' if self.swimming_pool else 'No'}\n"
                f"- Garden: {'Yes' if self.garden else 'No'}")



class Builder(ABC):

    @abstractmethod
    def build_walls(self):
        pass

    @abstractmethod
    def build_windows(self):
        pass

    @abstractmethod
    def build_doors(self):
        pass

    @abstractmethod
    def add_swimming_pool(self):
        pass

    @abstractmethod
    def add_garage(self):
        pass

    @abstractmethod
    def add_garden(self):
        pass


class StandardHouseBuilder(Builder):

    def __init__(self):
        self.reset()

    def reset(self):
        self.house = House()

    def build_walls(self):
        self.house.walls = "Brick Walls"
        return self

    def build_doors(self):
        self.house.doors = "Wooden doors"
        return self

    def build_windows(self):
        self.house.windows = "Glass windows"
        return self

    def add_garage(self):
        self.house.garage = True
        return self

    def add_swimming_pool(self):
        self.house.swimming_pool = False
        return self

    def add_garden(self):
        self.house.garden = True
        return self

    def get_result(self) -> House:
        return self.house

class Director:
    def __init__(self, builder: Builder):
        self.builder = builder

    def construct_minimal_house(self):
        return (self.builder
                .build_walls()
                .build_doors()
                .get_result())
    
    def construct_full_house(self):
        return (self.builder
                .build_walls()
                .build_doors()
                .build_windows()
                .add_garage()
                .add_swimming_pool()
                .add_garden()
                .get_result())



# Uso del patrón Builder
if __name__ == "__main__":
    # Crear una casa estándar
    standard_builder = StandardHouseBuilder()
    director = Director(standard_builder)

    print("Standard Minimal House:")
    minimal_house = director.construct_minimal_house()
    print(minimal_house)

    print("\nStandard Full House:")
    full_standard_house = director.construct_full_house()
    print(full_standard_house)



