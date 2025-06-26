from crewai import Agent, Task, Crew
from langchain.chat_models import ChatOpenAI
import pandas as pd
from app.services.gdrive_service import fetch_sheet_data
from dotenv import load_dotenv
load_dotenv()

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
                expected_output = """
                A comprehensive and well-structured Training Needs Assessment (TNA) report that includes the following key sections:

                1. Organizational Context
                - Identify the Vision and Mission of the Organisation.
                - Establish the existence of a Job Specification Document.
                - Establish Role Definition of Job Holder.
                - Identify the Performance Standard for Job Holder.

                2. Performance Analysis
                - Assess the Actual Performance of a Job Holder.
                - Determine existence of Job Holder Performance Gap.
                - Identify areas of Operations that require improvement in tabular form to follow the following column heading:
                S/N, AREA(S) REQUIRING IMPROVEMENT, WHY IS IMPROVEMENT NEEDED, HOW TO IMPROVE (INSTRUCTIONAL / NON - INSTRUCTIONAL)

                - Identify Priority Areas of Training in tabular format under the following column header: Order of Priority,
                Priority Areas of Training
 
                - Establish the regularity of Training in the Organisation in tabular format under the following column header: 
                S/N, Year, Number of Staff Trained, Percentage. Also represent in pie chart with primary colors.


                3. Key Skills or Knowledge Gaps
                - A list of missing or weak competencies per group (HR, Supervisors, Staff).

                4. Major Training Gaps
                - Specific areas where training is most urgently needed across job functions.

                5. Common Departmental Issues
                - Recurring problems or complaints across departments.

                6. Frequency of Common Issues
                - A count or summary showing how often each issue appears across data sources.

                7. Areas with Lowest Scores
                - The lowest scoring training/knowledge areas, per department or role group.

                8. Trends Across Departments
                - Patterns or recurring themes observed in the data.

                9. Safety Challenges
                - Identify specific safety-related gaps or concerns within job roles or departments.

                10. Recommended Training Actions
                    - Concrete, actionable training programs or strategies to address the identified issues.

                11. Performance Improvement Strategies
                    - Recommend appropriate strategies for improving individual and organizational performance.

                The report must be clearly structured into numbered sections with descriptive headers. Each section should be data-driven, where applicable, and should provide insights and recommendations in a concise and professional manner.
                """

                )
    crew = Crew(agents=[analyst], tasks=[task], llm=llm)
    results = crew.kickoff()
    return results