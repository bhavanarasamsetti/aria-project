from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors

import sys
import os

# Fix import path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.analyzer import generate_report, read_file

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
FRONTEND_DIR = os.path.join(BASE_DIR, "frontend")

# Serve frontend
app.mount("/static", StaticFiles(directory=FRONTEND_DIR), name="static")

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
        "vehicles": 1250,
        "severity": report["impact"]["severity"],
        "summary": report["summary"],
        "root_cause": report["root_cause"],
        "fix": report["fix"],
        "tests": report["tests"],
        "alert": report["alert"],
        "drop": "38%",
        "temp": "46°C"
    }


# PDF EXPORT (CLEAN PROFESSIONAL REPORT)
@app.get("/download-report")
def download_report():
    file_path = os.path.join(BASE_DIR, "output", "ARIA_Full_Report.pdf")

    doc = SimpleDocTemplate(file_path, pagesize=A4)
    styles = getSampleStyleSheet()

    # Styles
    title_style = ParagraphStyle(
        name='Title',
        parent=styles['Heading1'],
        fontSize=18,
        spaceAfter=14,
        textColor=colors.black
    )

    heading_style = ParagraphStyle(
        name='Heading',
        parent=styles['Heading2'],
        fontSize=13,
        spaceAfter=6,
        textColor=colors.black
    )

    body_style = ParagraphStyle(
        name='Body',
        parent=styles['Normal'],
        fontSize=11,
        leading=16,
        spaceAfter=10
    )

    story = []

    # ===== ARIA INCIDENT REPORT =====
    story.append(Paragraph("ARIA INCIDENT REPORT - Voltix EV Battery Anomaly", title_style))
    story.append(Spacer(1, 12))

    story.append(Paragraph("Issue Summary", heading_style))
    story.append(Paragraph(
        "Critical battery management system failure detected across Voltix EV fleet following firmware v2.2.0 deployment. Within 2 minutes, vehicles experienced sudden battery drops, temperature spikes, and charging degradation. Rapid propagation to 1,250 vehicles indicates a firmware-induced systemic failure.",
        body_style))

    story.append(Paragraph("Root Cause", heading_style))
    story.append(Paragraph(
        "Firmware v2.2.0 introduced incompatible battery calibration logic for BMS-04. This caused incorrect SOC calculation, thermal mismanagement (46°C spike), and charging inefficiency due to mismatch between firmware and hardware calibration.",
        body_style))

    story.append(Paragraph("Impact", heading_style))
    story.append(Paragraph(
        "• 1,250 vehicles immediately affected<br/>"
        "• 12,000 vehicles at risk<br/>"
        "• Severity: CRITICAL<br/>"
        "• Safety Risk: Elevated temperature nearing thermal threshold<br/>"
        "• Customer Impact: Range issues, degraded charging, possible vehicle stranding",
        body_style))

    story.append(Paragraph("Suggested Fix", heading_style))
    story.append(Paragraph(
        "Immediate OTA rollback to v2.1.x, halt v2.2.0 rollout, deploy hotfix v2.2.1 with corrected calibration, and implement staged rollout with monitoring.",
        body_style))

    story.append(Paragraph("Alert", heading_style))
    story.append(Paragraph(
        "CRITICAL BATTERY SYSTEM FAILURE — Immediate engineering response required. Rollback protocol initiated.",
        body_style))

    story.append(Spacer(1, 16))

    # ===== FIX & TEST REPORT =====
    story.append(Paragraph("FIX & TEST ANALYSIS REPORT", title_style))

    story.append(Paragraph("Identified Root Issues", heading_style))
    story.append(Paragraph(
        "• BMS calibration mismatch<br/>"
        "• Lack of pre-deployment validation<br/>"
        "• No canary deployment strategy<br/>"
        "• Delayed anomaly detection<br/>"
        "• Thermal response latency (~3.2s)",
        body_style))

    story.append(Paragraph("Fix Strategy", heading_style))
    story.append(Paragraph(
        "• Real-time telemetry monitoring (30s intervals)<br/>"
        "• ML-based anomaly detection<br/>"
        "• BMS validation system<br/>"
        "• Canary deployment (10 → 100 → 1000 → full)<br/>"
        "• Automated rollback triggers",
        body_style))

    story.append(Paragraph("Test Plan", heading_style))
    story.append(Paragraph(
        "• 25 total test cases<br/>"
        "• Monitoring validation (≤2 min detection)<br/>"
        "• BMS compatibility tests<br/>"
        "• Thermal response validation<br/>"
        "• Rollback execution tests<br/>"
        "• End-to-end failure simulation",
        body_style))

    story.append(Paragraph("Outcome", heading_style))
    story.append(Paragraph(
        "• Detection ≤2 minutes<br/>"
        "• Rollback ≤5 minutes<br/>"
        "• Fleet safety ensured<br/>"
        "• System ready for deployment",
        body_style))

    doc.build(story)

    return FileResponse(file_path, filename="ARIA_Full_Report.pdf")

@app.post("/analyze-custom")
async def analyze_custom(data: dict):
    """Analyze custom log data from text input"""
    try:
        log_data = data.get("logs", "")
        if not log_data:
            return {"error": "No log data provided"}
        
        report = generate_report(log_data)
        
        return {
            "vehicles": report["impact"]["vehicles"],
            "severity": report["impact"]["severity"],
            "summary": report["summary"],
            "root_cause": report["root_cause"],
            "fix": report["fix"],
            "tests": report["tests"],
            "alert": report["alert"]
        }
    except Exception as e:
        return {"error": str(e)}

