# -*-coding: UTF-8 -*-

import os
import sys
from re import compile as regexCompile
# noinspection PyUnresolvedReferences
import resources

# My Imports
from tables import Referral, Patient, Procedure, Bill
from MariaDBConnection import MariaDbConn
from DatabaseCreateDrop import TableOperation

# PyQt5 Imports
import PyQt5
from PyQt5 import uic
from PyQt5 import QtGui
from PyQt5.QtGui import QIcon, QFont, QPixmap, QMovie
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QLabel, QPushButton, QErrorMessage, QStyleFactory, \
	QTableWidget, QTableWidgetItem, QTableWidgetSelectionRange, QTableView, QAbstractScrollArea
from PyQt5.QtWidgets import QFileDialog, QDesktopWidget, QTextEdit
from PyQt5.QtCore import pyqtSlot, QSize, pyqtSignal, QThread, Qt

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
		self.__buttonActionSetter()
		self.MyDb.connect()
		self.__mainWindow()

	def showStatus(self, message: str, x: bool = False):
		self.statusBar().styleSheet()
		self.statusBar().showMessage(message)
		res = regexCompile(r"\bsuccessfull\b")
		if x is True:
			try:
				QMessageBox.information(self, res.findall(message)[0].capitalize(), message)
			except IndexError:
				QMessageBox.information(self, "Unsuccessfull", message)

	def makeWindowCenter(self):
		# For launching windows in center
		qtRectangle = self.frameGeometry()
		centerPoint = QDesktopWidget().availableGeometry().center()
		qtRectangle.moveCenter(centerPoint)
		self.move(qtRectangle.topLeft())

	def closeEvent(self, event):
		try:
			# noinspection PyCallByClass
			buttonReply = QMessageBox.question(self, 'Message', "Do you really want to exit?",
											   QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
			if buttonReply == QMessageBox.Yes:
				print('Exitted')
				event.accept()
			else:
				event.ignore()
			self.show()
		except AttributeError:
			pass

	def __buttonActionSetter(self):
		# Referral Table DML
		self.pushBtn_ref_insert.clicked.connect(lambda: self.__ref_DML(0))
		self.pushBtn_ref_update.clicked.connect(lambda: self.__ref_DML(1))
		self.pushBtn_ref_delete.clicked.connect(lambda: self.__ref_DML(2))
		# Patient Table DML
		self.pushBtn_patient_insert.clicked.connect(lambda: self.__patient_DML(0))
		self.pushBtn_patient_update.clicked.connect(lambda: self.__patient_DML(1))
		self.pushBtn_patient_delete.clicked.connect(lambda: self.__patient_DML(2))
		# Procedure Table DML
		self.pushBtn_proc_insert.clicked.connect(lambda: self.__procedure_DML(0))
		self.pushBtn_proc_update.clicked.connect(lambda: self.__procedure_DML(1))
		self.pushBtn_proc_delete.clicked.connect(lambda: self.__procedure_DML(2))
		# Bill Table DML
		self.pushBtn_bill_insert.clicked.connect(lambda: self.__bill_DML(0))
		self.pushBtn_bill_update.clicked.connect(lambda: self.__bill_DML(1))
		self.pushBtn_bill_delete.clicked.connect(lambda: self.__bill_DML(2))

	def __mainWindow(self):
		self.makeWindowCenter()
		self.setWindowTitle("Hospital Patient Management System")
		self.showStatus("Developed by Rizwan Hasan using Python and PyQt5")

		table = Referral.Operations(self.MyDb)
		ddl = table.DDL(self.ddlTable)

	def __ref_DML(self, x: int):
		try:
			self.pushBtn_ref_insert.clicked.disconnect()
			self.pushBtn_ref_update.clicked.disconnect()
			self.pushBtn_ref_delete.clicked.disconnect()
		except (TypeError, AttributeError):
			pass
		table = Referral.Operations(self.MyDb)
		table.DML(
			actionType=x,
			ref_id=self.lineEdit_ref_id.text().strip(),
			docName=self.lineEdit_doctor.text().strip(),
			docDetails=self.plainTextEdit_deatils.toPlainText().strip()
		)
		self.showStatus(table.getStatus(), True)
		self.pushBtn_ref_insert.clicked.connect(lambda: self.__ref_DML(0))
		self.pushBtn_ref_update.clicked.connect(lambda: self.__ref_DML(1))
		self.pushBtn_ref_delete.clicked.connect(lambda: self.__ref_DML(2))

	# noinspection DuplicatedCode
	def __patient_DML(self, x: int):
		try:
			self.pushBtn_patient_insert.clicked.disconnect()
			self.pushBtn_patient_update.clicked.disconnect()
			self.pushBtn_patient_delete.clicked.disconnect()
		except (TypeError, AttributeError):
			pass
		table = Patient.Operations(self.MyDb)
		table.DML(
			actionType=x,
			patient_id=self.lineEdit_patient_id.text().strip(),
			ref_id=self.lineEdit_p_ref_id.text().strip(),
			name=self.lineEdit_patient_name.text().strip(),
			sex=self.lineEdit_patient_sex.text().strip(),
			addr=self.lineEdit_patient_address.text().strip()
		)
		self.showStatus(table.getStatus(), True)
		self.pushBtn_patient_insert.clicked.connect(lambda: self.__patient_DML(0))
		self.pushBtn_patient_update.clicked.connect(lambda: self.__patient_DML(1))
		self.pushBtn_patient_delete.clicked.connect(lambda: self.__patient_DML(2))

	# noinspection DuplicatedCode
	def __procedure_DML(self, x: int):
		try:
			self.pushBtn_proc_insert.clicked.disconnect()
			self.pushBtn_proc_update.clicked.disconnect()
			self.pushBtn_proc_delete.clicked.disconnect()
		except (TypeError, AttributeError):
			pass
		table = Procedure.Operations(self.MyDb)
		table.DML(
			actionType=x,
			procedure_id=self.lineEdit_procedure_id.text().strip(),
			ref_id=self.lineEdit_procedure_ref_id.text().strip(),
			patient_id=self.lineEdit_procedure_p_id.text().strip(),
			cost=self.lineEdit_procedure_cost.text().strip(),
			result=self.lineEdit_procedure_result.text().strip()
		)
		self.showStatus(table.getStatus(), True)
		self.pushBtn_proc_insert.clicked.connect(lambda: self.__procedure_DML(0))
		self.pushBtn_proc_update.clicked.connect(lambda: self.__procedure_DML(1))
		self.pushBtn_proc_delete.clicked.connect(lambda: self.__procedure_DML(2))

	# noinspection DuplicatedCode
	def __bill_DML(self, x: int):
		try:
			self.pushBtn_bill_insert.clicked.disconnect()
			self.pushBtn_bill_update.clicked.disconnect()
			self.pushBtn_bill_delete.clicked.disconnect()
		except (TypeError, AttributeError):
			pass
		table = Bill.Operations(self.MyDb)
		table.DML(
			actionType=x,
			bill_id=self.lineEdit_bill_id.text().strip(),
			procedure_id=self.lineEdit_bill_proc_id.text().strip(),
			patient_id=self.lineEdit_bill_patient_id.text().strip(),
			ref_id=self.lineEdit_bill_ref_id.text().strip(),
			total_cost=self.lineEdit_bill_cost.text().strip(),
			bill_date=self.lineEdit_bill_date.text().strip()
		)
		self.showStatus(table.getStatus(), True)
		self.pushBtn_bill_insert.clicked.connect(lambda: self.__bill_DML(0))
		self.pushBtn_bill_update.clicked.connect(lambda: self.__bill_DML(1))
		self.pushBtn_bill_delete.clicked.connect(lambda: self.__bill_DML(2))


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
