from abc import ABC, abstractmethod

class IEmployee(ABC):

    @abstractmethod
    def create_employee(self) -> None:
        pass

    @abstractmethod
    def select_employee(self):
        pass


    @abstractmethod
    def update_employee(self): 
        pass


    @abstractmethod
    def delete_employee(self):
        pass