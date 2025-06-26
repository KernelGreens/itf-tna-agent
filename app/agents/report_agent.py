from docxtpl import DocxTemplate
import os

def generate_report(insights: str):

    # Ensure the output directory exists
    output_dir = "generated_reports"
    os.makedirs(output_dir, exist_ok=True)  # creates the folder if it doesn't exist

    # Prepare the template and context
    doc = DocxTemplate("templates/ITF_TNA_report_template.docx")
    #context = {"findings": insights}  # this maps to {{ findings }} in your template
    context = {
        "organizational_context": insights.get("Organizational Context", ""),
        "performance_analysis": insights.get("Performance Analysis", ""),
        "ksa_gaps": insights.get("Key Skills or Knowledge Gaps", ""),
        "training_gaps": insights.get("Major Training Gaps", ""),
        "Common_dept_issues": insights.get("Common Departmental Issues", ""),
        "freq_of_common_issues": insights.get("Frequency of Common Issues", ""),
        "lowest_scores_areas": insights.get("Areas with Lowest Scores", ""),
        "depts_trends": insights.get("Trends Across Departments", ""),
        "safety_challenges": insights.get("Safety Challenges", ""),
        "recommended_training_actions": insights.get("Recommended Training Actions", ""),
        "performance_improvement_strategies": insights.get("Performance Improvement Strategies", ""),
    }
    output_path = os.path.join(output_dir, "tna_report.docx")

    # Render and save the report
    doc.render(context)
    doc.save(output_path)
    return output_path
