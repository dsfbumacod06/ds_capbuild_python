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
import pandas as pd
import gspread

def main():
    GSHEET_SCOPE = ['https://www.googleapis.com/auth/spreadsheets']
    SERVICE_ACCOUNT_FILE = 'reflected-wind-264114-4b2bba4b561a.json'
    # spread_id = '1vVl2H_wPMU8wet5KDzmliLvUJhaCiNH_'  # .xlsx -> microsoft excel format
    spread_id = '1PpyCS3IPHqq2CZ_k3Y7dTs-H-Yty3IQjVTuuJraE2g4'  # spreadsheet
    try:
        gsheet_credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE,
                                                                                   scopes=GSHEET_SCOPE)
        
        # pprint(df.to_dict('records'))
        
        service = build("sheets", "v4", credentials=gsheet_credentials)
        
        
        response = service.spreadsheets().values().get(spreadsheetId=spread_id,
                                                        majorDimension="ROWS",
                                                        range='SPIEL').execute()    
        # print(response.values()) 
        
        columns = response['values'][0]
        # if columns != ['TEST BED 1\nhttps://10.66.9.88:4432/LinkWorkbench/', 'TEST BED 2\nhttps://10.237.196.74:4432/LinkWorkbench/', 'PROD MPID', 'Message Name', 'Current Spiel', 'New Spiel', 'Status', 'Character Count']:
        #     raise Exception("Columns must be of values ['TEST BED 1\nhttps://10.66.9.88:4432/LinkWorkbench/', 'TEST BED 2\nhttps://10.237.196.74:4432/LinkWorkbench/', 'PROD MPID', 'Message Name', 'Current Spiel', 'New Spiel', 'Status', 'Character Count']")
        data = response['values'][1:]
        df = pd.DataFrame(data, columns=columns)
        df_validation = df.isin(["", None, 0])  # checks which cells are null
        if not all(df_validation['PROD MPID']):  # should be true
            return False
        if not all(df_validation['Status']):     # should be true
            return False
        if any(df_validation['New Spiel']):  # should be false
            return False
        if any(df_validation['Message Name']):  #should be false
            return False
        df.reset_index(inplace=True)
        return df.to_dict('records')
        # return True

        
        # # print(columns)
        # for column in columns:
        #     print(f"----- COLUMN {column} -------")
        #     print(df[column])
        
    except Exception as error:
        # TODO(developer) - Handle errors from drive API.
        print(f'An error occurred: {error}')


if __name__ == '__main__':
    pprint(main())