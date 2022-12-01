import gspread
def read_csv():
    #Authenticate Google service account
    gp = gspread.service_account(filename='script/google-auth.json')
    #Open Google spreadsheet
    gsheet = gp.open('rpi-temp')
    wsheet = gsheet.worksheet("Sheet1")
    return wsheet.get_all_values()
