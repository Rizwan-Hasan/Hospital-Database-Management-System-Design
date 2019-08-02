import json

import mysql.connector as mariadb


class MariaDbConn:

    def __init__(self, appFolder: str):
        self.__connection = None
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
        except:
            try:
                self.__connection = mariadb.connect(
                    host=self.dbConfig.get('host'),
                    port=self.dbConfig.get('port'),
                    # database=self.dbConfig.get('database'),
                    user=self.dbConfig.get('username'),
                    passwd=self.dbConfig.get('password')
                )
                print("Connection successfull")
            except:
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
        except AttributeError:
            print("Close operation isn't successfull")
