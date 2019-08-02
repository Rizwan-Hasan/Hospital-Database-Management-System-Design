# -*-coding: UTF-8 -*-

import os
import sys
import resources

# My Imports
from MariaDbConnection import OracleConn
from DatabaseCreateDrop import TableOperation

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
    MyDb = OracleConn(appFolder)

    def __init__(self):
        # noinspection PyArgumentList
        super(MainWindow, self).__init__()

        # Loading Main UI Design Files ↓
        uic.loadUi(appFolder + 'ui\\MainWindow.ui', self)

        # Icon Variables
        self.icon = QIcon(':/icon/icon.png')

        self.MyDb.connect()
        self.mainWindow()

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
        self.setWindowIcon(self.icon)

        # tableOperation = TableOperation(appFolder, self.MyDb)
        # tableOperation.create()
        # tableOperation.drop()
        # mycursor = self.MyDb.execute("show databases")
        # for i in mycursor:
        #     print(i)

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
