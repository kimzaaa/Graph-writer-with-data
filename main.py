# google sheet
import gspread

# pyqt
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

# mathplotlib
from datetime import date
from google.oauth2.credentials import Credentials

today = str(date.today())
scopes = ["https://www.googleapis.com/auth/spreadsheets"]
creds = Credentials.from_authorized_user_file("token.json", scopes=scopes)
client = gspread.authorize(creds)

sheet_id = "1zJMqB5eIj0NJ62VrNjPFaxHcdmSXa3Z04cRiF9Qrtcw"
workbook = client.open_by_key(sheet_id)

sheet = workbook.worksheet("Chulada Graphing Data")
# value = sheet.cell(1, 2).value
# print(value)


class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = "Graph writer with data"
        self.left = 10
        self.top = 70
        self.width = 1600
        self.height = 900
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Create all 6 textbox
        self.tlable = QLabel(self)
        self.tlable.setText("Enter T Value")
        self.tlable.move(20, 15)
        self.t = QLineEdit(self)
        self.t.move(20, 40)
        self.t.resize(200, 30)

        self.stlable = QLabel(self)
        self.stlable.setText("Enter ΣT Value")
        self.stlable.move(260, 15)
        self.st = QLineEdit(self)
        self.st.move(260, 40)
        self.st.resize(200, 30)

        self.nlable = QLabel(self)
        self.nlable.setText("Enter N Value")
        self.nlable.move(20, 95)
        self.n = QLineEdit(self)
        self.n.move(20, 120)
        self.n.resize(200, 30)

        self.snlable = QLabel(self)
        self.snlable.setText("Enter Σñ Value")
        self.snlable.move(260, 95)
        self.sn = QLineEdit(self)
        self.sn.move(260, 120)
        self.sn.resize(200, 30)

        self.flable = QLabel(self)
        self.flable.setText("Enter ƒ Value")
        self.flable.move(20, 175)
        self.f = QLineEdit(self)
        self.f.move(20, 200)
        self.f.resize(200, 30)

        self.qlable = QLabel(self)
        self.qlable.setText("Enter Q Value")
        self.qlable.move(260, 175)
        self.q = QLineEdit(self)
        self.q.move(260, 200)
        self.q.resize(200, 30)

        self.showlable = QLabel(self)
        self.showlable.setText("")
        self.showlable.move(200, 255)

        # Create a button in the window
        self.button = QPushButton("Show text", self)
        self.button.move(190, 280)

        # connect button to function on_click
        self.button.clicked.connect(self.on_click)
        self.show()

    @pyqtSlot()
    def on_click(self):
        # init variables
        tval = self.t.text()
        stval = self.st.text()
        nval = self.n.text()
        snval = self.sn.text()
        fval = self.f.text()
        qval = self.q.text()
        # float conversion
        ftval = float(tval)
        fstval = float(stval)
        fnval = float(nval)
        fsnval = float(snval)
        ffval = float(fval)
        fqval = float(qval)
        # equation init
        ev = float(
            100 * (((ftval * fnval) / (fstval * fsnval)) + (ffval * fqval * fqval))
        )
        # show label showing E
        sev = str(ev)
        self.showlable.setText(sev)
        # update googlesheetcell
        sheet.insert_row([today, ftval, fstval, fnval, fsnval, ffval, fqval, ev], 2)

        self.t.setText("")
        self.st.setText("")
        self.n.setText("")
        self.sn.setText("")
        self.f.setText("")
        self.q.setText("")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
# https://docs.google.com/spreadsheets/d/1zJMqB5eIj0NJ62VrNjPFaxHcdmSXa3Z04cRiF9Qrtcw/edit?gid=0#gid=0
