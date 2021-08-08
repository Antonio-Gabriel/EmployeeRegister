
from src.repository.EmployeeRepository import EmployeeRepository
from uuid import uuid1
from typing import Type
from .Residence import Residence

class Employee:

    def __init__(self, name: str, email: str, phone: int, residence: Type[Residence]) -> None:
        self.__name = name        
        self.__email = email
        self.__phone = phone
        self.__residence = residence
        self.__repository = EmployeeRepository()


    def create(self) -> list:       
                 
        response = self.__repository.create_employee(**{
            "id_employee": str(uuid1()),
            "name": self.__name,
            "email": self.__email,
            "phone": self.__phone,
            "district": self.__residence._.get("district"),
            "location": self.__residence._.get("location"),
            "resid_number": self.__residence._.get("resid_number")
        })

        print(response)


    def select(self):
        return self.__repository.select_employee()


    def update(self, identifier: str) -> list:

        return self.__repository.update_employee(**{
            "id_employee": identifier,
            "name": self.__name,
            "email": self.__email,
            "phone": self.__phone,
            "district": self.__residence._.get("district"),
            "location": self.__residence._.get("location"),
            "resid_number": self.__residence._.get("resid_number")
        })


    def delete(self, identifier: str):
        return self.__repository.delete_employee(identifier)

    
    def count(self):
        return len(self.select())