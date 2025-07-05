import tkinter as tk
from UI.LoginUI import LoginUI
from UI.Admin.AdminPanelUI import AdminPanelUI
from UI.Voter.EnrtyPoint import EntryPoint
from UI.Voter.AvailableElections import AvailableElections


window = tk.Tk()
# app = LoginUI(window)
# app = AdminPanelUI(window)
# app = EntryPoint(window)
AvailableElections(window,"4150405303331")
window.mainloop()

