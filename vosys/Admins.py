
from BaseClass import BaseClass

class Admin(BaseClass):

    def __init__(self,users,pass_word):
        print("inside here")

        super().__init__()
        print("inside here1")
        self.username = users
        print("inside here2")

        self.password = pass_word
        print("inside here3")



    def edit_details (self,users,pass_word):
        self.username = users
        self.password = pass_word

    def validate_admin(self):
        print("hi validator")
        self.ensure_db()
        print("hi validator2")
        query = "select * from admins where username = '"+ self.username +"' and password = '"+ self.password+"';"
        result= self.db.query(query)

        print("hi validator3")

        if result["count_row"] == 1:
            return 1
        else:
            return 0
'''
user = Admin("user0314","LetmeIn")
print(user.validate_admin())
'''
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