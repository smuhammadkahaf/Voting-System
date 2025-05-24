from UI import Login
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog,QApplication


app = QApplication(sys.argv)
main_window = Login()
widget  = QtWidgets.QStackedWidget()
widget.addWidget(main_window)
widget.setFixedHeight(600)
widget.setFixedWidth(430)
widget.show()
app.exec_()


'''
secure = RSA(50657,2083,4675)
db = Database("localhost", "root", "root", "vosys","utf8mb4")

if db.verify_admin("user034","LetmeIn") ==0:
    print("no record found")
elif db.verify_admin("user034","LetmeIn") ==-1:
    print("Multiple users with id passwords")
elif db.verify_admin("user034","LetmeIn") == 1:
    print("access granted")
elif db.verify_admin("user034","LetmeIn") ==-2:
    print("other cases")
else :
    print("what is this....")

'''



'''msg  = input("Enter Message: ")

E = secure.encryptString(msg)
D = secure.decryptSting(E)
print("Original message  = ",msg)
print("Encrypted message  = ",E)
print("Decrypted message  = ",D)

input ("Press enter to Exit")'''