from fastapi import FastAPI, Request, HTTPException
import os
import time

from pydantic import BaseModel

from solver.quiz_solver import solve_quiz_url

app = FastAPI()

SECRET = os.getenv("TDS_SECRET", "changeme")

class QuizRequest(BaseModel):
    email: str
    secret: str
    url: str

@app.post("/")
async def tds_endpoint(req: Request):
    try:
        data = await req.json()
    except:
        raise HTTPException(status_code=400, detail="Invalid JSON")

    try:
        payload = QuizRequest(**data)
    except:
        raise HTTPException(status_code=400, detail="Invalid fields")

    if payload.secret != SECRET:
        raise HTTPException(status_code=403, detail="Invalid secret")

    result = await solve_quiz_url(payload.email, payload.secret, payload.url)

    return {
        "status": "ok",
        "initial_url": payload.url,
        "result": result
    }
