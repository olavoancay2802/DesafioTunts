import os.path
import math
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials


SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

#ID sample spreadsheet.
SPREADSHEET_ID = '1iWkXgDSz1sM7bkhewXJdSMBVJrmrZj9QRFLla8NMeuY'
#Infos Range
SPREADSHEET_INFOS = 'engenharia_de_software!A4:F'
#Semester classes range
TOTAL_CLASSES = 'engenharia_de_software!A2'

def main():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                                range=SPREADSHEET_INFOS).execute()
    values = result.get('values', [])
    
    totalClasses = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                                range=TOTAL_CLASSES).execute()
    valuesTotalClasses = totalClasses.get('values')
    
    update =[]
    
    txt = valuesTotalClasses[0][0]
    
    numbers = ""

    for letter in txt:
        if letter.isdigit():
            numbers += str(letter)
          
    numberSemesterClasses = int(numbers)

    if not values:
        print('No data found.')
    else:
        for row in values:
            auxUpdate =[]
            absences,p1,p2,p3 = int(row[2]),int(row[3]),int(row[4]), int(row[5])
            media = (p1 + p2 + p3)/3         
            media = math.ceil(media)
            
            if absences / numberSemesterClasses > 0.25:
                condition = 'Reprovado por Falta'
            elif media < 50:
                condition = 'Reprovado por Nota'
            elif media < 70:
                condition = 'Exame Final'
            else: 
                condition = 'Aprovado'
                
            if condition == 'Exame Final':
                finalScoreNeeded = 100 - media
            else:
                finalScoreNeeded = 0
                
            auxUpdate.append(condition)
            auxUpdate.append(finalScoreNeeded)
            update.append(auxUpdate)
        
        request = sheet.values().update(spreadsheetId=SPREADSHEET_ID,
                                                             range='engenharia_de_software!G4', valueInputOption='RAW', body={'values':update}).execute()

if __name__ == '__main__':
    main()
