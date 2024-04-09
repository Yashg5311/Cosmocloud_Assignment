from fastapi import FastAPI
from routes import student_route

app= FastAPI()

app.include_router(student_route.router)