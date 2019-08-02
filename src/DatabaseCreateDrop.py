class TableOperation:

    def __init__(self, appFolder: str, cursor):
        self.appFolder = appFolder
        self.cursor = cursor

    def create(self):
        try:
            with open(self.appFolder + 'sql_scripts\\create_script.sql', 'r', encoding='utf-8') as file:
                for query in file.read().replace('\n', '').split(';')[:-1]:
                    # print(query)
                    self.cursor.execute(query)
            print("Table creation successful")
        except Exception as e:
            print(e)
            print("Table creation error")

    def drop(self):
        try:
            with open(self.appFolder + 'sql_scripts\\drop_script.sql', 'r', encoding='utf-8') as file:
                for query in file.read().replace('\n', '').split(';')[:-1]:
                    # print(query)
                    self.cursor.execute(query)
            print("Table dropping successfull")
        except Exception as e:
            print(e)
            print("Table dropping error")
