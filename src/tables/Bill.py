# PyQt5 Imports
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidgetItem


class Operations:

	def __init__(self, db):
		self.__connection = db.getConnection()
		self.__cursor = self.__connection.cursor()
		self.__message: str = str()

	def DML(self, actionType: int, bill_id: str, procedure_id: str, patient_id: str, ref_id: str, total_cost: str,
			bill_date: str):
		if actionType is 0:
			self.__insert(bill_id, procedure_id, patient_id, ref_id, total_cost, bill_date)
		elif actionType is 1:
			self.__update(bill_id, procedure_id, patient_id, ref_id, total_cost, bill_date)
		elif actionType is 2:
			self.__delete(bill_id)
		else:
			self.__message = "Unknown action type"

	# noinspection DuplicatedCode
	def DDL(self, tableView):
		cursor = self.__connection.cursor()
		cursor.execute('SELECT COUNT(*) as "row" FROM bill')
		rowCount = int(cursor.fetchone()[0])
		cursor.execute('SELECT COUNT(*) as "column" FROM information_schema.columns WHERE table_name = \'bill\'')
		columnCount = int(cursor.fetchone()[0])
		cursor.execute('SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME=\'bill\'')
		columnNameList: list = list()
		for i in cursor.fetchall():
			columnNameList.append(i[0])
		cursor.execute('SELECT * FROM bill')
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

	def __insert(self, bill_id: str, procedure_id: str, patient_id: str, ref_id: str, total_cost: str, bill_date: str):
		try:
			sql: str = "INSERT INTO bill  (bill_id, procedure_id, patient_id, ref_id, total_cost, bill_date) " \
					   "VALUES (%s, %s, %s, %s, %s, %s)"
			val: tuple = (bill_id, procedure_id, patient_id, ref_id, total_cost, bill_date)
			self.__cursor.execute(sql, val)
			self.__connection.commit()
			self.__message = 'Row insertion successfull in Bill Table.'
		except Exception as e:
			print(e)
			self.__message = 'Row insertion unsuccessfull in Bill Table.'

	def __update(self, bill_id: str, procedure_id: str, patient_id: str, ref_id: str, total_cost: str, bill_date: str):
		try:
			sql: str = "UPDATE bill SET " \
					   "procedure_id = '{0}'," \
					   "patient_id = '{1}'," \
					   "ref_id = '{2}'," \
					   "total_cost = '{3}'," \
					   "bill_date = '{4}' " \
					   "WHERE bill_id = '{5}'" \
				.format(procedure_id, patient_id, ref_id, total_cost, bill_date, bill_id)
			self.__cursor.execute(sql)
			print(self.__connection.commit())
			self.__message = 'Row updation successfull in Bill Table.'
		except Exception as e:
			print(e)
			self.__message = 'Row updation unsuccessfull in Bill Table.'

	def __delete(self, bill_id: str):
		try:
			sql: str = "DELETE FROM bill WHERE bill_id='{0}'" \
				.format(bill_id)
			self.__cursor.execute(sql)
			self.__connection.commit()
			self.__message = 'Row deletion successfull in Bill Table.'
		except Exception as e:
			print(e)
			self.__message = 'Row deletion unsuccessfull in Bill Table.'

	def getStatus(self):
		return self.__message
