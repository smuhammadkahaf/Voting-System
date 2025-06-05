from BaseClass import BaseClass
from RSA import  RSA
class Admin(BaseClass):

    def __init__(self,users,pass_word):
        super().__init__()
        self.username = users
        self.password = pass_word
        self.ensure_db()

    def edit_details (self,users,pass_word):
        self.username = users
        self.password = pass_word

    def validate_admin(self):
        query = "select * from admins where username = '"+ self.username +"' and password = '"+ self.password+"';"
        result= self.db.query(query)

        if result["count_row"] == 1: #admin found
            return 1
        else:
            return 0

    def create_admin(self,name,username,password):
        query= "SELECT * FROM admins WHERE username = '"+username+")"
        result = self.db.query(query)
        if result["count_row"] ==1:
            return 0# username already exist
        else:
            query = "INSERT INTO admins(name,username,password) VALUES ("+name+","+username+","+password+");"
            self.db.insert(query)
            return 1# username created

'''
user = Admin("user0314","LetmeIn")
print(user.validate_admin())'''

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