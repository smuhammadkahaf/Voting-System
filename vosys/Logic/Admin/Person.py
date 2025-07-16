
from Includes.BaseClass import BaseClass
from Includes.Common import Common

class Person(BaseClass):

    def __init__(self):
        super().__init__()
        self.ensure_db()



    def create_person(self, name, cnic, date_of_birth, phone_number, email,key):
        name = Common.locker(name)
        cnic = Common.locker(cnic)
        date_of_birth = date_of_birth # no need to lock the date
        phone_number = Common.locker(phone_number)
        email = Common.locker(email)
        key = Common.locker(key)

        cnic_query= "SELECT * FROM users WHERE cnic = '"+cnic+"';"

        cnic_result = self.db.query(cnic_query)
        if cnic_result["count_row"] >=1:
            return 0# cnic already exist

        email_query = "SELECT * FROM users WHERE email = '" + email + "';"
        email_result = self.db.query(email_query)

        if email_result["count_row"] >=1:
            return 1# email already exist

        else:
            table_name = "users"
            data = {
                "Name": name,
                "cnic":cnic,
                "date_of_birth": date_of_birth,
                "phone_number": phone_number,
                "email": email,
                "key_": key
            }
            self.db.insert_single(table_name,data)
            return 2# person created

    def get_person_id(self,cnic):
        query = "SELECT id FROM users where cnic = '" + Common.locker(cnic) + "';"
        id = self.db.query(query)
        print(id)
        return id["first_row"][0]["id"]

    def remove_person_from_all(self,person_id):
        condition = "user_id = " +str(person_id)
        self.db.delete("Person_Categories",condition)

    def add_person_in_class(self,person_id,category_id):
        self.remove_person_from_all(person_id)
        table_name = "Person_Categories"
        columns = ["user_id","category_id"]
        print(columns)
        rows = []
        for i in range(len(category_id)):
            rows.append([person_id,category_id[i]])
        print(rows)
        self.db.insert_multiple(table_name,columns,rows)

    def get_all_persons(self):
        query = "SELECT u.id AS id, u.name AS Name, u.cnic as CNIC, COUNT(pc.category_id) AS number_in_categories FROM users u LEFT JOIN person_categories pc ON u.id = pc.user_id GROUP BY u.id, u.name, u.cnic;"
        result = self.db.query(query)
        return result["all_rows"]

    def get_person(self,id_):
        query = "SELECT name,cnic,date_of_birth,phone_number,email,key_ FROM users WHERE id = " + str(id_) + " ;"
        result = self.db.query(query)
        return result["first_row"][0]

    def person_in_categories(self,id_):
        query = "select category_name from categories where id in (select category_id from person_categories where user_id ="  + str(id_) + ");"
        result = self.db.query(query)
        result = result["all_rows"]
        categories = []
        for category in result:
            decrypted_category = Common.unlocker(category["category_name"])
            categories.append(decrypted_category)
        return categories

    def verify_person_existence(self, cnic):
        query = "SELECT id FROM users where cnic = '" + Common.locker(cnic) + "';"
        result = self.db.query(query)
        if result["count_row"] == 0:
            return False
        else:
            return True

    def get_number_of_persons(self):
        query = "select count(*) as persons from users;"
        results = self.db.query(query)
        results = results["first_row"][0]["persons"]

        return results

    def update_person(self,data,condition):
        email_query = "SELECT * FROM users WHERE email = '" + data["email"] + "';"
        email_result = self.db.query(email_query)

        if email_result["count_row"] >= 1:
            return 1  # email already exist
        self.db.update("users",data,condition)