import mysql.connector

class Database:

    __conection = mysql.connector.connect(user='root', password='20232023', port = '3306',  host='localhost', database='word')

    __cursor = __conection.cursor(prepared=True)

    @classmethod
    def cursor(cls):
        return cls.__cursor

