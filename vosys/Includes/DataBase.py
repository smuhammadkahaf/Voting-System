from calendar import day_abbr

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
    def insert_single(self,table_name,data):
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
        print(query)
        self.cursor.execute(query)
        self.connection.commit()

    def insert_multiple(self,table_name,columns,data):
        if not columns or not data:
            return ""

        query = "INSERT INTO "+ table_name + "("
        for i in range(len(columns)):
            query = query + columns[i]
            if i!=len(columns)-1:
                query = query+","
            else:
                query = query + ") VALUES "

        for i in range(len(data)):
            query = query + "("
            for j in range(len(data[i])):
                query = query + "'"+ str(data[i][j]) +"'"
                if j != len(data[i])-1:
                    query += ","
                else:
                    query+= ")"

            if i != len(data)-1:
                query+=","
            else:
                query+=";"
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

    def delete(self,table_name, condition):
        query = "DELETE FROM " + table_name + " WHERE " + condition + ";"
        self.cursor.execute(query)
        self.connection.commit()

    def close_all(self):
            self.cursor.close()
            self.connection.close()

    def get_last_enterd_record(self,table_name):
        query = "SELECT * FROM " + table_name + " ORDER BY id DESC LIMIT 1;"
        result = self.query(query)
        return result["first_row"]

'''table_name  = "admins"
conditions = "id = 3"

Database.delete(table_name,conditions)'''

