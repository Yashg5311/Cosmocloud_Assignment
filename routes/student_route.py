from fastapi import APIRouter, HTTPExceptions, Query
from db.connection import collection
from models.student_model import Student
import random
import string

router = APIRouter()

def generate_custom_id():
    # Generate a random 6-digit alphanumeric ID
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

@router.post("/students", status_code=201, response_model=dict)
async def create_student(student: Student):
    student_dict = student.dict()
    
    # Generate custom ID
    custom_id = generate_custom_id()
    
    # Check if custom ID already exists
    while collection.find_one({"id": custom_id}):
        custom_id = generate_custom_id()
    
    # Add custom ID to student dictionary
    student_dict["id"] = custom_id
    
    # Insert student into MongoDB collection
    result = collection.insert_one(student_dict)
    
    return {"id": custom_id}


@router.get("/students", response_model=dict)
async def list_students(country: str = Query(None, description="To apply filter of country."),
                        age: int = Query(None, description="Only records which have age greater than equal to the provided age should be present in the result.")):
    query = {}
    
    if country:
        query["address.country"] = country
    
    if age:
        query["age"] = {"$gte": age}
    
    projection = {"name": 1, "age": 1, "id": 1, "_id": 0}  # Include id in the result
    
    students = list(collection.find(query, projection))
    
    return {"data": students}

