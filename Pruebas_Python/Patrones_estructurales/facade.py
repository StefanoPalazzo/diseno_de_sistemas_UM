# Subsistema: Luces
class Lights:
    def turn_on(self):
        print("Lights turned ON.")

    def turn_off(self):
        print("Lights turned OFF.")

# Subsistema: Aire Acondicionado
class AirConditioner:
    def turn_on(self):
        print("Air Conditioner turned ON.")

    def turn_off(self):
        print("Air Conditioner turned OFF.")

    def set_temperature(self, temperature):
        print(f"Temperature set to {temperature}°C.")

# Subsistema: Cerradura de la puerta
class DoorLock:
    def lock(self):
        print("Doors locked.")

    def unlock(self):
        print("Doors unlocked.")

# Clase Facade
class SmartHomeFacade:
    def __init__(self):
        self.lights = Lights()
        self.ac = AirConditioner()
        self.lock = DoorLock()

    def leave_home(self):
        """Un método simplificado para salir de casa."""
        print("\nPreparing to leave home...")
        self.lights.turn_off()
        self.ac.turn_off()
        self.lock.lock()
        print("You are ready to leave!\n")

    def arrive_home(self):
        """Un método simplificado para llegar a casa."""
        print("\nPreparing to arrive home...")
        self.lock.unlock()
        self.lights.turn_on()
        self.ac.turn_on()
        self.ac.set_temperature(22)
        print("Welcome home!\n")

# Cliente
if __name__ == "__main__":
    # Cliente interactúa solo con la fachada
    smart_home = SmartHomeFacade()

    # Salir de casa
    smart_home.leave_home()

    # Llegar a casa
    smart_home.arrive_home()
