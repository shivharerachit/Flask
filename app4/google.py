client_secret = "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"
# from google_auth_oauthlib.flow import InstalledAppFlow
# from google.auth.transport.requests import Request
# flow = InstalledAppFlow.from_client_secrets_file(
#     'client_secret.json', ['https://www.googleapis.com/auth/drive.metadata.readonly'])

# creds = flow.run_local_server(port=0)

# from googleapiclient.discovery import build
# service = build('drive', 'v3', credentials=creds)
json_file = {"web":{"client_id":"84420110064-qo2j067loorjmotsv46mv9knc5kg6101.apps.googleusercontent.com","project_id":"rachits-project","auth_uri":"https://accounts.google.com/o/oauth2/auth","token_uri":"https://oauth2.googleapis.com/token","auth_provider_x509_cert_url":"https://www.googleapis.com/oauth2/v1/certs","client_secret":"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"}}







from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
import json

# Load client secrets from file
with open('client_secret.json', 'r') as json_file:
    client_secret = json.load(json_file)

client_id = '84420110064-qo2j067loorjmotsv46mv9knc5kg6101.apps.googleusercontent.com'
# client_secret = json_file['web']['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']

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

# folder = '1y5UdK6rIgLPp8vTR22323LCcbDbBIozzcJ

# file1 = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : 'hello2.txt'})
# file1.SetContentString('Hello world!, this is my second file')
# file1.Upload()