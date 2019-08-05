# PyQt5 Imports
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidgetItem


class Operations:

	def __init__(self, db):
		self.__connection = db.getConnection()
		self.__cursor = self.__connection.cursor()
		self.__message: str = str()

	def DML(self, actionType: int, patient_id: str, ref_id: str, name: str, sex: str, addr: str):
		if actionType is 0:
			self.__insert(patient_id, ref_id, name, sex, addr)
		elif actionType is 1:
			self.__update(patient_id, ref_id, name, sex, addr)
		elif actionType is 2:
			self.__delete(patient_id)
		else:
			self.__message = "Unknown action type"

	# noinspection DuplicatedCode
	def DDL(self, tableView):
		cursor = self.__connection.cursor()
		cursor.execute('SELECT COUNT(*) as "row" FROM patient')
		rowCount = int(cursor.fetchone()[0])
		cursor.execute('SELECT COUNT(*) as "column" FROM information_schema.columns WHERE table_name = \'patient\'')
		columnCount = int(cursor.fetchone()[0])
		cursor.execute('SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME=\'patient\'')
		columnNameList: list = list()
		for i in cursor.fetchall():
			columnNameList.append(i[0])
		cursor.execute('SELECT * FROM patient')
		data = cursor.fetchall()

		# Table View
		tableView.setRowCount(0)
		tableView.setRowCount(rowCount)
		tableView.setColumnCount(columnCount)
		tableView.setHorizontalHeaderLabels(columnNameList)
		# tableView.resizeColumnsToContents()

		rowPosition: int = 0
		for i in range(len(data)):
			# print(data[i])
			tableView.insertRow(rowPosition)
			for j in range(len(data[i])):
				# print(data[i][j])
				item = QTableWidgetItem(str(data[i][j]) if type(data[i][j]) is int else data[i][j])
				item.setFlags(Qt.ItemIsEnabled)
				tableView.setItem(rowPosition, j, item)
			rowPosition += 1

	def __insert(self, patient_id: str, ref_id: str, name: str, sex: str, addr: str):
		try:
			sql: str = "INSERT INTO patient (patient_id, ref_id, name, sex, address) " \
					   "VALUES (%s, %s, %s, %s, %s)"
			val: tuple = (patient_id, ref_id, name, sex, addr)
			self.__cursor.execute(sql, val)
			self.__connection.commit()
			self.__message = 'Row insertion successfull in Patient Table.'
		except Exception as e:
			print(e)
			self.__message = 'Row updation unsuccessfull in Procedure Table.'

	def __update(self, patient_id: str, ref_id: str, name: str, sex: str, addr: str):
		try:
			sql: str = "UPDATE patient " \
					   "SET name = '{0}', sex = '{1}', address = '{2}' " \
					   "WHERE patient_id = '{3}' AND ref_id = '{4}'" \
				.format(name, sex, addr, patient_id, ref_id)
			self.__cursor.execute(sql)
			self.__connection.commit()
			self.__message = 'Row updation successfull in Patient Table.'
		except Exception as e:
			print(e)
			self.__message = 'Row updation unsuccessfull in Procedure Table.'

	def __delete(self, patient_id: str):
		try:
			sql: str = "DELETE FROM patient WHERE patient_id='{0}'" \
				.format(patient_id)
			self.__cursor.execute(sql)
			self.__connection.commit()
			self.__message = 'Row deletion successfull in Patient Table.'
		except Exception as e:
			print(e)
			self.__message = 'Row updation unsuccessfull in Procedure Table.'

	def getStatus(self):
		return self.__message
