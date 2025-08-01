import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

def authorize_sheets(json_keyfile):
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name(json_keyfile, scope)
    client = gspread.authorize(creds)
    return client

def log_to_sheet(client, sheet_name, worksheet_title, df):
    sheet = client.open(sheet_name)
    try:
        worksheet = sheet.worksheet(worksheet_title)
        sheet.del_worksheet(worksheet)
    except:
        pass
    worksheet = sheet.add_worksheet(title=worksheet_title, rows="1000", cols="20")
    worksheet.update([df.columns.values.tolist()] + df.values.tolist())
    print(f" Logged to sheet: {worksheet_title}")
