import tkinter as tk
from Includes.Common import Common
from Logic.Admin.Category import Category


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
        self.warning_label.pack(pady=(30, 0))

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
        category_name = self.category_name_entry.get()
        category_name=category_name.upper()



        if not category_name:
            self.warning_label.config(text="All fields are required", fg="red")
        else:
            user = Category()
            result = user.create_category(category_name)
            if result == 0:
                self.warning_label.config(text="Category Already Exist", fg="red")
            else:
                self.warning_label.config(text="Category created successfully", fg="green")
                self.category_name_entry.delete(0,tk.END)

#Admin button frames are written bellow




