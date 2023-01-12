from fastapi import FastAPI, HTTPException
import os
import json


EMPLOYEES_FILE = "employees.json"
EMPLOYEES = []

if os.path.exists(EMPLOYEES_FILE):
    with open(EMPLOYEES_FILE, "r") as emps:
        EMPLOYEES = json.load(emps)


testApp = FastAPI()


@testApp.get("/")
async def root():
    return {"message": "Hello, this is test app."}


@testApp.get("/getAllEmployees")
async def list_books():
    return {"employees": EMPLOYEES}


@testApp.get("/getEmployeeByID")
async def get_book(emp_id: str):
    for emp in EMPLOYEES:
        if emp["empId"] == emp_id:
            return emp

    raise HTTPException(404, f"Employee ID {emp_id} not found in database.")
