from datetime import datetime
from typing import List
from pydantic import BaseModel
from bson.objectid import ObjectId


class EmployeeBaseSchema(BaseModel):
    name: str
    email: str
    age: int
    company: str
    join_date: datetime
    job_title: str
    gender: str
    salary: int

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}


class CreateEmployeeSchema(EmployeeBaseSchema):
    pass


class EmployeeResponse(EmployeeBaseSchema):
    pass


class ListEmployeeResponse(BaseModel):
    status: str
    results: int
    employees: List[EmployeeResponse]
