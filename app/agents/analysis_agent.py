from crewai import Agent, Task, Crew
import pandas as pd
from app.services.gdrive_service import fetch_sheet_data

def run_analysis(sheet_link):
    df_hr, df_sup, df_staff = fetch_sheet_data(sheet_link)

    prompt = f"""You are a expert Training Analyst. Analyze the training needs in the following data:
    HR Data: {df_hr.to_csv(index=False)}
    Supervisor Data: {df_sup.to_csv(index=False)}
    Staff Data: {df_staff.to_csv(index=False)}

    Extract Key skills or knowledge gaps, major training gaps, Common departmental issues, 
    frequency of common issues, areas with lowest scores,Trends across departments and recommended training actions.
    """

    analyst = Agent(name="Training Analyst", goal="Identify training gaps", backstory="You specialize in HR analytics.")
    task = Task(description=prompt, agent=analyst)
    crew = Crew(agents=[analyst], tasks=[task])
    results = crew.run()
    return results