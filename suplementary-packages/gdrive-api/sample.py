# from __future__ import print_function

# import os.path

# from google.auth.transport.requests import Request
# from google.oauth2.credentials import Credentials
# from google_auth_oauthlib.flow import InstalledAppFlow
# from googleapiclient.discovery import build
# from googleapiclient.errors import HttpError

# # If modifying these scopes, delete the file token.json.
# SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly']

# from Google import Create_Service
# CLIENT_SECRET_FILE = "gdrive-creds.json"
# API_NAME = 'drive'
# API_VERSION = "v3"
# SCOPES = ['https://www.googleapis.com/auth/drive']

# def main():
#     service = Create_Service(CLIENT_SECRET_FILE, API_VERSION, SCOPES)
#     print(dir(service))


# if __name__ == '__main__':
#     main()



from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2 import service_account
from pprint import pprint

# If modifying these scopes, delete the file token.json.
# SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly']


def main():
    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    CLIENT_SECRET_FILE = "gdrive-creds.json"
    API_NAME = 'drive'
    API_VERSION = "v3"
    SCOPES = ['https://www.googleapis.com/auth/drive', 'https://www.googleapis.com/auth/drive.file']
    TOKEN = 'token.json'
    # pickle_file = f'token_{API_SERVICE_NAME}_{API_VERSION}.pickle'
    
    # if os.path.exists(TOKEN):
    #     creds = Credentials.from_authorized_user_file(TOKEN, SCOPES)
    # # If there are no (valid) credentials available, let the user log in.
    # if not creds or not creds.valid:
    #     if creds and creds.expired and creds.refresh_token:
    #         creds.refresh(Request())
    #     else:
    #         flow = InstalledAppFlow.from_client_secrets_file(
    #             CLIENT_SECRET_FILE, SCOPES)
    #         creds = flow.run_local_server(port=0)
    #     # Save the credentials for the next run
    #     with open('token.json', 'w') as token:
    #         token.write(creds.to_json())


    try:
        gdrive_credentials = service_account.Credentials.from_service_account_file(filename="reflected-wind-264114-4b2bba4b561a.json",
                                                                                   scopes=SCOPES)
        service = build(API_NAME, API_VERSION, credentials=gdrive_credentials)
        # service = build(API_NAME, API_VERSION, credentials=creds)
        # folder_id = "13EoqrSzsud-FjHcJf1KDqj8SKWTw9oxf"  # mentor me folder
        # # folder_id = "15SY6_5T6U7z6KIcJUZlm-8CpY20KNe63" # empty mentor me folder
        # # folder_id = "16hWxGAm-knPwR6thKmvrxPGR_tJ6AkqM" # di folder
        # # folder_id = "157AlcrbRkTlUj4KFix7YloTe8UrYoXET"
        # q = f"parents = '{folder_id}'"
        # response = service.files().list(q=q).execute()
        # # nextPageToken = response.get('nextPageToken')
        # pprint(response)


        
        folder_ids = [
            "13EoqrSzsud-FjHcJf1KDqj8SKWTw9oxf",
            "15SY6_5T6U7z6KIcJUZlm-8CpY20KNe63"
        ]
        for folder in folder_ids:
            print(f'------ FOLDER CONTENTS -------')
            q = f"parents = '{folder}'"
            response = service.files().list(q=q).execute()
            pprint(response)
        # print(len(response.get('files')))
        # print(nextPageToken)
        # print(dir(service))






        # Call the Drive v3 API
        # results = service.files().list(
        #     pageSize=10, fields="nextPageToken, files(id, name)").execute()
        # items = results.get('files', [])

        # if not items:
        #     print('No files found.')
        #     return
        # print('Files:')
        # for item in items:
        #     print(u'{0} ({1})'.format(item['name'], item['id']))
    except HttpError as error:
        # TODO(developer) - Handle errors from drive API.
        print(f'An error occurred: {error}')


if __name__ == '__main__':
    main()