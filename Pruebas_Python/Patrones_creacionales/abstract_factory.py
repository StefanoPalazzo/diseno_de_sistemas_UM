from abc import ABC, abstractmethod

class abstractTV(ABC):
    @abstractmethod
    def turn_on(self):
        pass

class AppleTV(abstractTV):
    def turn_on(self):
        print ("Turning on Apple TV, say 'Hey Siri'.")

class SamgungTV(abstractTV):
    def turn_on(self):
        print ("Turning on Samguns TV, say 'Okay Google'")
        


class abstractPhone(ABC):
    @abstractmethod
    def turn_on(self):
        pass

class ApplePhone(abstractPhone):
    def turn_on(self):
        print ("Use Face ID to unlock")

class SamsungPhone(abstractPhone):
    def turn_on(self):
        print ("Use Iris to unlock")

class AbstractFactory(ABC):
    @abstractmethod
    def create_phone(self):
        pass

    def create_tv(self):
        pass

class AppleFactory(AbstractFactory):
    def create_phone(self):
        return ApplePhone()
    
    def create_tv(self):
        return AppleTV()
    
class SamgungFactory(AbstractFactory):
    def create_phone(self):
        return SamsungPhone()
    def create_tv(self):
        return SamgungTV()
    
def client(factory: AbstractFactory):
    phone = factory.create_phone()
    tv = factory.create_tv()
    print("Using the phone:")
    phone.turn_on()

    print("Using the TV:")
    tv.turn_on()
    

if __name__ == '__main__':
    factory_A = AppleFactory()
    factory_S = SamgungFactory()
    print ("Apple Client")
    AppleClient = client(factory_A)
    print ("Samgung Client")

    SamsungClient = client(factory_S)
    

    


