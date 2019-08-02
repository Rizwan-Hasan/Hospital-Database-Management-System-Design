class Operations:
    def __init__(self, db):
        self.__connection = db.getConnection()
        self.__cursor = self.__connection.cursor()
        self.__message: str = str()

    def insert(self, ref_id: str, docName: str, docDetails: str):
        try:
            sql: str = "INSERT INTO referral (ref_id, doctor, details) VALUES (%s, %s, %s)"
            val: tuple = (ref_id, docName, docDetails)
            self.__cursor.execute(sql, val)
            self.__connection.commit()
            self.__message = 'Row insertion successfull in Referral Table.'
        except:
            self.__message = 'Row insertion unsuccessfull in Referral Table.'

    def update(self, ref_id: str, docName: str, docDetails: str):
        try:
            sql: str = "UPDATE referral SET doctor = '{0}', details = '{1}' WHERE ref_id='{2}'" \
                .format(docName, docDetails, ref_id)
            self.__cursor.execute(sql)
            self.__connection.commit()
            self.__message = 'Row updation successfull in Referral Table.'
        except:
            self.__message = 'Row updation unsuccessfull in Referral Table.'

    def delete(self, ref_id: str):
        try:
            sql: str = "DELETE FROM referral WHERE ref_id='{0}'" \
                .format(ref_id)
            self.__cursor.execute(sql)
            self.__connection.commit()
            self.__message = 'Row deletion successfull in Referral Table.'
        except KeyboardInterrupt:
            self.__message = 'Row deletion unsuccessfull in Referral Table.'

    def getStatus(self):
        return self.__message
