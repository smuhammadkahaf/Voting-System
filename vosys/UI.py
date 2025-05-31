import tkinter
from Admins import Admin

user = Admin("user034","LetmeIn")
print(user.validate_admin())
window = tkinter.Tk()
window.title("VOSYS")

label = tkinter.Label(window,text="First program")

window.mainloop()