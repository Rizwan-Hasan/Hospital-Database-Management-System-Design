# -*-coding: UTF-8 -*-

import os
import sys
# noinspection PyUnresolvedReferences
import resources

# My Imports
from tables import Referral, Patient, Procedure, Bill
from MariaDbConnection import MariaDbConn
from DatabaseCreateDrop import TableOperation

# PyQt5 Imports
import PyQt5
from PyQt5 import uic
from PyQt5 import QtGui
from PyQt5.QtGui import QIcon, QFont, QPixmap, QMovie
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QLabel, QPushButton, QErrorMessage, QStyleFactory
from PyQt5.QtWidgets import QFileDialog, QDesktopWidget, QTextEdit
from PyQt5.QtCore import pyqtSlot, QSize, pyqtSignal, QThread

# Application root location ↓
appFolder = os.path.dirname(os.path.realpath(sys.argv[0])) + "\\"


class MainWindow(QMainWindow):
    MyDb = MariaDbConn(appFolder)

    def __init__(self):
        # noinspection PyArgumentList
        super(MainWindow, self).__init__()

        # Loading Main UI Design Files ↓
        uic.loadUi(appFolder + 'ui\\MainWindow.ui', self)

        # Stylesheet
        with open(appFolder + 'ui\\stylesheet.qss', 'r') as styleSheetFile:
            self.setStyleSheet(styleSheetFile.read())

        # Variables
        self.icon = QIcon(':/icon/icon.png')
        self.MyDb.connect()
        self.mainWindow()

    def showStatus(self, message: str):
        self.statusBar().styleSheet()
        self.statusBar().showMessage(message)

    def makeWindowCenter(self):
        # For launching windows in center
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

    # def closeEvent(self, event):
    #     try:
    #         # noinspection PyCallByClass
    #         buttonReply = QMessageBox.question(self, 'Message', "Do you really want to exit?",
    #                                            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
    #         if buttonReply == QMessageBox.Yes:
    #             print('Exitted')
    #             event.accept()
    #         else:
    #             event.ignore()
    #         self.show()
    #     except AttributeError:
    #         pass

    def mainWindow(self):
        self.makeWindowCenter()
        self.setWindowTitle("Hospital Patient Management System")
        self.showStatus("Developed by Rizwan Hasan using Python and PyQt5")

        # tableOperation = TableOperation(appFolder, self.MyDb)
        # tableOperation.create()
        # tableOperation.drop()
        # mycursor = self.MyDb.execute("show databases")
        # for i in mycursor:
        #     print(i)

        x = Bill.Operations(db=self.MyDb)
        x.update("601", "309", "203", "100", "1600", "2019-04-21")
        self.showStatus(x.getStatus())

        self.MyDb.close()


# Main Function ↓
def main():
    app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create('Fusion'))
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())


# Start Application ↓
if __name__ == '__main__':
    main()
