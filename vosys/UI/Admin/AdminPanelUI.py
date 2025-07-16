import tkinter as tk
from Includes.Common import Common
from UI.Admin.AdminTab.AdminFrame import AdminFrame
from UI.Admin.CategoryTab.CategoryFrame import CategoryFrame
from UI.Admin.PersonTab.PersonFrame import PersonFrame
from UI.Admin.ElectionTab.ElectionFrame import ElectionFrame
from UI.Admin.Dashboard.DashboardFrame import DashboardFrame
from UI.Admin.ConfigurationTab.Configuration import Configuration

from UI.Results import Results


class AdminPanelUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Admin Panel")
        self.root.geometry("1024x600")
        self.root.configure(bg="#EAEAEA")
        self.root.resizable(False, False)

        self.build_ui()

    def build_ui(self):
        # Left Sidebar
        self.sidebar = tk.Frame(self.root, bg="#395472", width=200)
        self.sidebar.pack(side="left", fill="y")

        # Main Content Area
        self.content = tk.Frame(self.root, bg="#EAEAEA")
        self.content.pack(side="right", expand=True, fill="both")

        # Buttons
        self.dashboard = self.add_sidebar_button("Dashboard", self.show_dashboard)
        self.admin = self.add_sidebar_button("Admin", self.show_add_admin)
        self.person = self.add_sidebar_button("Person", self.show_add_person)
        self.elections = self.add_sidebar_button("Elections", self.show_elections)
        self.category = self.add_sidebar_button("Category", self.show_categories)
        self.results = self.add_sidebar_button("Results", self.show_results)
        self.email_configuration = self.add_sidebar_button("Configuration", self.show_configuration)
        self.logout = self.add_sidebar_button("Logout", self.logout_clicked)

        self.dashboard.config(bg = "#3498db")
        self.show_dashboard()

    def add_sidebar_button(self, text, command):
        btn  = Common.new_tab(self.sidebar,text,command)
        btn.pack(fill="x")
        return btn

    def show_dashboard(self):
        self.reset_all_tabs_colors()
        self.dashboard.config(bg = "#3498db")
        Common.clear_content(self.content)
        DashboardFrame(self.content).pack(expand=True, fill="both")

    def show_add_admin(self):
        self.reset_all_tabs_colors()
        self.admin.config(bg = "#3498db")
        Common.clear_content(self.content)
        AdminFrame(self.content).pack(expand=True, fill="both")

    def show_add_person(self):
        self.reset_all_tabs_colors()
        self.person.config(bg = "#3498db")
        Common.clear_content(self.content)
        PersonFrame(self.content).pack(expand=True, fill="both")



    def show_elections(self):
        self.reset_all_tabs_colors()
        self.elections.config(bg = "#3498db")
        Common.clear_content(self.content)
        ElectionFrame(self.content).pack(expand=True, fill="both")

    def show_categories(self):
        self.reset_all_tabs_colors()
        self.category.config(bg = "#3498db")
        Common.clear_content(self.content)
        CategoryFrame(self.content).pack(expand=True, fill="both")

    def show_results(self):
        self.reset_all_tabs_colors()
        self.results.config(bg = "#3498db")
        Common.clear_content(self.content)
        Results(self.content,send_to="admin").pack(expand=True, fill="both")

    def show_configuration(self):
        self.reset_all_tabs_colors()
        self.email_configuration.config(bg="#3498db")
        Common.clear_content(self.content)
        Configuration(self.content).pack(expand=True, fill="both")

    def logout_clicked(self):
        Common.clear_content(self.root)
        from UI.Voter.EnrtyPoint import EntryPoint
        EntryPoint(self.root)


    def reset_all_tabs_colors(self):
        self.dashboard.config(bg="#395472")
        self.admin.config(bg="#395472")
        self.person.config(bg="#395472")
        self.elections.config(bg="#395472")
        self.category.config(bg="#395472")
        self.results.config(bg="#395472")
        self.email_configuration.config(bg="#395472")






