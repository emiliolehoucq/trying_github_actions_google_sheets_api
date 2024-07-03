import os
import json
import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2.service_account import Credentials
from datetime import datetime

# Write the credentials from the environment variable to a file
with open('credentials.json', 'w') as creds_file:
    creds_file.write(os.getenv('GOOGLE_APPLICATION_CREDENTIALS'))

# Load credentials from the file
creds = Credentials.from_service_account_file('credentials.json')
service = build("sheets", "v4", credentials=creds)
result = service.spreadsheets().values().get(spreadsheetId="176xIIin9KdZzD4ZZVKdMEj3V3uUUoDHHKg6z7zXjnqo", range="A1:A10").execute()
rows = result.get("values", [])

# Create the .txt file with the current datetime in 'data' folder
file_path = f"data/rows_{current_datetime}.txt"
with open(file_path, 'w') as file:
    for row in rows:
        file.write(f"{row}\n")
