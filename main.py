import gspread

# pyqt5
# mathplotlib
from datetime import date
from google.oauth2.credentials import Credentials

today = str(date.today())
scopes = ["https://www.googleapis.com/auth/spreadsheets"]
creds = Credentials.from_authorized_user_file("token.json", scopes=scopes)
client = gspread.authorize(creds)

sheet_id = "1zJMqB5eIj0NJ62VrNjPFaxHcdmSXa3Z04cRiF9Qrtcw"
workbook = client.open_by_key(sheet_id)
"""
t = int(input("Enter t value: "))
st = int(input("Enter sigma t value: "))
n = int(input("Enter n value: "))
sn = int(input("Enter sigma n value: "))
f = int(input("Enter f value: "))
q = int(input("Enter q value: "))

ev = 100 * (((t * n) / (st * sn)) + (f * q * q))
"""
sheet = workbook.worksheet("Chulada Graphing Data")
"""
sheet.update_cell(2, 1, today)
sheet.update_cell(2, 2, t)
sheet.update_cell(2, 3, st)
sheet.update_cell(2, 4, n)
sheet.update_cell(2, 5, sn)
sheet.update_cell(2, 6, f)
sheet.update_cell(2, 7, q)
sheet.update_cell(2, 8, ev)
"""
value = sheet.cell(1, 2).value
print(value)

# https://docs.google.com/spreadsheets/d/1zJMqB5eIj0NJ62VrNjPFaxHcdmSXa3Z04cRiF9Qrtcw/edit?gid=0#gid=0
