#!python3

class Storage:
    
    def start_storage(file_route: str, permition: str = "r"):
        dbContext =  open(file_route, permition) 
        return dbContext

