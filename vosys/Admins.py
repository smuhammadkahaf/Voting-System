from xml.dom.minidom import Comment

from BaseClass import BaseClass
from Common import Common
class Admin(BaseClass):
    user = None

    def __init__(self,users,pass_word):
        super().__init__()
        self.username = Common.locker(users)
        self.password = Common.locker(pass_word)
        self.ensure_db()

    def edit_details (self,users,pass_word):
        #encrypting username
        self.username = Common.locker(users)
        self.password = Common.locker(pass_word)

    def validate_admin(self):
        query = "select * from admins where username = '"+ self.username +"' and password = '"+ self.password+"';"
        result = self.db.query(query)
        Admin.user = result['first_row'][0] if result['first_row'] is not None else None

        if result["count_row"] == 1: #admin found
            return True
        else:
            return False

    def create_admin(self,name,username,password):
        name = Common.locker(name)
        username = Common.locker(username)
        password = Common.locker(password)

        query= "SELECT * FROM admins WHERE username = '"+username+"';"
        result = self.db.query(query)
        if result["count_row"] ==1:
            return 0# username already exist
        else:
            query = "INSERT INTO admins(name,username,password) VALUES ('"+name+"','"+username+"','"+password+"');"
            self.db.insert(query)
            return 1# username created

    def get_all_admins(self):
        query = "SELECT * FROM admins;"
        result = self.db.query(query)
        return result["all_rows"]





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