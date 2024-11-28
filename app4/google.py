from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()

client_id = os.getenv('CLIENT_ID'),
project_id = os.getenv('PROJECT_ID'),
auth_uri = os.getenv('AUTH_URI'),
token_uri = os.getenv('TOKEN_URI'),
auth_provider = os.getenv('AUTH_PROVIDER'),
client_secret = os.getenv('CLIENT_SECRET')
# from google_auth_oauthlib.flow import InstalledAppFlow
# from google.auth.transport.requests import Request
# flow = InstalledAppFlow.from_client_secrets_file(
#     'client_secret.json', ['https://www.googleapis.com/auth/drive.metadata.readonly'])

# creds = flow.run_local_server(port=0)

# from googleapiclient.discovery import build
# service = build('drive', 'v3', credentials=creds)
json_file = {
    "web":{
        "client_id": client_id,
        "project_id": project_id,
        "auth_uri": auth_uri,
        "token_uri": token_uri,
        "auth_provider_x509_cert_url": auth_provider,
        "client_secret": client_secret
        }
    }







from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
import json

# Load client secrets from file
with open('client_secret.json', 'r') as json_file:
    client_secret = json.load(json_file)


# Initialize flow using client secrets
flow = InstalledAppFlow.from_client_secrets_file(
    'client_secret.json', scopes=['https://www.googleapis.com/auth/drive.metadata.readonly'])

# Authenticate and authorize the user
creds = flow.run_local_server(port=0)

# Build service using authenticated credentials
service = build('drive', 'v3', credentials=creds)

# # Now you can use the service to make requests to Google Drive API

# from pydrive.auth import GoogleAuth
# from pydrive.drive import GoogleDrive

# gauth = GoogleAuth()
# drive = GoogleDrive(gauth)

# file1 = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : 'hello2.txt'})
# file1.SetContentString('Hello world!, this is my second file')
# file1.Upload()