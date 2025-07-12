import tkinter as tk

from Includes.Common import Common
from UI.Admin.LoginUI import LoginUI
from Logic.Voter.Voter import Voter
from Includes.TOTP import MyTOTP
from UI.Voter.AvailableElections import AvailableElections

class EntryPoint:
    def __init__(self, root):
        self.root = root
        self.root.title("Verification ")
        self.root.geometry("1024x600")
        self.root.configure(bg="#EAEAEA")
        self.root.resizable(False, False)
        self.build_ui()

    def build_ui(self):
        title = tk.Frame(self.root, bg="#EAEAEA")
        title.pack(fill="x", pady=(50, 10))

        button_frame = tk.Frame(title, bg="#EAEAEA")
        button_frame.pack(fill="x", pady=(0, 10))

        login_button = Common.new_button(button_frame, "Admin Login",self.admin_login_clicked)
        login_button.pack(side="right", padx=20)

        title_label = Common.new_label(title, "VOSYS", 65)
        title_label.pack(side="top", pady=10)

        warning = tk.Frame(self.root, bg="#EAEAEA")
        warning.pack()
        self.warning_label = Common.new_label(warning, "", 16)
        self.warning_label.pack(pady=(10,0))

        center_frame = tk.Frame(self.root, bg="#EAEAEA")  # Center Frame to hold inputs and button, centered in the window
        center_frame.pack(expand=True)

        cnic_label = Common.new_label(center_frame, "CNIC*", 16)
        cnic_label.grid(row=0, column=0, sticky="w", pady=(0, 5))
        self.cnic_entry = tk.Entry(
            center_frame,
            font=("Arial", 16),
            width=35,# wider input
            highlightthickness=1,
            highlightbackground="#cccccc",
            bg="#dddddd"
        )
        self.cnic_entry.grid(row=1, column=0, pady=(0, 15))

        otp_label = Common.new_label(center_frame, "OTP*", 16)
        otp_label.grid(row=2, column=0, sticky="w", pady=(0, 5))
        self.otp_entry = tk.Entry(
            center_frame,
            font=("Arial", 16),
            width=35,
            show="*",
            highlightthickness=1,
            highlightbackground="#cccccc",
            bg="#dddddd"
        )
        self.otp_entry.grid(row=3, column=0, pady=(0, 15))

        validate_button = Common.new_button(self.root, "Authenticate",self.validate_button_clicked)
        validate_button.pack( padx=(240,0),pady=(0,110))

    def admin_login_clicked(self):
        Common.clear_content(self.root)
        LoginUI(self.root)


    def validate_button_clicked(self):
        cnic = self.cnic_entry.get()
        otp = self.otp_entry.get()
        result = self.validate_entries(cnic,otp)
        if result ==0:
            user  = Voter()
            result = user.get_person_key(cnic)
            if result ==-1:
                self.warning_label.config(text="You are not registered person", fg="red")
            else:
                key = result
                safe = MyTOTP()
                response = safe.verify(key,otp)
                if response:
                    Common.clear_content(self.root)
                    AvailableElections(self.root,cnic)

                else:
                    self.warning_label.config(text="Invalid OTP", fg="red")

    def validate_entries(self,cnic,otp):

        if not cnic or not otp:
            self.warning_label.config(text="All Fields Are Required",fg="red")
            return -1
        else:
            return self.validate_cnic_format(cnic)

    def validate_cnic_format(self,cnic):
        if "-" in cnic:
            self.warning_label.config(text="no dashes are allowed",fg="red")
            return -1   #incorrect format
        if len(cnic)!=13:
            self.warning_label.config(text="CNIC must be 13 digit long",fg="red")
            return -1   #incorrect format
        else:
            return 0 #correct format