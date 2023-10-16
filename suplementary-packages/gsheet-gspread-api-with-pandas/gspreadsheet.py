from __future__ import print_function
import gspread
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2 import service_account
import pandas as pd
import gspread


input_approved = {
            'create': ['1PpyCS3IPHqq2CZ_k3Y7dTs-H-Yty3IQjVTuuJraE2g4', 
                       '1iAehlIA1_fnYQET5rMw9r_XajNm26kXUD8I7gdnoUWU'], 
            'decommission': None, 
            'update': None
            }
        
input_draft = {
            'create': None, 
            'decommission': None, 
            'update': None
            }
input_approved_rows = {
    'create': [[{'Character Count': 345,
              'Current Spiel': '',
              'Message Name': 'AMAX_UTANG_P1ANS20',
              'New Spiel': 'Pwede mo nang magamit ang iyong hiniram na ANS20 '
                           'na may 300MB pang-internet at 150MB para sa '
                           'FunALIW apps. May unlimited calls at texts to all '
                           'networks pa, lahat valid for 2 days! Para sa promo '
                           'status, text UTANG ANS20 BAL to 3733. Pag may '
                           'budget ka na, bumili lang ng at least P21 load '
                           'para mabayaran at maka-avail muli ng Utang service '
                           'na ito.',
              'PROD MPID': 'update1',
              'Status': '',
              'TEST BED 1\nhttps://10.66.9.88:4432/LinkWorkbench/': 71273,
              'TEST BED 2\nhttps://10.237.196.74:4432/LinkWorkbench/': 35141,
              'index': 0},
             {'Character Count': 261,
              'Current Spiel': '',
              'Message Name': 'AMAX_UTANG_P1FB10',
              'New Spiel': 'Pwede mo nang magamit ang iyong hiniram na FB10 '
                           'with 600MB data pang-Facebook, valid for 3 days! '
                           'Para sa promo status, text UTANG FB10 BAL to 3733. '
                           'Pag may budget ka na, bumili lang ng at least P11 '
                           'load para mabayaran at maka-avail muli ng Utang '
                           'service na ito.',
              'PROD MPID': 'update1',
              'Status': '',
              'TEST BED 1\nhttps://10.66.9.88:4432/LinkWorkbench/': 71293,
              'TEST BED 2\nhttps://10.237.196.74:4432/LinkWorkbench/': 35161,
              'index': 1},
             {'Character Count': 267,
              'Current Spiel': '',
              'Message Name': 'AMAX_UTANG_P1TIKTOK10',
              'New Spiel': 'Pwede mo nang magamit ang iyong hiniram na '
                           'TIKTOK10 with 600MB data pang-TikTok, valid for 3 '
                           'days! Para sa promo status, text UTANG TIKTOK10 '
                           'BAL to 3733. Pag may budget ka na, bumili lang ng '
                           'at least P11 load para mabayaran at maka-avail '
                           'muli ng Utang service na ito.',
              'PROD MPID': 'update1',
              'Status': '',
              'TEST BED 1\nhttps://10.66.9.88:4432/LinkWorkbench/': 71294,
              'TEST BED 2\nhttps://10.237.196.74:4432/LinkWorkbench/': 35181,
              'index': 2},
             {'Character Count': 260,
              'Current Spiel': '',
              'Message Name': 'AMAX_UTANG_P1YT10',
              'New Spiel': 'Pwede mo nang magamit ang iyong hiniram na YT10 '
                           'with 600MB data pang-YouTube, valid for 3 days! '
                           'Para sa promo status, text UTANG YT10 BAL to 3733. '
                           'Pag may budget ka na, bumili lang ng at least P11 '
                           'load para mabayaran at maka-avail muli ng Utang '
                           'service na ito.',
              'PROD MPID': 'update1',
              'Status': '',
              'TEST BED 1\nhttps://10.66.9.88:4432/LinkWorkbench/': 71295,
              'TEST BED 2\nhttps://10.237.196.74:4432/LinkWorkbench/': 35201,
              'index': 3},
             {'Character Count': 267,
              'Current Spiel': '',
              'Message Name': 'AMAX_UTANG_P1ML10',
              'New Spiel': 'Pwede mo nang magamit ang iyong hiniram na ML10 '
                           'with 600MB data pang-Mobile Legends, valid for 3 '
                           'days! Para sa promo status, text UTANG ML10 BAL to '
                           '3733. Pag may budget ka na, bumili lang ng at '
                           'least P11 load para mabayaran at maka-avail muli '
                           'ng Utang service na ito.',
              'PROD MPID': 'update1',
              'Status': '',
              'TEST BED 1\nhttps://10.66.9.88:4432/LinkWorkbench/': 71296,
              'TEST BED 2\nhttps://10.237.196.74:4432/LinkWorkbench/': 35202,
              'index': 4},
             {'Character Count': 345,
              'Current Spiel': 'Pwede mo nang magamit ang iyong hiniram na '
                               'UTANG ANS20 na may 300MB pang-internet at '
                               '150MB para sa FunALIW apps. May unlimited '
                               'calls at texts to all networks pa, all valid '
                               'for 2 days! Para sa promo status, text UTANG '
                               'ANS20 BAL to 3733. Pag may budget ka na, '
                               'bumili lang ng at least P24 load para '
                               'mabayaran at maka-avail muli ng Utang service '
                               'na ito.',
              'Message Name': 'AMAX_UTANG_ANS20',
              'New Spiel': 'Pwede mo nang magamit ang iyong hiniram na ANS20 '
                           'na may 300MB pang-internet at 150MB para sa '
                           'FunALIW apps. May unlimited calls at texts to all '
                           'networks pa, lahat valid for 2 days! Para sa promo '
                           'status, text UTANG ANS20 BAL to 3733. Pag may '
                           'budget ka na, bumili lang ng at least P24 load '
                           'para mabayaran at maka-avail muli ng Utang service '
                           'na ito.',
              'PROD MPID': 'update1',
              'Status': '',
              'TEST BED 1\nhttps://10.66.9.88:4432/LinkWorkbench/': 71297,
              'TEST BED 2\nhttps://10.237.196.74:4432/LinkWorkbench/': 35221,
              'index': 5}],
            [{'Character Count': 345,
              'Current Spiel': '',
              'Message Name': 'AMAX_UTANG_P1ANS20',
              'New Spiel': 'Pwede mo nang magamit ang iyong hiniram na ANS20 '
                           'na may 300MB pang-internet at 150MB para sa '
                           'FunALIW apps. May unlimited calls at texts to all '
                           'networks pa, lahat valid for 2 days! Para sa promo '
                           'status, text UTANG ANS20 BAL to 3733. Pag may '
                           'budget ka na, bumili lang ng at least P21 load '
                           'para mabayaran at maka-avail muli ng Utang service '
                           'na ito.',
              'PROD MPID': 'update2',
              'Status': '',
              'TEST BED 1\nhttps://10.66.9.88:4432/LinkWorkbench/': 91273,
              'TEST BED 2\nhttps://10.237.196.74:4432/LinkWorkbench/': 95141,
              'index': 0},
             {'Character Count': 261,
              'Current Spiel': '',
              'Message Name': 'AMAX_UTANG_P1FB10',
              'New Spiel': 'Pwede mo nang magamit ang iyong hiniram na FB10 '
                           'with 600MB data pang-Facebook, valid for 3 days! '
                           'Para sa promo status, text UTANG FB10 BAL to 3733. '
                           'Pag may budget ka na, bumili lang ng at least P11 '
                           'load para mabayaran at maka-avail muli ng Utang '
                           'service na ito.',
              'PROD MPID': 'update2',
              'Status': '',
              'TEST BED 1\nhttps://10.66.9.88:4432/LinkWorkbench/': 91293,
              'TEST BED 2\nhttps://10.237.196.74:4432/LinkWorkbench/': 95161,
              'index': 1},
             {'Character Count': 267,
              'Current Spiel': '',
              'Message Name': 'AMAX_UTANG_P1TIKTOK10',
              'New Spiel': 'Pwede mo nang magamit ang iyong hiniram na '
                           'TIKTOK10 with 600MB data pang-TikTok, valid for 3 '
                           'days! Para sa promo status, text UTANG TIKTOK10 '
                           'BAL to 3733. Pag may budget ka na, bumili lang ng '
                           'at least P11 load para mabayaran at maka-avail '
                           'muli ng Utang service na ito.',
              'PROD MPID': 'update2',
              'Status': '',
              'TEST BED 1\nhttps://10.66.9.88:4432/LinkWorkbench/': 91294,
              'TEST BED 2\nhttps://10.237.196.74:4432/LinkWorkbench/': 95181,
              'index': 2},
             {'Character Count': 260,
              'Current Spiel': '',
              'Message Name': 'AMAX_UTANG_P1YT10',
              'New Spiel': 'Pwede mo nang magamit ang iyong hiniram na YT10 '
                           'with 600MB data pang-YouTube, valid for 3 days! '
                           'Para sa promo status, text UTANG YT10 BAL to 3733. '
                           'Pag may budget ka na, bumili lang ng at least P11 '
                           'load para mabayaran at maka-avail muli ng Utang '
                           'service na ito.',
              'PROD MPID': 'update2',
              'Status': '',
              'TEST BED 1\nhttps://10.66.9.88:4432/LinkWorkbench/': 91295,
              'TEST BED 2\nhttps://10.237.196.74:4432/LinkWorkbench/': 95201,
              'index': 3},
             {'Character Count': 267,
              'Current Spiel': '',
              'Message Name': 'AMAX_UTANG_P1ML10',
              'New Spiel': 'Pwede mo nang magamit ang iyong hiniram na ML10 '
                           'with 600MB data pang-Mobile Legends, valid for 3 '
                           'days! Para sa promo status, text UTANG ML10 BAL to '
                           '3733. Pag may budget ka na, bumili lang ng at '
                           'least P11 load para mabayaran at maka-avail muli '
                           'ng Utang service na ito.',
              'PROD MPID': 'update2',
              'Status': '',
              'TEST BED 1\nhttps://10.66.9.88:4432/LinkWorkbench/': 91296,
              'TEST BED 2\nhttps://10.237.196.74:4432/LinkWorkbench/': 35202,
              'index': 4},
             {'Character Count': 345,
              'Current Spiel': 'Pwede mo nang magamit ang iyong hiniram na '
                               'UTANG ANS20 na may 300MB pang-internet at '
                               '150MB para sa FunALIW apps. May unlimited '
                               'calls at texts to all networks pa, all valid '
                               'for 2 days! Para sa promo status, text UTANG '
                               'ANS20 BAL to 3733. Pag may budget ka na, '
                               'bumili lang ng at least P24 load para '
                               'mabayaran at maka-avail muli ng Utang service '
                               'na ito.',
              'Message Name': 'AMAX_UTANG_ANS20',
              'New Spiel': 'Pwede mo nang magamit ang iyong hiniram na ANS20 '
                           'na may 300MB pang-internet at 150MB para sa '
                           'FunALIW apps. May unlimited calls at texts to all '
                           'networks pa, lahat valid for 2 days! Para sa promo '
                           'status, text UTANG ANS20 BAL to 3733. Pag may '
                           'budget ka na, bumili lang ng at least P24 load '
                           'para mabayaran at maka-avail muli ng Utang service '
                           'na ito.',
              'PROD MPID': 'update2',
              'Status': '',
              'TEST BED 1\nhttps://10.66.9.88:4432/LinkWorkbench/': 91297,
              'TEST BED 2\nhttps://10.237.196.74:4432/LinkWorkbench/': 95221,
              'index': 5}]],
    'decommission': None,
    'update': None
    }
