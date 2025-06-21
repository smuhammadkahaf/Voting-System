import tkinter as tk
from Includes.Common import Common
from Logic.Admin.Person import  Person

class updatePersonFrame(tk.Frame):
    def __init__(self, parent,id):
        super().__init__(parent, bg="#252525")
        self.id = id
        self.parent = parent
        self.user = Person()
        data = self.user.get_person(id)
        self.name = Common.unlocker(data["name"])
        self.cnic = Common.unlocker((data["cnic"]))
        self.date_of_birth = data["date_of_birth"]
        self.phone_number = Common.unlocker((data["phone_number"]))
        self.email = Common.unlocker((data["email"]))


        self.buildUI()

    def buildUI(self):
        title = tk.Frame(self.parent, bg="#252525")
        title.pack(pady=(50, 10))  # slightly space from top
        title_label = Common.new_label(title, "Edit Person", 30)
        title_label.pack()

        warning = tk.Frame(self.parent, bg="#252525")
        warning.pack()
        self.warning_label = Common.new_label(warning, "", 16)
        self.warning_label.pack(pady=(15, 0))

        center_frame = Common.get_scroll_bar(self.parent)
        # name input
        name_label = Common.new_label(center_frame, "name*", 16)
        name_label.grid(row=0, column=0, sticky="w", pady=(0, 5), padx=(60, 0))
        self.name_entry = tk.Entry(
            center_frame,
            font=("Arial", 16),
            width=25  # wider input
        )
        self.name_entry.grid(row=1, column=0, pady=(0, 15), padx=(60, 0))
        self.name_entry.delete(0, tk.END)
        self.name_entry.insert(0, self.name)
        self.name_entry.config(state="readonly")

        #CNIC input
        cnic_label = Common.new_label(center_frame, "CNIC* (no dashes)", 16)
        cnic_label.grid(row=0, column=1, sticky="w", pady=(0, 5),padx=(60,0))
        self.cnic_entry = tk.Entry(
            center_frame,
            font=("Arial", 16),
            width=25  # wider input
        )
        self.cnic_entry.grid(row=1, column=1, pady=(0, 15),padx=(60,0))
        self.cnic_entry.delete(0, tk.END)
        self.cnic_entry.insert(0, self.cnic)
        self.cnic_entry.config(state="readonly")

        # DOB Input
        DOB_label = Common.new_label(center_frame, "Date of Birth* (YYYY-MM-DD)", 16)
        DOB_label.grid(row=2, column=0, sticky="w", pady=(0, 5), padx=(60, 0))
        self.DOB_entry = tk.Entry(
            center_frame,
            font=("Arial", 16),
            width=25
        )
        self.DOB_entry.grid(row=3, column=0, pady=(0, 15), padx=(60, 0))
        self.DOB_entry.delete(0, tk.END)
        self.DOB_entry.insert(0, self.date_of_birth)
        self.DOB_entry.config(state="readonly")

        # Phone number
        phone_label = Common.new_label(center_frame, "Phone Number", 16)
        phone_label.grid(row=2, column=1, sticky="w", pady=(0, 5), padx=(60, 0))
        self.phone_entry = tk.Entry(
            center_frame,
            font=("Arial", 16),
            width=25
        )
        self.phone_entry.grid(row=3, column=1, pady=(0, 15), padx=(60, 0))
        self.phone_entry.delete(0, tk.END)
        self.phone_entry.insert(0, self.phone_number)
        self.phone_entry.config(state="readonly")

        # Email Input
        email_label = Common.new_label(center_frame, "Email Address", 16)
        email_label.grid(row=4, column=0, sticky="w", pady=(0, 5), padx=(60, 0))
        self.email_entry = tk.Entry(
            center_frame,
            font=("Arial", 16),
            width=25
        )
        self.email_entry.grid(row=5, column=0, pady=(0, 15), padx=(60, 0))
        self.email_entry.delete(0, tk.END)
        self.email_entry.insert(0, self.email)
        self.email_entry.config(state="readonly")



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
