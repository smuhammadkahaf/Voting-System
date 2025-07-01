import tkinter as tk
from Includes.Common import Common
from Logic.Admin.Category import  Category

class updateCategoryFrame(tk.Frame):
    def __init__(self, parent,id):
        super().__init__(parent, bg="#252525")
        self.id = id
        self.parent = parent
        self.user = Category()
        data = self.user.get_category(id)
        self.name = Common.unlocker(data["category_name"])
        self.status_var = tk.StringVar(value="Active")

        self.buildUI()

    def buildUI(self):
        title = tk.Frame(self.parent, bg="#252525")
        title.pack(pady=(100, 10))  # slightly space from top
        title_label = Common.new_label(title, "Edit Category", 30)
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
        self.category_name_entry.delete(0, tk.END)
        self.category_name_entry.insert(0, self.name)

        # Login Button - larger font and width, aligned right
        create_admin_button = Common.new_button(center_frame, "Update", self.update_category_button_clicked)
        create_admin_button.grid(row=2, column=0, sticky="e", pady=10)

    def update_category_button_clicked(self):
        name = Common.locker(self.category_name_entry.get().upper())

        if not name:
            self.warning_label.config(text="All fields are required", fg="red")
        else:
            data = {
                "category_name": name,
            }
            condition = "id = " + str(self.id)
            result = self.user.update_category(data,condition)
            if result:
                self.warning_label.config(text="Updated Successfully", fg="green")
            else:
                self.warning_label.config(text="Category Already exist", fg="blue")