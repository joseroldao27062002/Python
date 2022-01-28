from abc import ABC, abstractmethod
class Dispositivo(ABC):
    def __init__(self, ipAddress, macAddress):
        self.__ipAddress = ipAddress
        self.__macAddress = macAddress
        
    #métodos getter
    @property
    def ipAddress(self):
        return self.__ipAddress

    @property
    def macAddress(self):
        return self.__macAddress

    #Métodos setter
    @ipAddress.setter
    def ipAddress(self, ipAddress):
        self.__ipAddress = ipAddress
    
    @macAddress.setter
    def macAddress(self, macAddress):
        self.__macAddress = macAddress


