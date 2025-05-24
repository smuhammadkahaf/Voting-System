import sys
from fileinput import close

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi
from admin import Admin



class Login(QDialog):
    def __init__(self):
        super(Login,self).__init__()
        loadUi("UI\\login.ui", self)
        self.login.clicked.connect(self.login_pressed)
        self.invalid_user.hide()
        self.empty_fields.hide()
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
    def login_pressed(self):
        username = self.username.text()
        password = self.password.text()
        if username =="" or password == "":
            self.invalid_user.hide()
            self.empty_fields.show()
        else:

            user = Admin(username, password)
            if user.validate_admin() == 1:
                self.invalid_user.hide()
                self.empty_fields.hide()
            else:
                self.invalid_user.show()
