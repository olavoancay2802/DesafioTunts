import os.path
import math
import json
from Settings import Settings
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials


SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

def get_settings():
    with open('sheet_settings.json') as settingsFile:
        settingsLoad = json.load(settingsFile)

    settings = Settings(settingsLoad)
    
    return settings
    
def get_credentials():
    creds = None
    
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
       
    return creds
    
def get_amount_of_classes_per_semester(sheet, settings):
    textContainingAmountOfClasses = sheet.values().get(spreadsheetId=settings.spreadsheetId,
                                range=settings.totalClassesRange).execute().get('values')
    
    txt = textContainingAmountOfClasses[0][0]
    
    onlyDigits = ""

    for letter in txt:                     #Iterating string to get only amount of classes
        if letter.isdigit():
            onlyDigits += str(letter)
          
    amtOfClassesPerSemester = int(onlyDigits)
                                
    return amtOfClassesPerSemester
    
def define_student_status_based_on_grades_and_absences(sheetData, amtOfClassesPerSemester):
    updatePayload = []
    
    for row in sheetData:
        rowUpdate =[]                        
        absences,p1,p2,p3 = int(row[2]),int(row[3]),int(row[4]),int(row[5])
        average = (p1 + p2 + p3)/3         
        average = math.ceil(average)
            
        if absences / amtOfClassesPerSemester > 0.25:
            status = 'Reprovado por Falta'
        elif average < 50:
            status = 'Reprovado por Nota'
        elif average < 70:
            status = 'Exame Final'
        else: 
            status = 'Aprovado'
                
        if status == 'Exame Final':
            finalScoreNeeded = 100 - average
        else:
            finalScoreNeeded = 0
                
            rowUpdate.append(status)
            rowUpdate.append(finalScoreNeeded)
            updatePayload.append(rowUpdate)
    
    return updatePayload

def main():
    settings = get_settings()
    
    creds = get_credentials()

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    
    amtOfClassesPerSemester = get_amount_of_classes_per_semester(sheet, settings)
    
    result = sheet.values().get(spreadsheetId=settings.spreadsheetId,
                                range=settings.spreadsheetData).execute()
    sheetData = result.get('values', [])
    
    if not sheetData:
        print('No data found.')
    else:
        updatePayload = define_student_status_based_on_grades_and_absences(sheetData,amtOfClassesPerSemester)
        
        request = sheet.values().update(spreadsheetId=settings.spreadsheetId,
                                                             range=settings.updateFrom, valueInputOption='RAW', body={'values':updatePayload}).execute()

if __name__ == '__main__':
    main()
