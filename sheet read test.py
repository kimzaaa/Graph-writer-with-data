# google sheet
import gspread

# pyqt
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

# mathplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

from datetime import date
from google.oauth2.credentials import Credentials

today = str(date.today())
scopes = ["https://www.googleapis.com/auth/spreadsheets"]
creds = Credentials.from_authorized_user_file("token.json", scopes=scopes)
client = gspread.authorize(creds)

sheet_id = "1zJMqB5eIj0NJ62VrNjPFaxHcdmSXa3Z04cRiF9Qrtcw"
workbook = client.open_by_key(sheet_id)

sheet = workbook.worksheet("Chulada Graphing Data")

values_list = sheet.col_values(1)[1:][::-1]
print(values_list)