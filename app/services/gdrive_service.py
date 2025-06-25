# app/services/gdrive_service.py

import pandas as pd

def fetch_sheet_data(sheet_url: str):
    """
    Simulate loading 3 tabs from a Google Sheet URL.
    Replace with actual Google Sheets API/gspread integration later.
    """

    # Simulated example — you’ll later load this from gspread
    df_hr = pd.DataFrame({
        "Skill": ["Communication", "Leadership", "Problem Solving"],
        "Gap Level": ["High", "Medium", "High"]
    })

    df_sup = pd.DataFrame({
        "Skill": ["Team Management", "Strategic Thinking"],
        "Gap Level": ["Low", "High"]
    })

    df_staff = pd.DataFrame({
        "Skill": ["Technical Skills", "Safety Compliance"],
        "Gap Level": ["Medium", "High"]
    })

    return df_hr, df_sup, df_staff
