import tkinter as tk
from Includes.Common import Common
from Logic.Admin.Admins import Admin
from UI.Admin.AdminTab.CreateAdminFrame import CreateAdminFrame
from UI.Admin.AdminTab.updateAdminFrame import updateAdminFrame

class AdminFrame(tk.Frame):
    def __init__(self, parent):
        self.parent = parent
        super().__init__(parent, bg="#252525")

        # Title
        header = tk.Frame(self, bg="#252525", width=200)
        header.pack(pady=20,anchor="n",fill="x")
        tk.Label(header, text="Admin Records", font=("Arial", 24), fg="white", bg="#252525").pack(pady=20)
        Create_admin_button = Common.new_button(header,"New Admin",self.new_admin_clicked)
        Create_admin_button.pack(side="right", anchor="e")

        # Fetch data
        admin_user = Admin()
        results = admin_user.get_all_admins()
        rows = results
        Common.generate_table(
            self,
            rows,
            ["Name","username"],
            True,
            lambda id:(
                Common.clear_content(self.parent),
                updateAdminFrame(self.parent,id)
            ),"Edit")

    def new_admin_clicked(self):
        Common.clear_content(self.parent)
        CreateAdminFrame(self.parent)