input_draft_rows = {'create': None, 'decommission': None, 'update': None}



GSHEET_SCOPE = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = 'reflected-wind-264114-4b2bba4b561a.json'
spread_ids = ['1PpyCS3IPHqq2CZ_k3Y7dTs-H-Yty3IQjVTuuJraE2g4', '1iAehlIA1_fnYQET5rMw9r_XajNm26kXUD8I7gdnoUWU']  # spreadsheet

creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=GSHEET_SCOPE)
service = gspread.authorize(creds)
# for f_id in spread_ids:
#     worksheet = service.open_by_key(f_id).worksheet('SPIEL')
#     list_of_dicts = worksheet.get_all_records()
#     df = pd.DataFrame(list_of_dicts)
#     print(df.shape)

for file_ids, rows in zip(input_approved.values(), input_approved_rows.values()):
    print("------------------")
    if file_ids is None:
        print(file_ids)
        print(rows)
        continue
    for file, row in zip(file_ids, rows):
        print(f"----- File {file} -------")
        df = pd.DataFrame(row)
        # print(list(df.columns))
        # print(df)
        worksheet = service.open_by_key(file).worksheet('SPIEL')
        data = worksheet.get_all_records()
        df2 = pd.DataFrame(data)
        # print(df2.columns)
        df.set_index('index', inplace=True)
        df = df[df2.columns]
        # print(df.columns)
        worksheet.update([df.columns.values.tolist()] + df.values.tolist())
    # print(len(file_ids))
    # print(len(rows))
    # worksheet.update([df.columns.values.tolist()] + df.values.tolist())

# for column in df.columns:
#             print(f"----- COLUMN {column} -------")
#             print(df[column])