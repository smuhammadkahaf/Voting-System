from tkinter.constants import INSERT

import mysql.connector
class Database:
    def __init__(self,h="localhost",u = "root",p="root",d="vosys",c="utf8mb4"):
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

    # def insert(self,q):
    #     self.cursor.execute(q)
    #     self.connection.commit()
    def insert(self,table_name,data):
        query = "INSERT INTO "+table_name+" ("
        keys_list = list(data.keys())
        values_list = list(data.values())
        for i in range(len(keys_list)):
            query+= keys_list[i]
            if i<len(keys_list)-1:
                query +=" , "
        query +=") VALUES ("
        for i in range(len(values_list)):
            query =query +  " '" + str(values_list[i]) + "'"

            if i < len(values_list) - 1:
                query += " , "
        query += ");"
        self.cursor.execute(query)
        self.connection.commit()

    def update(self,table_name,data,condition):
        query = "UPDATE "+ table_name+ " SET "
        data_keys = list(data.keys())
        data_values= list(data.values())
        for i in range(len(data_keys)):
            query = query + data_keys[i] +" = '" + data_values[i] + "' "
            if i <len(data_values)-1:
                query +=" , "
        query = query + "WHERE " + condition +";"
        self.cursor.execute(query)
        self.connection.commit()





    def close_all(self):
            self.cursor.close()
            self.connection.close()

