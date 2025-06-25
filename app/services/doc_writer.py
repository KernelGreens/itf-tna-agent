# app/services/doc_writer.py

from docxtpl import DocxTemplate
import os
from datetime import datetime

def generate_report_from_template(insights: str, output_dir="generated_reports") -> str:
    """Generates a report using a .docx template and AI-generated insights."""
    
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Load template
    template_path = os.path.join("templates", "report_template.docx")
    doc = DocxTemplate(template_path)

    # Prepare context for template placeholders
    context = {
        "date": datetime.now().strftime("%B %d, %Y"),
        "findings": insights
    }

    # Render and save
    filename = f"TNA_Report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.docx"
    output_path = os.path.join(output_dir, filename)
    doc.render(context)
    doc.save(output_path)

    return output_path
