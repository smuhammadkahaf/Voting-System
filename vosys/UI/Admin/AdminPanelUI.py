import tkinter as tk
from Includes.Common import Common
from UI.Admin.AdminTab.AdminFrame import AdminFrame
from UI.Admin.CategoryTab.CategoryFrame import CategoryFrame
from UI.Admin.PersonTab.PersonFrame import PersonFrame

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
        self.add_sidebar_button("Category", self.show_categories)

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
        PersonFrame(self.content).pack(expand=True, fill="both")

    def show_add_candidates(self):
        Common.clear_content(self.content)
        CandidatesFrame(self.content).pack(expand=True, fill="both")

    def show_add_elections(self):
        Common.clear_content(self.content)
        AddElectionsFrame(self.content).pack(expand=True, fill="both")

    def show_categories(self):
        Common.clear_content(self.content)
        CategoryFrame(self.content).pack(expand=True, fill="both")


# Individual Frames
class DashboardFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#252525")
        tk.Label(self, text="Dashboard", font=("Arial", 24), fg="white", bg="#252525").pack(pady=20)




class CandidatesFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#252525")
        tk.Label(self, text="Candidates", font=("Arial", 24), fg="white", bg="#252525").pack(pady=20)

class AddElectionsFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#252525")
        tk.Label(self, text="Add Elections", font=("Arial", 24), fg="white", bg="#252525").pack(pady=20)
#category button frame logic is written bellow
