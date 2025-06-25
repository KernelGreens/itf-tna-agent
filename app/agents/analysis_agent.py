from crewai import Agent, Task, Crew
from langchain.chat_models import ChatOpenAI
import pandas as pd
from app.services.gdrive_service import fetch_sheet_data

llm = ChatOpenAI(model="gpt-4", temperature=0.3)

def run_analysis(sheet_link):
    df_hr, df_sup, df_staff = fetch_sheet_data(sheet_link)

    prompt = f"""You are a expert Training Analyst. Analyze the training needs in the following data:
    HR Data: {df_hr.to_csv(index=False)}
    Supervisor Data: {df_sup.to_csv(index=False)}
    Staff Data: {df_staff.to_csv(index=False)}

    Extract Key skills or knowledge gaps, major training gaps, Common departmental issues, 
    frequency of common issues, areas with lowest scores,Trends across departments and recommended training actions.
    """

    analyst = Agent(name="Training Analyst", 
                    role="HR Analyst", 
                    goal="Identify training gaps", 
                    backstory="You specialize in HR analytics.")
    task = Task(description=prompt, 
                agent=analyst,
                expected_output="""
                A well-structured training needs report that includes the following:

                1. **Key Skills or Knowledge Gaps** - A list of missing or weak competencies per group (HR, Supervisors, Staff).
                2. **Major Training Gaps** - Specific areas where training is most urgently needed.
                3. **Common Departmental Issues** - Recurring problems or complaints across departments.
                4. **Frequency of Common Issues** - A count or summary showing how often each issue appears.
                5. **Areas with Lowest Scores** - The lowest scoring training/knowledge areas, per department.
                6. **Trends Across Departments** - Patterns or recurring themes seen in the data.
                7. **Recommended Training Actions** - Concrete, actionable training programs or strategies to address the issues.

                The report should be structured in numbered sections with clear headers.
                """
                )
    crew = Crew(agents=[analyst], tasks=[task], llm=llm)
    results = crew.kickoff()
    return results