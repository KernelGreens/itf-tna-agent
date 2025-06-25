from docxtpl import DocxTemplate
import os

def generate_report(insights: str):
    doc = DocxTemplate("templates/report_template.docx")
    context = {"findings": insights}  # this maps to {{ findings }} in your template
    output_path = "generated_reports/tna_report.docx"
    doc.render(context)
    doc.save(output_path)
    return output_path
