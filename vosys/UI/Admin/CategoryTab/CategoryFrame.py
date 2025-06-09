import tkinter as tk
from Includes.Common import Common
from UI.Admin.CategoryTab.addCategoryFrame import addCategoryFrame
from Logic.Admin.Category import Category
from UI.Admin.CategoryTab.updateCategoryFrame import updateCategoryFrame

class CategoryFrame(tk.Frame):
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

        #fetchiong the data
        user = Category()
        results = user.get_all_categories()
        rows  = results
        Common.generate_table(
            self,
            rows,
            ["category_name"],
            True,
            lambda id: (
                Common.clear_content(self.parent),
                updateCategoryFrame(self.parent, str(id))
            ), "Edit")

    def add_category_clicked(self):
        Common.clear_content(self.parent)
        addCategoryFrame(self.parent)

