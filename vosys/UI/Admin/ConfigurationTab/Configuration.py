import tkinter as tk
from Includes.Common import Common
from Includes.Confirmation import Confirmation
from Includes.Emails import Emails

class Configuration(tk.Frame):
    def __init__(self, parent):
        self.parent = parent
        super().__init__(parent, bg=Common.background_color)
        email = Emails()
        details = email.get_email_config()



        # Title
        header = tk.Frame(self.parent, bg="#EAEAEA", width=200)
        header.pack(pady=20,anchor="n",fill="x")
        tk.Label(header, text="Configuration", font=("Times", 30), fg="#2e3e55", bg="#EAEAEA").pack(pady=20)

        warning = tk.Frame(self.parent, bg=Common.background_color)
        warning.pack()

        self.warning_label = Common.new_label(warning, "", 16, )
        self.warning_label.pack(pady=(10, 0))

        center_frame = tk.Frame(self.parent, bg=Common.background_color)
        center_frame.pack()

        email = details["sender_email"]
        email = Common.unlocker(email)
        sender_mail_label = Common.new_label(center_frame, "sender Email*", 16)
        sender_mail_label.grid(row=0, column=0, sticky="w", pady=(0, 5))
        self.sender_mail_entry = tk.Entry(
            center_frame,
            font=("Times", 16),
            width=35,  # wider input
            highlightthickness=1,
            highlightbackground="#bbbbbb",
            bg="#d4d4d4"
        )
        self.sender_mail_entry.grid(row=1, column=0, pady=(0, 15))
        self.sender_mail_entry.delete(0, tk.END)
        self.sender_mail_entry.insert(0, email)


        port = Common.unlocker(details["port"])
        port_label = Common.new_label(center_frame, "port*", 16)
        port_label.grid(row=2, column=0, sticky="w", pady=(0, 5))
        self.port_entry = tk.Entry(
            center_frame,
            font=("Times", 16),
            width=35,  # wider input
            highlightthickness=1,
            highlightbackground="#bbbbbb",
            bg="#d4d4d4"
        )
        self.port_entry.grid(row=3, column=0, pady=(0, 15))
        self.port_entry.delete(0, tk.END)
        self.port_entry.insert(0, port)

        password = Common.unlocker(details["password"])
        password_label = Common.new_label(center_frame, "Password*", 16)
        password_label.grid(row=4, column=0, sticky="w", pady=(0, 5))
        self.password_entry = tk.Entry(
            center_frame,
            font=("Times", 16),
            width=35,  # wider input
            highlightthickness=1,
            highlightbackground="#bbbbbb",
            bg="#d4d4d4"
        )
        self.password_entry.grid(row=5, column=0, pady=(0, 15))
        self.password_entry.delete(0, tk.END)
        self.password_entry.insert(0, password)

        smtp = Common.unlocker(details["smtp"])

        smtp_label = Common.new_label(center_frame, "SMTP*", 16)
        smtp_label.grid(row=6, column=0, sticky="w", pady=(0, 5))
        self.smtp_entry = tk.Entry(
            center_frame,
            font=("Times", 16),
            width=35,  # wider input
            highlightthickness=1,
            highlightbackground="#bbbbbb",
            bg="#d4d4d4",
        )
        self.smtp_entry.grid(row=7, column=0, pady=(0, 15))
        self.smtp_entry.delete(0, tk.END)
        self.smtp_entry.insert(0, smtp)

        update_button = Common.new_button(center_frame, "Update", self.update_clicked)
        update_button.grid(row=8, column=0, pady=(20, 50),padx=(200,0))


    def update_clicked(self):
        email = self.sender_mail_entry.get()
        port = self.port_entry.get()
        password = self.password_entry.get()
        smtp = self.smtp_entry.get()

        if not email or not port or not password or not smtp:
            self.warning_label.config(text ="All Fields are required",fg = "red")
            return

        result = Confirmation.ask(self.parent,"This is Sensitive Information\nAre you sure you want to change")
        if result == None or result == 0:
            return

        emails = Emails()
        emails.change_configuration(email,port,password,smtp)



