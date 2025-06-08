from xml.dom.minidom import Comment

from BaseClass import BaseClass
from Common import Common
class Admin(BaseClass):
    user = None

    def __init__(self):
        super().__init__()
        self.ensure_db()


    def validate_admin(self,username,password):
        query = "select * from admins where username = '"+ username +"' and password = '"+ password+"';"
        result = self.db.query(query)
        Admin.user = result['first_row'][0] if result['first_row'] is not None else None

        if result["count_row"] == 1: #admin found
            return True
        else:
            return False

    def create_admin(self,name,username,password,status_):
        name = Common.locker(name)
        username = Common.locker(username)
        password = Common.locker(password)
        status =status_

        query= "SELECT * FROM admins WHERE username = '"+username+"';"
        result = self.db.query(query)
        if result["count_row"] ==1:
            return 0# username already exist
        else:
            table_name = "admins"
            data = {
                "Name": name,
                "username":username,
                "password": password,
                "status": status
            }
            self.db.insert(table_name,data)
            return 1# username created

    def get_all_admins(self):
        query = "SELECT id,Name,username,status FROM admins;"
        result = self.db.query(query)
        return result["all_rows"]

    def get_admin(self,id_):
        query = "SELECT Name,username,password FROM admins WHERE id = " + str(id_) + ";"
        result = self.db.query(query)
        return result["first_row"][0]
    def update_admin(self,data,condition):
        self.db.update("admins",data,condition)






'''       
Model
Admin

view
logging
    email
    password
    btn
form

EndUser
vote cast

Controller
Admin
    login_view
    login

'''