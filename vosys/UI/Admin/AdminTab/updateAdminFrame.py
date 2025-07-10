import tkinter as tk
from Includes.Common import Common
from Logic.Admin.Admins import  Admin

class updateAdminFrame(tk.Frame):
    def __init__(self, parent,id):
        super().__init__(parent, bg="#EAEAEA")
        self.id = id
        self.parent = parent
        self.user = Admin()
        data = self.user.get_admin(id)
        self.name = Common.unlocker(data["Name"])
        self.username = Common.unlocker((data["username"]))
        self.password = Common.unlocker((data["password"]))
        self.status_var = tk.StringVar(value="Active")

        self.buildUI()

    def buildUI(self):
        title = tk.Frame(self.parent, bg="#EAEAEA")
        title.pack(pady=(50, 10))  # slightly space from top
        title_label = Common.new_label(title, "Edit Admin", 30)
        title_label.pack()

        warning = tk.Frame(self.parent, bg="#EAEAEA")
        warning.pack()
        self.warning_label = Common.new_label(warning, "", 16)
        self.warning_label.pack(pady=(15, 0))

        center_frame = tk.Frame(self.parent,
                                bg="#EAEAEA")  # Center Frame to hold inputs and button, centered in the window
        center_frame.pack(expand=True)

        name_label = Common.new_label(center_frame, "name*", 16)
        name_label.grid(row=0, column=0, sticky="w", pady=(0, 5))
        self.name_entry = tk.Entry(
            center_frame,
            font=("Arial", 16),
            width=35  # wider input
        )
        self.name_entry.grid(row=1, column=0, pady=(0, 15))
        self.name_entry.delete(0, tk.END)
        self.name_entry.insert(0, self.name)

        username_label = Common.new_label(center_frame, "Username*", 16)
        username_label.grid(row=2, column=0, sticky="w", pady=(0, 5))
        self.username_entry = tk.Entry(
            center_frame,
            font=("Arial", 16),
            width=35,
        )
        self.username_entry.grid(row=3, column=0, pady=(0, 15))
        self.username_entry.delete(0, tk.END)
        self.username_entry.insert(0, self.username)
        self.username_entry.config(state="readonly")

        # Password Label and Entry - larger font and width
        password_label = Common.new_label(center_frame, "Password*", 16)
        password_label.grid(row=4, column=0, sticky="w", pady=(0, 5))
        self.password_entry = tk.Entry(
            center_frame,
            font=("Arial", 16),
            width=35,
            show="*"
        )
        self.password_entry.grid(row=5, column=0, pady=(0, 15))
        self.password_entry.delete(0, tk.END)
        self.password_entry.insert(0, self.password)
        self.password_entry.config(state="readonly")

        radio_frame = tk.Frame(center_frame, bg="#EAEAEA")
        radio_frame.grid(row=6, column=0, sticky="w")
        active_radio_button = Common.new_radio_button(radio_frame, "Active", self.status_var)
        inactive_radio_button = Common.new_radio_button(radio_frame, "Inactive", self.status_var)
        active_radio_button.grid(row=0, column=0, pady=(0, 15))
        inactive_radio_button.grid(row=0, column=1, pady=(0, 15))

        # Login Button - larger font and width, aligned right
        create_admin_button = Common.new_button(center_frame, "Update", self.update_admin_button_clicked)
        create_admin_button.grid(row=7, column=0, sticky="e", pady=10)

    def update_admin_button_clicked(self):
        name = Common.locker(self.name_entry.get())
        username = self.username_entry.get()
        password = self.password_entry.get()
        status = self.status_var.get()

        if not name or not username or not password:
            self.warning_label.config(text="All fields are required", fg="red")
        else:
            data = {
                "Name": name,
                "status": status
            }
            condition = "id = " + str(self.id)
            self.user.update_admin(data,condition)
            self.warning_label.config(text="Status Updated Successfully", fg="green")
