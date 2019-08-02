class Operations:

    def __init__(self, db):
        self.__connection = db.getConnection()
        self.__cursor = self.__connection.cursor()
        self.__message: str = str()

    def insert(self, bill_id: str, procedure_id: str, patient_id: str, ref_id: str, total_cost: str, bill_date: str):
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

    def update(self, bill_id: str, procedure_id: str, patient_id: str, ref_id: str, total_cost: str, bill_date: str):
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

    def delete(self, bill_id: str):
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
