# app/services/gdrive_service.py

import gspread
from google.oauth2.service_account import Credentials
import pandas as pd

SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
SERVICE_ACCOUNT_FILE = 'credentials.json'  # Your downloaded JSON key

def fetch_sheet_data(sheet_url: str):
    # Authenticate
    creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    gc = gspread.authorize(creds)

    # Open the spreadsheet by URL
    sh = gc.open_by_url(sheet_url)

    # Assume tabs are named "HR", "Supervisors", "Staff"
    df_hr = pd.DataFrame(sh.worksheet("ITF_TNA_HR").get_all_records())
    df_sup = pd.DataFrame(sh.worksheet("ITF_TNA_Supervisors").get_all_records())
    df_staff = pd.DataFrame(sh.worksheet("ITF_TNA_Operatives").get_all_records())

    return df_hr, df_sup, df_staff
