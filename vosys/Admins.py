from xml.dom.minidom import Comment

from BaseClass import BaseClass
from Common import Common
class Admin(BaseClass):

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
        result= self.db.query(query)

        if result["count_row"] == 1: #admin found
            return 1
        else:
            return 0

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