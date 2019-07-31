import mysql.connector as mariadb


class OracleConn:
    __username: str = 'rizwan'
    __password: str = '01733938633'
    __server: str = 'localhost'
    __port: int = 3306
    __database: str = 'hospitaldb'

    def __init__(self):
        self.__connection = None

    def connect(self):
        try:
            self.__connection = mariadb.connect(
                host=self.__server,
                port=self.__port,
                database=self.__database,
                user=self.__username,
                passwd=self.__password)
            print("Connection successfull")
        except ValueError:
            print("Connection unsuccessfull")

    def getConnection(self):
        return self.__connection

    def execute(self, query: str):
        try:
            data = self.__connection.cursor()
            data.execute(query)
            return data.fetchall()
        except:
            return -1

    def close(self):
        self.__connection.close()
