class Settings():
    
    def __init__(self, settings_json):
        self.spreadsheetId = settings_json['SPREADSHEET_ID']
        self.spreadsheetData = settings_json['SPREADSHEET_DATA']
        self.totalClassesRange = settings_json['TOTAL_CLASSES_RANGE']
        self.updateFrom = settings_json['UPDATE_FROM']
            
 