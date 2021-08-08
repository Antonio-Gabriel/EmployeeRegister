import json
from typing import Union
from src.infrastructure import *
from src.helper.Exceptions import *
from functools import wraps

ROOT = db_context_config_root.get("app_root") 

class HandlerContext:

    def __init__(self, operator) -> None:
        wraps(operator)(self)
        self.__operator = operator

    
    def __call__(self, add_asset = [], **kwds) -> Union[list, dict]:
        
        try:                
            read_context = Storage.start_storage(file_route=f"{ROOT}/db/db.json")
            add_asset = json.load(read_context)        

            if kwds != {}:
                add_asset.append({
                    "data": kwds
                })
            
            response = self.__operator(add_asset)

        except EmployeeException as error:            
            return { "state": -1, "error": error }            
        else:            
            return response


class HandlerContextTrigger:
    
    def __init__(self, operator) -> None:
        wraps(operator)(self)
        self.__operator = operator

    
    def __call__(self, add_asset):

        context = Storage.start_storage(file_route=f"{ROOT}/db/db.json", permition="w+")    
        if context == None:
            json.dump([], context, indent=4)                
        else:
            json.dump(add_asset, context, indent=4)        

        return self.__operator(add_asset)
