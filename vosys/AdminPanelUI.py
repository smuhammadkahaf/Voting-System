import tkinter as tk
from ctypes import HRESULT

from Common import Common
from idlelib.debugger_r import restart_subprocess_debugger

from Admins import Admin

class AdminPanelUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Admin Panel")
        self.root.geometry("1024x600")
        self.root.configure(bg="#252525")
        self.root.resizable(False, False)

        self.build_ui()

    def build_ui(self):
        # Left Sidebar
        self.sidebar = tk.Frame(self.root, bg="#333333", width=200)
        self.sidebar.pack(side="left", fill="y")

        # Main Content Area
        self.content = tk.Frame(self.root, bg="#252525")
        self.content.pack(side="right", expand=True, fill="both")

        # Buttons
        self.add_sidebar_button("Dashboard", self.show_dashboard)
        self.add_sidebar_button("Admin", self.show_add_admin)
        self.add_sidebar_button("Person", self.show_add_person)
        self.add_sidebar_button("Candidate", self.show_add_candidates)
        self.add_sidebar_button("Add Elections", self.show_add_elections)

        self.show_dashboard()

    def add_sidebar_button(self, text, command):
        btn = tk.Button(self.sidebar, text=text, bg="#444", fg="white", font=("Arial", 14), command=command)
        btn.pack(fill="x", pady=5)

    def show_dashboard(self):
        Common.clear_content(self.content)
        DashboardFrame(self.content).pack(expand=True, fill="both")

    def show_add_admin(self):
        Common.clear_content(self.content)
        AdminFrame(self.content).pack(expand=True, fill="both")

    def show_add_person(self):
        Common.clear_content(self.content)
        AddPersonFrame(self.content).pack(expand=True, fill="both")

    def show_add_candidates(self):
        Common.clear_content(self.content)
        CandidatesFrame(self.content).pack(expand=True, fill="both")

    def show_add_elections(self):
        Common.clear_content(self.content)
        AddElectionsFrame(self.content).pack(expand=True, fill="both")


# Individual Frames
class DashboardFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#252525")
        tk.Label(self, text="Dashboard", font=("Arial", 24), fg="white", bg="#252525").pack(pady=20)

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
        Common.generate_table(self, rows,["Name","username"], True,lambda id:(print(id),print(id+1),print(id+2)),"Edit")

    def new_admin_clicked(self):
        Common.clear_content(self.parent)
        CreateAdminFrame(self.parent)


        # Display each row
        # for row in rows:
        #     text = " | ".join(f"{k}: {v}" for k, v in row.items())
        #     tk.Label(self, text=text, font=("Arial", 12), fg="black", bg="#ffffff",width=50).pack(anchor="w", padx=10, pady=2)


class AddPersonFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#252525")
        tk.Label(self, text="Person", font=("Arial", 24), fg="white", bg="#252525").pack(pady=20)

class CandidatesFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#252525")
        tk.Label(self, text="Candidates", font=("Arial", 24), fg="white", bg="#252525").pack(pady=20)

class AddElectionsFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#252525")
        tk.Label(self, text="Add Elections", font=("Arial", 24), fg="white", bg="#252525").pack(pady=20)

class CreateAdminFrame(tk.Frame):
    def __init__(self,parent):
        super().__init__(parent,bg="#252525")
        self.parent = parent
        self.buildUI()


    def buildUI(self):
        title = tk.Frame(self.parent, bg="#252525")
        title.pack(pady=(50, 10))  # slightly space from top
        title_label = Common.new_label(title, "Create Admin", 30)
        title_label.pack()
        self.status_var = tk.StringVar(value="Active")

        warning = tk.Frame(self.parent, bg="#252525")
        warning.pack()
        self.warning_label = Common.new_label(warning, "", 16)
        self.warning_label.pack(pady=(15,0))

        center_frame = tk.Frame(self.parent,bg="#252525")  # Center Frame to hold inputs and button, centered in the window
        center_frame.pack(expand=True)

        name_label = Common.new_label(center_frame, "name*", 16)
        name_label.grid(row=0, column=0, sticky="w", pady=(0, 5))
        self.name_entry = tk.Entry(
            center_frame,
            font=("Arial", 16),
            width=35  # wider input
        )
        self.name_entry.grid(row=1, column=0, pady=(0, 15))

        username_label = Common.new_label(center_frame, "Username*", 16)
        username_label.grid(row=2, column=0, sticky="w", pady=(0, 5))
        self.username_entry = tk.Entry(
            center_frame,
            font=("Arial", 16),
            width=35  # wider input
        )
        self.username_entry.grid(row=3, column=0, pady=(0, 15))

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
        radio_frame = tk.Frame(center_frame,bg="#252525")
        radio_frame.grid(row=6, column=0,sticky="w")
        active_radio_button = Common.new_radio_button(radio_frame,"Active",self.status_var)
        inactive_radio_button = Common.new_radio_button(radio_frame,"Inactive",self.status_var)
        active_radio_button.grid(row=0, column=0, pady=(0, 15))
        inactive_radio_button.grid(row=0, column=1, pady=(0, 15))


        # Login Button - larger font and width, aligned right
        create_admin_button = Common.new_button(center_frame, "Create Admin",self.create_admin_button_clicked)
        create_admin_button.grid(row=7, column=0, sticky="e", pady=10)

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
