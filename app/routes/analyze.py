from fastapi import APIRouter
from app.agents.analysis_agent import run_analysis
from app.agents.report_agent import generate_report
from app.services.email_sender import send_email

router = APIRouter()

@router.post("/")
async def analyze_tna(data: dict):
    sheet_link = data.get("sheet_url")
    emails = data.get("recipients", [])
    
    insights = run_analysis(sheet_link)
    report_path = generate_report(insights)
    send_email(emails, report_path)

    return {"status": "completed", "report": report_path}
