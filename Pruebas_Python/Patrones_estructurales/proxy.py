from abc import ABCMeta, abstractmethod
from time import sleep


class IPerson(metaclass=ABCMeta):
    @abstractmethod
    def person_method():
        """interface method"""

class Person(IPerson):
    def person_method(self):
        print ("I am a person!")

class ProxyPerson(IPerson):

    def __init__(self):
        self.person = Person()

    def person_method(self):
        print ("I am the Proxy functionality")
        sleep(2)
        self.person.person_method()

P1 = ProxyPerson()

P1.person_method()