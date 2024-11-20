class Singleton:
    _instance = None  # Variable de clase para almacenar la instancia única

    def __new__(cls):
        if cls._instance is None:  # Si no existe, crea una nueva instancia
            cls._instance = super().__new__(cls)
        return cls._instance



singleton1 = Singleton()
singleton2 = Singleton()

print(singleton1 is singleton2)  
