from docxtpl import DocxTemplate
import os

def generate_report(insights: str):

    # Ensure the output directory exists
    output_dir = "generated_reports"
    os.makedirs(output_dir, exist_ok=True)  # creates the folder if it doesn't exist

    # Prepare the template and context
    doc = DocxTemplate("templates/ITF_TNA_report_template.docx")
    context = {"findings": insights}  # this maps to {{ findings }} in your template
    output_path = os.path.join(output_dir, "tna_report.docx")

    # Render and save the report
    doc.render(context)
    doc.save(output_path)
    return output_path
