import tkinter as tk
from UI.LoginUI import LoginUI
from UI.Admin.AdminPanelUI import AdminPanelUI

window = tk.Tk()
#app = LoginUI(window)
app = AdminPanelUI(window)
window.mainloop()

