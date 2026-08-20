from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Expense(BaseModel):
    amount: float
    category: str
    description: str

expenses_db = []

@app.post("/expenses")
def add_expense(expense: Expense):
    expense_data = expense.model_dump()
    expense_data["id"] = len(expenses_db) + 1
    expenses_db.append(expense_data)
    return {"message": "Added!", "data": expense_data}
    
@app.get("/expenses")
def get_expenses():
    return expenses_db

@app.get("/expenses/summary")
def get_summary():
    summary = {}
    for expense in expenses_db:
        category = expense["category"]
        summary[category] = summary.get(category, 0) + expense["amount"]
    
    return summary

@app.get("/expenses/{expense_id}")
def get_expense(expense_id: int):
    for expense in expenses_db:
        if expense['id'] == expense_id:
            return expense
    raise HTTPException(status_code=404, detail="Expense not found!")

@app.put("/expenses/{expense_id}")
def update_expense(expense_id: int, updated: Expense):
    for expense in expenses_db:
        if expense['id'] == expense_id:
            expense["amount"] = updated.amount
            expense["category"] = updated.category
            expense["description"] = updated.description
            return {"message": "Updated!", "data": expense}
        
    raise HTTPException(status_code=404, detail="Expense not found")

@app.delete("/expenses/{expense_id}")
def delete_expense(expense_id: int):
    for i, expense in enumerate(expenses_db):
        if expense['id'] == expense_id:
            expenses_db.pop(i)
            return {"message": "Deleted!"}
    raise HTTPException(status_code=404, detail="Expense not found")

        
