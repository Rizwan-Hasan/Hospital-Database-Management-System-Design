# PyQt5 Imports
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidgetItem, QAbstractScrollArea


class Operations:

	def __init__(self, db):
		self.__connection = db.getConnection()
		self.__cursor = self.__connection.cursor()
		self.__message: str = str()

	def DML(self, actionType: int, ref_id: str, docName: str, docDetails: str):
		if actionType is 0:
			self.__insert(ref_id, docName, docDetails)
		elif actionType is 1:
			self.__update(ref_id, docName, docDetails)
		elif actionType is 2:
			self.__delete(ref_id)
		else:
			self.__message = "Unknown action type"

	def DDL(self, tableView):
		cursor = self.__connection.cursor()
		cursor.execute('SELECT COUNT(*) as "row" FROM referral')
		rowCount = int(cursor.fetchone()[0])
		cursor.execute('SELECT COUNT(*) as "column" FROM information_schema.columns WHERE table_name = \'referral\'')
		columnCount = int(cursor.fetchone()[0])
		cursor.execute('SELECT doctor FROM referral')

		# Table View
		tableView.setRowCount(rowCount)
		tableView.setColumnCount(columnCount)
		tableView.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
		tableView.resizeColumnsToContents()

		rowPosition = 0
		tableView.insertRow(rowPosition)
		item = QTableWidgetItem("text1")
		item.setFlags(Qt.ItemIsEnabled)
		tableView.setItem(rowPosition, 0, QTableWidgetItem("text1"))
		tableView.setItem(rowPosition, 1, QTableWidgetItem("text2"))
		tableView.setItem(rowPosition, 2, QTableWidgetItem("text3"))

	def __insert(self, ref_id: str, docName: str, docDetails: str):
		try:
			sql: str = "INSERT INTO referral (ref_id, doctor, details) " \
					   "VALUES (%s, %s, %s)"
			val: tuple = (ref_id, docName, docDetails)
			self.__cursor.execute(sql, val)
			self.__connection.commit()
			self.__message = 'Row insertion successfull in Referral Table.'
		except Exception as e:
			print(e)
			self.__message = 'Row insertion unsuccessfull in Referral Table.'

	def __update(self, ref_id: str, docName: str, docDetails: str):
		try:
			sql: str = "UPDATE referral SET doctor = '{0}', details = '{1}' WHERE ref_id='{2}'" \
				.format(docName, docDetails, ref_id)
			self.__cursor.execute(sql)
			self.__connection.commit()
			self.__message = 'Row updation successfull in Referral Table.'
		except Exception as e:
			print(e)
			self.__message = 'Row updation unsuccessfull in Referral Table.'

	def __delete(self, ref_id: str):
		try:
			sql: str = "DELETE FROM referral WHERE ref_id='{0}'" \
				.format(ref_id)
			self.__cursor.execute(sql)
			self.__connection.commit()
			self.__message = 'Row deletion successfull in Referral Table.'
		except Exception as e:
			print(e)
			self.__message = 'Row deletion unsuccessfull in Referral Table.'

	def getStatus(self):
		return self.__message
