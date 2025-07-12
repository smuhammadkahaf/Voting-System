import tkinter as tk
from Includes.Common import Common
from Logic.Admin.Admins import Admin
from UI.Admin.AdminPanelUI import  AdminPanelUI

class LoginUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Admin")
        self.root.geometry("1024x600")
        self.root.configure(bg="#EAEAEA")
        self.root.resizable(False, False)
        self.build_ui()


    def build_ui(self):
        # i created frame for the titlew
        title = tk.Frame(self.root, bg="#EAEAEA")
        title.pack(fill="x", pady=(50, 10))

        button_frame = tk.Frame(title, bg="#EAEAEA")
        button_frame.pack(fill="x", pady=(0, 10))

        back_button = Common.new_button(button_frame, "Back",self.back_button_clicked)
        back_button.pack(side="left", padx=20)

        title_label = Common.new_label(title, "VOSYS", 65)
        title_label.pack(side="top", pady=10)

        warning = tk.Frame(self.root, bg="#EAEAEA")
        warning.pack()
        self.warning_label =Common.new_label(warning,"",16,)
        self.warning_label.pack(pady=(10, 0))

        center_frame = tk.Frame(self.root, bg="#EAEAEA")# Center Frame to hold inputs and button, centered in the window
        center_frame.pack(expand=True)

        # Username Label and Entry - larger font and width
        username_label = Common.new_label(center_frame,"Username*",16)
        username_label.grid(row=0, column=0, sticky="w", pady=(0, 5))
        self.username_entry = tk.Entry(
            center_frame,
            font=("Times", 16),
            width=35,  # wider input
            highlightthickness=1,
            highlightbackground = "#bbbbbb",
            bg="#d4d4d4"
        )
        self.username_entry.grid(row=1, column=0, pady=(0, 15))

        # Password Label and Entry - larger font and width
        password_label = Common.new_label(center_frame,"Password*",16)
        password_label.grid(row=2, column=0, sticky="w", pady=(0, 5))
        self.password_entry = tk.Entry(
            center_frame,
            font=("Times", 16),
            width=35,
            show="*",
            highlightthickness=1,
            highlightbackground="#cccccc",
            bg="#dddddd"
        )
        self.password_entry.grid(row=3, column=0, pady=(0, 15))

        # Login Button - larger font and width, aligned right
        login_button = Common.new_button(self.root,"Login",self.login_clicked)
        login_button.pack( padx=(240,0),pady=(0,110))

    def login_clicked(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if not username or not password:
            self.warning_label.config(text="All fields are required",fg = "red")
        else:
            admin_user=Admin()

            is_validate = admin_user.validate_admin(Common.locker(username),Common.locker(password))
            if is_validate and Admin.user['status'] == "Active":

                Common.clear_content(self.root)
                AdminPanelUI(self.root)
            elif is_validate:
                self.warning_label.config(text="You Are an Inactive Admin", fg="blue")

            else:
                self.warning_label.config(text="Incorrect username or password",fg="red")

    def back_button_clicked(self):
        from UI.Voter.EnrtyPoint import EntryPoint
        Common.clear_content(self.root)
        EntryPoint(self.root)