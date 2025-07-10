import tkinter as tk
from Includes.Common import Common
from Logic.Admin.Admins import Admin
from UI.Admin.AdminTab.CreateAdminFrame import CreateAdminFrame
from UI.Admin.AdminTab.updateAdminFrame import updateAdminFrame

class AdminFrame(tk.Frame):
    def __init__(self, parent):
        self.parent = parent
        super().__init__(parent, bg="#EAEAEA")

        # Title
        header = tk.Frame(self, bg="#EAEAEA", width=200)
        header.pack(pady=20,anchor="n",fill="x")
        tk.Label(header, text="Admin Records", font=("Times", 30), fg="#2e3e55", bg="#EAEAEA").pack(pady=20)
        Create_admin_button = Common.new_button(header,"New Admin",self.new_admin_clicked)
        Create_admin_button.pack(side="right", anchor="e",padx=(0,30),pady=(0,10))

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