from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class loanApplication(BaseModel):
    age:int
    income: float
    loan_amount: float

@app.post("/predict")
def predict_loan(application: loanApplication):
    if application.income>5000:
        decision = "approved"
    else:
        decision = "rejected"
    return{
        "application_age":application.age,
        "decision":decision

    }

@app.get("/customer/{customer_id}")
def get_customer(customer_id:int):
    return{
        "customer_id":customer_id
    }
