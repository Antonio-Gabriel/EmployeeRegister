#!python3

from src.usecase import *


__author__ = "António Campos Gabriel"


if __name__ == "__main__":

    employee = Employee(
        name = "António Campos Gabriel", 
        email = "antoniocampos@gmail.com", 
        phone = 993487235, 
        residence= Residence(
            location = "Hoji-ya-henda", 
            district = "Zamba4", 
            resid_num = 223
        )
    )

    # print(employee.create())
    # print(employee.select())
    # print(employee.delete("ecf0ad9a-f7c2-11eb-bef0-81026a322abb"))
    # employee.update("30b29900-f7b7-11eb-bef0-81026a322abb")
    # print(employee.count())
