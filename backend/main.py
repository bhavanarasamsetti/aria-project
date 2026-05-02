from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.analyzer import generate_report, read_file

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🔥 Serve frontend folder
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
FRONTEND_DIR = os.path.join(BASE_DIR, "frontend")

app.mount("/static", StaticFiles(directory=FRONTEND_DIR), name="static")


# 🔥 Serve index.html
@app.get("/")
def home():
    return FileResponse(os.path.join(FRONTEND_DIR, "index.html"))

@app.get("/dashboard")
def dashboard():
    return FileResponse(os.path.join(FRONTEND_DIR, "dashboard.html"))
# API
@app.get("/get-data")
def get_data():
    file_path = os.path.join(BASE_DIR, "data", "ev_battery_issue.txt")

    log_data = read_file(file_path)
    report = generate_report(log_data)

    return {
        "vehicles": report["impact"]["vehicles"],
        "severity": report["impact"]["severity"],
        "summary": report["summary"],
        "root_cause": report["root_cause"],
        "fix": report["fix"],
        "tests": report["tests"],
        "alert": report["alert"],
        "drop": "38%",
        "temp": "46°C"
    }