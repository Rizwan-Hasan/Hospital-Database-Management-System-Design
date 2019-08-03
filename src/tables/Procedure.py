class Operations:

    def __init__(self, db):
        self.__connection = db.getConnection()
        self.__cursor = self.__connection.cursor()
        self.__message: str = str()

    def DML(self, actionType: int, procedure_id: str, ref_id: str, patient_id: str, cost: str, result: str):
        if actionType is 0:
            self.__insert(procedure_id, ref_id, patient_id, cost, result)
        elif actionType is 1:
            self.__update(procedure_id, ref_id, patient_id, cost, result)
        elif actionType is 2:
            self.__delete(procedure_id)
        else:
            self.__message = "Unknown action type"

    def __insert(self, procedure_id: str, ref_id: str, patient_id: str, cost: str, result: str):
        try:
            sql: str = "INSERT INTO `procedure` (procedure_id, ref_id, patient_id, cost, result) " \
                       "VALUES (%s, %s, %s, %s, %s)"
            val: tuple = (procedure_id, ref_id, patient_id, cost, result)
            self.__cursor.execute(sql, val)
            self.__connection.commit()
            self.__message = 'Row insertion successfull in Procedure Table.'
        except Exception as e:
            print(e)
            self.__message = 'Row insertion unsuccessfull in Procedure Table.'

    def __update(self, procedure_id: str, ref_id: str, patient_id: str, cost: str, result: str):
        try:
            sql: str = "UPDATE `procedure` " \
                       "SET ref_id = '{0}', patient_id = '{1}', cost = '{2}', result = '{3}' " \
                       "WHERE procedure_id = '{4}'" \
                .format(ref_id, patient_id, cost, result, procedure_id)
            self.__cursor.execute(sql)
            self.__connection.commit()
            self.__message = 'Row updation successfull in Procedure Table.'
        except Exception as e:
            print(e)
            self.__message = 'Row updation unsuccessfull in Procedure Table.'

    def __delete(self, procedure_id: str):
        try:
            sql: str = "DELETE FROM `procedure` WHERE procedure_id='{0}'" \
                .format(procedure_id)
            self.__cursor.execute(sql)
            self.__connection.commit()
            self.__message = 'Row deletion successfull in Procedure Table.'
        except Exception as e:
            print(e)
            self.__message = 'Row deletion unsuccessfull in Procedure Table.'

    def getStatus(self):
        return self.__message
