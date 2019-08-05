import os
import sys
from re import compile as regexCompile

# PyQt5 Imports
from PyQt5 import uic
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QStyleFactory
from PyQt5.QtWidgets import QDesktopWidget

# noinspection PyUnresolvedReferences
import resources
from MariaDBConnection import MariaDbConn
# My Imports
from main import MainWindow
from tables import Referral, Patient, Procedure, Bill


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
