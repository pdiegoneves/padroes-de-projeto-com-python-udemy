import sqlite3


class Singleton(type):
    __intances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls.__intances:
            cls.__intances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls.__intances[cls]
    

class Database(metaclass=Singleton):
    connection = None
    
    def connect(self):
        if self.connection is None:
            self.connection = sqlite3.connect("db.sqlite3")
            self.cursor = self.connection.cursor()
        return self.cursor
    
db1 = Database().connect()
print(f"Conexão 1: {id(db1)}")

db2 = Database().connect()
print(f"Conexão 2: {id(db2)}")
            