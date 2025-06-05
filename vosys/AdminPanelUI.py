import tkinter as tk

class AdminPanelUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Admin Panel")
        self.root.geometry("1024x600")
        self.root.configure(bg="#252525")

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

    def clear_content(self):
        for widget in self.content.winfo_children():
            widget.destroy()

    def show_dashboard(self):
        self.clear_content()
        DashboardFrame(self.content).pack(expand=True, fill="both")

    def show_add_admin(self):
        self.clear_content()
        AddAdminFrame(self.content).pack(expand=True, fill="both")

    def show_add_person(self):
        self.clear_content()
        AddPersonFrame(self.content).pack(expand=True, fill="both")

    def show_add_candidates(self):
        self.clear_content()
        AddCandidatesFrame(self.content).pack(expand=True, fill="both")

    def show_add_elections(self):
        self.clear_content()
        AddElectionsFrame(self.content).pack(expand=True, fill="both")


# Individual Frames
class DashboardFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#252525")
        tk.Label(self, text="Dashboard", font=("Arial", 24), fg="white", bg="#252525").pack(pady=20)

class AddAdminFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#252525")
        tk.Label(self, text="Admin", font=("Arial", 24), fg="white", bg="#252525").pack(pady=20)

class AddPersonFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#252525")
        tk.Label(self, text="Person", font=("Arial", 24), fg="white", bg="#252525").pack(pady=20)

class AddCandidatesFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#252525")
        tk.Label(self, text="Candidates", font=("Arial", 24), fg="white", bg="#252525").pack(pady=20)

class AddElectionsFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#252525")
        tk.Label(self, text="Add Elections", font=("Arial", 24), fg="white", bg="#252525").pack(pady=20)
