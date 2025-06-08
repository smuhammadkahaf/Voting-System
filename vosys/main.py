import tkinter as tk
from LoginUI import LoginUI
from AdminPanelUI import AdminPanelUI

window = tk.Tk()
# app = LoginUI(window)
app = AdminPanelUI(window)
window.mainloop()

