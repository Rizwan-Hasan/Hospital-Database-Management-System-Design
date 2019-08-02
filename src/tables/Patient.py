class Operations:

    def __init__(self, db):
        self.__connection = db.getConnection()
        self.__cursor = self.__connection.cursor()
        self.__message: str = str()

    def insert(self, patient_id: str, ref_id: str, name: str, sex: str, addr: str):
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

    def update(self, patient_id: str, ref_id: str, name: str, sex: str, addr: str):
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

    def delete(self, patient_id: str):
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
