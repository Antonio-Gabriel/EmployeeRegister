from abc import ABC, abstractmethod

class IResidence(ABC):

    @abstractmethod
    def create_residence(self) -> None:
        pass

    @abstractmethod
    def select_residence(self):
        pass


    @abstractmethod
    def update_residence(self): 
        pass


    @abstractmethod
    def delete_residence(self):
        pass