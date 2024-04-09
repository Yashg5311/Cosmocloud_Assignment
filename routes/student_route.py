from fastapi import APIRouter, HTTPExceptions, Query
from db.connection import collection
from models.student_model import Student
import random
import string

router = APIRouter()