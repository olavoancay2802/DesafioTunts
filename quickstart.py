from __future__ import print_function
import os.path
import math
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1iWkXgDSz1sM7bkhewXJdSMBVJrmrZj9QRFLla8NMeuY'
SAMPLE_RANGE_NAME = 'engenharia_de_software!A4:F'

TOTAL_DE_AULAS = 'engenharia_de_software!A2'

def main():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=SAMPLE_RANGE_NAME).execute()
    values = result.get('values', [])
    update =[]

    if not values:
        print('No data found.')
    else:
        print('Médias alunos')
        for row in values:
            auxUpdate =[]
            # sum the 3 student grades
            faltas,p1,p2,p3 = int(row[2]),int(row[3]),int(row[4]), int(row[5]) 
            media = (p1 + p2 + p3)/3
            media = math.ceil(media)
            
            if faltas % 60 > 25:
                situacao = 'Reprovado por Falta'
            elif media < 50:
                situacao = 'Reprovado por Nota'
            elif media < 70:
                situacao = 'Exame Final'
            else: 
                situacao = 'Aprovado'
                
            if situacao == 'Exame Final':
                naf = 100 - media
            else:
                naf = 0
                
            auxUpdate.append(situacao)
            auxUpdate.append(naf)
            update.append(auxUpdate)
                
            print('%s %s' % (row[0], row[4]),f'{faltas} {p1} {p2} {p3} {situacao} {naf}')
            
        for i in range (len(update)):    
            print(update[i])
        

if __name__ == '__main__':
    main()