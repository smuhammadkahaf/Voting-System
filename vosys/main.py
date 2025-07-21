import tkinter as tk
from UI.Voter.AvailableElections import AvailableElections
from UI.Admin.AdminPanelUI import  AdminPanelUI
from UI.Voter.EntryPoint import EntryPoint
from UI.Admin.LoginUI import LoginUI

window = tk.Tk()
# app = EntryPoint(window)
# app = LoginUI(window)
app = AdminPanelUI(window)
# AvailableElections(window,"4150405303331")
window.mainloop()
