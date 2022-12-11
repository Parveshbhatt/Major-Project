import gspread
def WriteToGs(fileName, data):
    print(data)
    #Authenticate Google service account
    gp = gspread.service_account(filename='script/google-auth.json')
    #Open Google spreadsheet
    gsheet = gp.open(fileName)
    wsheet = gsheet.worksheet("Sheet1")
    wsheet.append_row(data)