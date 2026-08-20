# 1. Import FastAPI and BaseModel

# 2. Create app instance

# 3. Define an Expense model with:
#    - amount   (float)
#    - category (str)
#    - description (str)

# 4. Create an empty list called expenses_db

# 5. Write POST /expenses
#    → accepts an Expense body
#    → appends it to expenses_db
#    → returns {"message": "Added!", "data": expense}

# 6. Write GET /expenses
#    → returns the full expenses_db list

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Expense(BaseModel):
    amount: float
    category: str
    description: str

expenses_db = []

@app.post("/expenses")
def add_expense(expense: Expense):
    expenses_db.append(expense.model_dump())
    return {"message": "Added!", "data": expense}
    
@app.get("/expenses")
def get_expenses():
    return expenses_db
