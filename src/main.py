# -*-coding: UTF-8 -*-

import os
import sys

# My Imports
from OracleDBConnection import OracleConn
from TableCreateDrop import TableOperation

# PyQt5 Imports
import PyQt5
from PyQt5 import uic
from PyQt5 import QtGui
from PyQt5.QtGui import QIcon, QFont, QPixmap, QMovie
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QLabel, QPushButton, QErrorMessage
from PyQt5.QtWidgets import QFileDialog, QDesktopWidget, QTextEdit
from PyQt5.QtCore import pyqtSlot, QSize, pyqtSignal, QThread

# Application root location ↓
appFolder = os.path.dirname(os.path.realpath(sys.argv[0])) + "\\"


class MainWindow(QMainWindow):
    MyDb = OracleConn()

    def __init__(self):
        super(MainWindow, self).__init__()

        # Loading Main UI Design Files ↓
        uic.loadUi(appFolder + 'ui\\MainWindow.ui', self)

        self.MyDb.connect()

        self.mainWindow()

    def mainWindow(self):
        self.setWindowTitle("Hospital Patient Management System")

        tableOperation = TableOperation(appFolder, self.MyDb.getCursor())

        tableOperation.create()
        tableOperation.drop()
        self.MyDb.close()


# Main Function ↓
def main():
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())


# Start Application ↓
if __name__ == '__main__':
    main()
