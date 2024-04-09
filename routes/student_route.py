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


