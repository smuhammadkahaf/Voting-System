import tkinter as tk
from Common import Common
from Admins import Admin

class LoginUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Admin")
        self.root.geometry("1024x600")
        self.root.configure(bg="#252525")
        self.root.resizable(False, False)
        self.build_ui()

    def build_ui(self):
        # i created frame for the titlew
        title = tk.Frame(self.root, bg="#252525")
        title.pack(pady=(100, 10))  # slightly space from top
        title_label = Common.new_label(title,"VOSYS",65)
        title_label.pack()

        warning = tk.Frame(self.root, bg="#252525")
        warning.pack()
        self.warning_label =Common.new_label(warning,"",16)
        self.warning_label.pack(pady = (30,10))

        center_frame = tk.Frame(self.root, bg="#252525")# Center Frame to hold inputs and button, centered in the window
        center_frame.pack(expand=True)

        # Username Label and Entry - larger font and width
        username_label = Common.new_label(center_frame,"Username*",16)
        username_label.grid(row=0, column=0, sticky="w", pady=(0, 5))
        self.username_entry = tk.Entry(
            center_frame,
            font=("Arial", 16),
            width=35  # wider input
        )
        self.username_entry.grid(row=1, column=0, pady=(0, 15))

        # Password Label and Entry - larger font and width
        password_label = Common.new_label(center_frame,"Password*",16)
        password_label.grid(row=2, column=0, sticky="w", pady=(0, 5))
        self.password_entry = tk.Entry(
            center_frame,
            font=("Arial", 16),
            width=35,
            show="*"
        )
        self.password_entry.grid(row=3, column=0, pady=(0, 15))

        # Login Button - larger font and width, aligned right
        login_button = tk.Button(
            center_frame,
            text="Login",
            font=("Arial", 16),
            bg="#444",
            fg="white",
            width=15,
            command=self.login_clicked
        )
        login_button.grid(row=4, column=0, sticky="e", pady=10)

    def login_clicked(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if not username or not password:
            self.warning_label.config(text="All fields are required",fg = "red")
        else:
            user = Admin(username,password)
            if user.validate_admin()==1:
                self.warning_label.config(text="Access Granted",fg="green")
            else:
                self.warning_label.config(text="Incorrect username or password",fg="red")