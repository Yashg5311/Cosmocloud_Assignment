from pydantic import BaseModel

class Address(BaseModel):
    city:str
    country:str

class Student(BaseModel):
    name:str
    age:int
    address:Address

    class Config:
        schema_extra={
            "example":{
                "name":"John Doe",
                "age":20,
                "address":{
                    "city":"New York",
                    "Country":"USA"
                },
                "id":"abc123"
            }
        }