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

from openpyxl import load_workbook
from io import FileIO, BytesIO
import pandas as pd

from itertools import islice

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
    CLIENT_SECRET_FILE = "reflected-wind-264114-4b2bba4b561a.json"
    API_NAME = 'drive'
    API_VERSION = "v3"
    SCOPES = ['https://www.googleapis.com/auth/drive']
    TOKEN = 'token.json'



    try:
        gdrive_credentials = service_account.Credentials.from_service_account_file(filename=CLIENT_SECRET_FILE,
                                                                                   scopes=SCOPES)
        service = build(API_NAME, API_VERSION, credentials=gdrive_credentials)


        
        # folder_ids = [
        #     "1AdV1xwuvrhoPBjeWG2vebc5RG7jKRTzy"
        # ]
        # for folder in folder_ids:
        #     print(f'------ FOLDER CONTENTS -------')
        #     q = f"parents = '{folder}'"
        #     response = service.files().list(q=q).execute()
        #     pprint(response)
            
        file_id = "1vVl2H_wPMU8wet5KDzmliLvUJhaCiNH_"
        body = service.files().get_media(fileId=file_id).execute()
        content = BytesIO(body)
        wkb = load_workbook(content, data_only=True)
        wks = wkb['SPIEL']
        # print(list(wks.columns))
        
        data = wks.values
        cols = next(data)
        data = list(data)
        # data = (islice(r, 0, None) for r in data)
        df = pd.DataFrame(data, columns=cols)
        # df.dropna(axis=1, inplace=True, how='all')
        df.drop(columns=[col for col in df.columns if col is None or pd.isna(col)], inplace=True)
        df.dropna(axis=0, inplace=True, how='all')
        
        df[['TEST BED 1\nhttps://10.66.9.88:4432/LinkWorkbench/',
        'TEST BED 2\nhttps://10.237.196.74:4432/LinkWorkbench/', 
       'Character Count']] = df[['TEST BED 1\nhttps://10.66.9.88:4432/LinkWorkbench/',
        'TEST BED 2\nhttps://10.237.196.74:4432/LinkWorkbench/', 
       'Character Count']].astype(int)
       
    #     # print(df.columns)
    #     for column in df.columns:
    #         print(f"----- COLUMN {column} -------")
    #         print(df[column])
            
        # df_validation = df.isin(["", None, 0])  # checks which cells are null
        # print(all(df_validation['PROD MPID']))
        # print(all(df_validation['Status']))
        # print(any(df_validation['New Spiel']))
        # print(any(df_validation['Message Name']))
        df.reset_index(inplace=True)
        pprint(df.to_dict('records'))
    
    
    
        # if not all(df_validation['PROD MPID']):  # should be true
        #     return False
        # if not all(df_validation['Status']):     # should be true
        #     return False
        # if any(df_validation['New Spiel']):  # should be false
        #     return False
        # if any(df_validation['Message Name']):  #should be false
        #     return False
        # return True
        
        # df = pd.DataFrame(wks.get_all_records())
        # columns = df.columns
        # df_validation = df.isin(["", None, 0])
        # pprint(df.to_dict('records'))
        
        
        
        
        # print(len(response.get('files')))
        # print(nextPageToken)
        # print(dir(service))
# def read_text_content(self, file_id):
#     body = self.drive_api.files().get_media(fileId=file_id).execute()
#     content = BytesIO(body)
#     return content






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