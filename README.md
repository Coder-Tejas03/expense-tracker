# 💸 Expense Tracker API

A RESTful API built with **FastAPI** and **Pydantic** — full CRUD for personal expense tracking.

## Stack
- Python 3.x
- FastAPI
- Pydantic
- Uvicorn

## Run Locally

```bash
pip install fastapi uvicorn
uvicorn expense_tracker:app --reload
```

API runs at `http://127.0.0.1:8000`  
Interactive docs at `http://127.0.0.1:8000/docs`

## Endpoints

| Method | Route | Description |
|--------|-------|-------------|
| POST | `/expenses` | Add a new expense |
| GET | `/expenses` | Get all expenses |
| GET | `/expenses/summary` | Total spent per category |
| GET | `/expenses/{id}` | Get one expense by ID |
| PUT | `/expenses/{id}` | Update an expense |
| DELETE | `/expenses/{id}` | Delete an expense |

## Request Body (POST / PUT)

```json
{
  "amount": 450.0,
  "category": "food",
  "description": "Lunch at Subway"
}
```

## Example Responses

**POST /expenses**
```json
{"message": "Added!", "data": {"amount": 450.0, "category": "food", "description": "Lunch at Subway", "id": 1}}
```

**GET /expenses/summary**
```json
{"food": 800.0, "transport": 200.0}
```

**GET /expenses/99** (not found)
```json
{"detail": "Expense not found!"}
```
