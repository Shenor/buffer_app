import sys
import json
import tkinter as tk
from datetime import datetime 
from PyQt5 import QtWidgets, uic


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('./view/main.ui', self)
        
        # Set Clipboard
        self.clipboard = app.clipboard()

        self.pushButton.setText("Text changed")
        self.pushButton.clicked.connect(self.printButtonPressed)
        self.show()

        self.clipboard.dataChanged.connect(self.detectClipboard)

    def printButtonPressed(self):
        # This is executed when the button is pressed
        self.listWidget.addItem('asd')
        print('printButtonPressed')
    
    def detectClipboard(self):
        text = self.clipboard.text()
        self.listWidget.addItem(text)
        print(text)

# GUI Variables #
app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()

# Clipboard
# clipboard = app.clipboard()

# Json format variables #
# now = datetime.now()
# history = []
# record = {"message": "Lol you father", "createAt": now.strftime("%d.%m.%Y %H:%M")}

# history.append(record)

# try:
#     with open('./data.json', 'r+') as f:
#         data = json.load(f)
#         data.append(record)
#         f.seek(0)
#         json.dump(data, f, ensure_ascii=False, indent=4)
#         print(data)
# except IOError:
#     with open("./data.json", "w", encoding='utf-8') as outfile:
#         json.dump(history, outfile, ensure_ascii=False, indent=4)
#     print("Файл не найден!")

# print(record)
