import tkinter as tk
from Includes.Common import Common
from Logic.Admin.Admins import Admin

class CreatePersonFrame(tk.Frame):
    def __init__(self,parent):
        super().__init__(parent,bg="#252525")
        self.parent = parent
        self.buildUI()


    def buildUI(self):
        title = tk.Frame(self.parent, bg="#252525")
        title.pack(pady=(50, 0))  # slightly space from top
        title_label = Common.new_label(title, "Create Person", 30)
        title_label.pack()

        warning = tk.Frame(self.parent, bg="#252525")
        warning.pack()
        self.warning_label = Common.new_label(warning, "warning here test", 16)
        self.warning_label.pack(pady=(15,0))

        center_frame = tk.Frame(self.parent,bg="#252525")  # Center Frame to hold inputs and button, centered in the window
        center_frame.pack(expand=True)
        #name input
        name_label = Common.new_label(center_frame, "name*", 16)
        name_label.grid(row=0, column=0, sticky="w", pady=(0, 5))
        self.name_entry = tk.Entry(
            center_frame,
            font=("Arial", 16),
            width=35  # wider input
        )
        self.name_entry.grid(row=1, column=0, pady=(0, 15))

        #CNIC input
        cnic_label = Common.new_label(center_frame, "CNIC* (no dashes)", 16)
        cnic_label.grid(row=2, column=0, sticky="w", pady=(0, 5))
        self.cnic_entry = tk.Entry(
            center_frame,
            font=("Arial", 16),
            width=35  # wider input
        )
        self.cnic_entry.grid(row=3, column=0, pady=(0, 15))

        #DOB Input
        DOB_label = Common.new_label(center_frame, "Date of Birth* (YYYY-MM-DD)", 16)
        DOB_label.grid(row=4, column=0, sticky="w", pady=(0, 5))
        self.DOB_entry = tk.Entry(
            center_frame,
            font=("Arial", 16),
            width=35
        )
        self.DOB_entry.grid(row=5, column=0, pady=(0, 15))

        #Phone number
        phone_label = Common.new_label(center_frame, "Phone Number", 16)
        phone_label.grid(row=6, column=0, sticky="w", pady=(0, 5))
        self.phone_entry = tk.Entry(
            center_frame,
            font=("Arial", 16),
            width=35
        )
        self.phone_entry.grid(row=7, column=0, pady=(0, 15))

        #Email Input
        email_label = Common.new_label(center_frame, "Email Address", 16)
        email_label.grid(row=8, column=0, sticky="w", pady=(0, 5))
        self.email_entry = tk.Entry(
            center_frame,
            font=("Arial", 16),
            width=35
        )
        self.email_entry.grid(row=9, column=0, pady=(0, 15))

        radio_frame = tk.Frame(center_frame,bg="#252525")
        radio_frame.grid(row=6, column=0,sticky="w")



        # Login Button - larger font and width, aligned right
        create_admin_button = Common.new_button(center_frame, "Create",self.create_admin_button_clicked)
        create_admin_button.grid(row=10, column=0, sticky="e", pady=10)

    def create_admin_button_clicked(self):
        name = self.name_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()
        status = self.status_var.get()

        if not name or not username or not password:
            self.warning_label.config(text="All fields are required",fg = "red")
        else:
            user = Admin()
            result = user.create_admin(name,username,password,status)
            if result == 0:
                self.warning_label.config(text="Username already taken.", fg="red")
            else:
                self.warning_label.config(text="Admin account created successfully", fg="green")
                self.name_entry.delete(0, tk.END)
                self.username_entry.delete(0, tk.END)
                self.password_entry.delete(0, tk.END)