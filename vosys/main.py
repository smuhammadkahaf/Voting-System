import tkinter as tk
from UI.LoginUI import LoginUI

window = tk.Tk()
app = LoginUI(window)
# app = AdminPanelUI(window)
window.mainloop()

