import cx_Oracle


class OracleConn:
    __username: str = 'hr'
    __password: str = 'hr'
    __server: str = 'localhost'
    __service: str = 'XE'

    def __init__(self):
        self.__connection = None
        self.__cursor = None

    def connect(self):
        try:
            self.__connection = cx_Oracle.connect(self.__username,
                                                  self.__password,
                                                  self.__server + '//' + self.__service)
            self.__cursor = self.__connection.cursor()
            print("Connection successfull")
        except ValueError:
            print("Connection unsuccessfull")

    def getConnection(self):
        return self.__connection

    def getCursor(self):
        return self.__cursor

    def close(self):
        self.__cursor.close()
