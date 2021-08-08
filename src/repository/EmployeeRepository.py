
from typing import Union
from collections import namedtuple
from src.interface import *
from src.infrastructure import *
from src.helper.Exceptions import *
from src.helper.decorators import *

class EmployeeRepository(IEmployee):
    
    ROOT = db_context_config_root.get("app_root")    
    
    def __init__(self) -> None:
        super().__init__()
        self.__storage = []


    def create_employee(self, **employee_params) -> dict:
         
        employee_data = self.__get_employee(**employee_params)        

        if self.__verify_existent_employee(employee_data, employee_params):
            return { "state": 0, "message": "Usuario Existente1" }        

        response = self.__push_employee_into_db(employee_data)

        if response is not None:
            return { "state": 1, "message": "sucess" }

            
    def select_employee(self) -> Union[namedtuple, None]:      

        Employee = namedtuple("Employee", "id_employee name email phone district location resid_number")
        response_Json = self.__get_employee()
        
        if response_Json != []:

            for i in range(0, len(response_Json)):

                self.__storage.append(
                    Employee(
                        id_employee= response_Json[i]["data"]["id_employee"],
                        name= response_Json[i]["data"]["name"],
                        email= response_Json[i]["data"]["email"],
                        phone= response_Json[i]["data"]["phone"],
                        district= response_Json[i]["data"]["district"],
                        location= response_Json[i]["data"]["location"],
                        resid_number= response_Json[i]["data"]["resid_number"]
                    )
                )            
        return self.__storage


    def update_employee(self, **employee_params) -> dict:         
                    
        employee = list(filter(lambda employee: employee[0] == employee_params["id_employee"], self.select_employee()))                
        index = self.__storage.index(employee[0])        
        employee_data = self.__get_employee(**employee_params)
            
        employee_data.pop(index)

        response = self.__push_employee_into_db(employee_data)
        return response        
        

    def delete_employee(self, identifier: str):        

        employee = list(filter(lambda employee: employee[0] == identifier, self.select_employee()))                  
        index = self.__storage.index(employee[0])        
        self.__storage.pop(index)        

        if self.__storage == []:
     
            response = self.__push_employee_into_db([])
            return response

        else:
            
            addasset = []
            for item in self.__storage:     

                employee_data = {
                    "data": {
                        "id_employee": item.id_employee,
                        "name": item.name,
                        "email": item.email,
                        "phone": item.phone,
                        "district": item.district,
                        "location": item.location,
                        "resid_number": item.resid_number
                    }                    
                }              
                addasset.append(employee_data)
            
            response = self.__push_employee_into_db(addasset)
            return response


    @HandlerContext
    def __get_employee(addasset: dict):
        return addasset            

    @HandlerContextTrigger
    def __push_employee_into_db(addasset: list):
        return addasset 


    def __verify_existent_employee(self, employee: list, data: dict) -> bool:
        repo = []
        for item in employee:
            for key in item.keys():
                repo.append(item[key]["email"])                

        if repo[0:-1].__contains__(data["email"]):  return True
        else: return False