# app/utils/helpers.py

import pandas as pd

def format_df_summary(df: pd.DataFrame, role: str) -> str:
    """
    Create a readable summary from a DataFrame for a specific respondent group.
    """
    summary_lines = [f"Training needs summary for {role} group:"]
    
    for index, row in df.iterrows():
        line = f"- {row['Skill']} — Gap Level: {row['Gap Level']}"
        summary_lines.append(line)

    return "\n".join(summary_lines)

def combine_summaries(hr: str, sup: str, staff: str) -> str:
    """
    Merge the summaries of all roles into one report insight section.
    """
    return f"{hr}\n\n{sup}\n\n{staff}"
