import mysql.connector
from RSA import RSA

class Database:
    def __init__(self,h="localhost",u = "root",p="root",d="vosys",c="utf8mb4"):
        self.rsa =RSA()
        self.connection = ""
        self.cursor =""
        self.host =h
        self.user = u
        self.password = p
        self.database = d
        self.charset = c

        self.connected()


    def connected(self):
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database,
            charset=self.charset
        )
        self.cursor = self.connection.cursor()


    def query(self,q):
        self.cursor.execute(q)
        columns = [desc[0] for desc in self.cursor.description]
        rows = self.cursor.fetchall()
        result = [dict(zip(columns, row)) for row in rows]
        results = {"all_rows" : result,
                   "count_row" : len(result) }
        if result:
            results["first_row"] =  result[0],
            results["last_row"] =  result[len(result) - 1]
        else:
            results["first_row"] = None
            results["last_row"] = None
        return results

    def insert(self,q):
        self.cursor.execute(q)
        self.connection.commit()




    def close_all(self):
            self.cursor.close()
            self.connection.close()



'''
[
    "all";[{},{}]
    first:{}
    last
]'''

