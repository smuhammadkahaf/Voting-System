import tkinter as tk
from UI.LoginUI import LoginUI
from UI.Admin.AdminPanelUI import AdminPanelUI
from UI.Voter.EnrtyPoint import EntryPoint

window = tk.Tk()
# app = LoginUI(window)
app = AdminPanelUI(window)
# app = EntryPoint(window)
window.mainloop()

