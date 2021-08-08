# Employee Register

![Badge](https://img.shields.io/badge/65%-PERCENTAGE-%237159c1?style=for-the-badge&logo=ghost)

`Open source`
A project developed with the aim of practicing the **knowledge** already retained during the study of the **python language**, working with a local storage configured by me and with a very readable architecture



```python

class Storage:
    def start_storage(file_route: str, permition: str = "r"):
        dbContext =  open(file_route, permition) 
        return dbContext

```

Configuration used for the application context, has a json file as a database simulation

```json
[
    {
        "data": {
            "id_employee": "30b29900-f7b7-11eb-bef0-81026a322abb",
            "name": "Dercio Sinione",
            "email": "derciosinione@gmail.com",
            "phone": 993487235,
            "district": "Zamba4",
            "location": "Hoji-ya-henda",
            "resid_number": 223
        }
    },
    {
        "data": {
            "id_employee": "6f27a854-f7cd-11eb-bef0-81026a322abb",
            "name": "Ant\u00f3nio Campos Gabriel",
            "email": "antoniocampos@gmail.com",
            "phone": 993487235,
            "district": "Zamba4",
            "location": "Hoji-ya-henda",
            "resid_number": 223
        }
    }
]
```

Complete application folder structure

```shell

📦src
 ┣ 📂helper
 ┃ ┣ 📂Exceptions
 ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┣ 📜EmployeeException.cpython-38.pyc
 ┃ ┃ ┃ ┗ 📜__init__.cpython-38.pyc
 ┃ ┃ ┣ 📜ControllerException.py
 ┃ ┃ ┣ 📜EmployeeException.py
 ┃ ┃ ┗ 📜__init__.py
 ┃ ┣ 📂decorators
 ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┣ 📜HandlerContext.cpython-38.pyc
 ┃ ┃ ┃ ┗ 📜__init__.cpython-38.pyc
 ┃ ┃ ┣ 📜Handler.py
 ┃ ┃ ┣ 📜HandlerContext.py
 ┃ ┃ ┗ 📜__init__.py
 ┃ ┗ 📂functions
 ┣ 📂infrastructure
 ┃ ┣ 📂__pycache__
 ┃ ┃ ┗ 📜__init__.cpython-38.pyc
 ┃ ┣ 📂config
 ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┣ 📜DbContext.cpython-38.pyc
 ┃ ┃ ┃ ┣ 📜StorageConfig.cpython-38.pyc
 ┃ ┃ ┃ ┗ 📜__init__.cpython-38.pyc
 ┃ ┃ ┣ 📂db
 ┃ ┃ ┃ ┗ 📜db.json
 ┃ ┃ ┣ 📜DbContext.py
 ┃ ┃ ┣ 📜StorageConfig.py
 ┃ ┃ ┗ 📜__init__.py
 ┃ ┗ 📜__init__.py
 ┣ 📂interface
 ┃ ┣ 📂__pycache__
 ┃ ┃ ┣ 📜IEmployee.cpython-38.pyc
 ┃ ┃ ┣ 📜IResidence.cpython-38.pyc
 ┃ ┃ ┗ 📜__init__.cpython-38.pyc
 ┃ ┣ 📜IEmployee.py
 ┃ ┣ 📜IResidence.py
 ┃ ┗ 📜__init__.py
 ┣ 📂repository
 ┃ ┣ 📂__pycache__
 ┃ ┃ ┣ 📜EmployeeRepository.cpython-38.pyc
 ┃ ┃ ┣ 📜ResidenceRepository.cpython-38.pyc
 ┃ ┃ ┗ 📜__init__.cpython-38.pyc
 ┃ ┣ 📜EmployeeRepository.py
 ┃ ┣ 📜ResidenceRepository.py
 ┃ ┗ 📜__init__.py
 ┗ 📂usecase
 ┃ ┣ 📂__pycache__
 ┃ ┃ ┣ 📜Employe.cpython-38.pyc
 ┃ ┃ ┣ 📜Residence.cpython-38.pyc
 ┃ ┃ ┗ 📜__init__.cpython-38.pyc
 ┃ ┣ 📜Employe.py
 ┃ ┣ 📜Residence.py
 ┃ ┗ 📜__init__.py

```

The same application performs a crud but everything locally, we will be able to do everything from inserting to removing data in the local file, as if we were working with a relational database

**Example of operations**

```python
print(employee.create())
print(employee.select())
print(employee.delete("ecf0ad9a-f7c2-11eb-bef0-81026a322abb"))
employee.update("30b29900-f7b7-11eb-bef0-81026a322abb")
print(employee.count())
```

The application fields are initially :*

Field name   | Data type
----------   | ---------
id_employee  | `string`
name         | `string`
email        | `string`
phone        | `integer`
district     | `string`
location     | `string`
resid_number | `string`


The more complex functions were replaced by decorators in order to avoid redundancy in the entire code

**example**

```python
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

```

Decorator implementation within a function

```python
@HandlerContext
def __get_employee(addasset: dict):
    return addasset 

# using in a context

def create_employee(self, **employee_params) -> dict:
         
    employee_data = self.__get_employee(**employee_params)        

    if self.__verify_existent_employee(employee_data, employee_params):
        return { "state": 0, "message": "Usuario Existente1" }        

    response = self.__push_employee_into_db(employee_data)

    if response is not None:
        return { "state": 1, "message": "sucess" }
```



**Future ideas that can be implemented**

Incorporate a `csv`, `exel` file to serve as an optional database, for this I count on your contribution


### Features

- [x] Employee registration
- [ ] Residence registration


### MIT License

Copyright (c) 2021 **António Campos Gabriel**