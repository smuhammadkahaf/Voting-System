import tkinter as tk
from Common import Common
from UI.Admin.AdminFrame import AdminFrame

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
        self.add_sidebar_button("Category", self.show_Candidates)

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

    def show_Candidates(self):
        Common.clear_content(self.content)
        AddCategoryFrame(self.content).pack(expand=True, fill="both")


# Individual Frames
class DashboardFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#252525")
        tk.Label(self, text="Dashboard", font=("Arial", 24), fg="white", bg="#252525").pack(pady=20)


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
#category button frame logic is written bellow

class AddCategoryFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#252525")
        self.parent = parent

        self.buildUI()

    def buildUI(self):
        # Title
        header = tk.Frame(self, bg="#252525", width=200)
        header.pack(pady=20, anchor="n", fill="x")
        tk.Label(header, text="Categories", font=("Arial", 24), fg="white", bg="#252525").pack(pady=20)
        Create_admin_button = Common.new_button(header, "New Category",self.add_category_clicked)
        Create_admin_button.pack(side="right", anchor="e")

    def add_category_clicked(self):
        Common.clear_content(self.parent)
        addCategoryFrame(self.parent)

class addCategoryFrame(tk.Frame):
    def __init__(self,parent):
        self.parent = parent
        super().__init__(parent,bg="#252525")
        self.buildUI()

    def buildUI(self):
        title = tk.Frame(self.parent, bg="#252525")
        title.pack(pady=(100, 10))  # slightly space from top
        title_label = Common.new_label(title, "Create Category", 50)
        title_label.pack()

        warning = tk.Frame(self.parent, bg="#252525")
        warning.pack()
        self.warning_label = Common.new_label(warning, "", 16)
        self.warning_label.pack(pady=(15, 0))

        center_frame = tk.Frame(self.parent,bg="#252525")  # Center Frame to hold inputs and button, centered in the window
        center_frame.pack(expand=True)

        category_name_label = Common.new_label(center_frame, "Category Name*", 16)
        category_name_label.grid(row=0, column=0, sticky="w", pady=(0, 5))
        self.category_name_entry = tk.Entry(
            center_frame,
            font=("Arial", 16),
            width=35  # wider input
        )
        self.category_name_entry.grid(row=1, column=0, pady=(0, 15))

        create_category_button = Common.new_button(center_frame, "Create",self.create_category_button_clicked)
        create_category_button.grid(row=2, column=0, sticky="e", pady=10)

    def create_category_button_clicked(self):
        pass

#Admin button frames are written bellow




