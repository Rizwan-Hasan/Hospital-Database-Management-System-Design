import json

import mysql.connector as mariadb


class MariaDbConn:

	def __init__(self, appFolder: str, obj):
        self.__connection = None
		self.__mainObj = obj
        with open(appFolder + 'DbConfig.json', 'r', encoding='utf-8') as file:
            self.dbConfig: dict = json.load(file)

    def connect(self):
        try:
            self.__connection = mariadb.connect(
                host=self.dbConfig.get('host'),
                port=self.dbConfig.get('port'),
                database=self.dbConfig.get('database'),
                user=self.dbConfig.get('username'),
                passwd=self.dbConfig.get('password')
            )
            print("Connection successfull")
			self.__mainObj.showStatus("Connection successfull")
        except Exception as e:
            print(e)
            try:
                self.__connection = mariadb.connect(
                    host=self.dbConfig.get('host'),
                    port=self.dbConfig.get('port'),
                    # database=self.dbConfig.get('database'),
                    user=self.dbConfig.get('username'),
                    passwd=self.dbConfig.get('password')
                )
                print("Connection successfull")
				self.__mainObj.showStatus("Connection successfull")
            except Exception as e:
                print(e)
				self.__mainObj.showStatus("Connection unsuccessfull")
                print("Connection unsuccessfull")

    def getConnection(self):
        return self.__connection

    def execute(self, query: str):
        data = self.__connection.cursor()
        data.execute(query)
        return data.fetchall()

    def close(self):
        try:
            self.__connection.close()
            print("Close operation is successfull")
        except Exception as e:
            print(e)
            print("Close operation isn't successfull")
