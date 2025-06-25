import  tkinter as tk
from datetime import datetime, timedelta
from Includes.Common import Common
from Logic.Admin.Category import Category
from Logic.Admin.Elections import Elections

class CreateElectionFrame(tk.Frame):
    def __init__(self,parent):
        super().__init__(parent,bg="#252525")
        self.parent = parent
        self.buildUI()

    def buildUI(self):
        title = tk.Frame(self.parent, bg="#252525")
        title.pack(pady=(50, 0))  # slightly space from top
        title_label = Common.new_label(title, "Create Election", 30)
        title_label.pack()

        warning = tk.Frame(self.parent, bg="#252525")
        warning.pack()

        self.warning_label = Common.new_label(warning, "", 16)
        self.warning_label.pack(pady=(15, 30))

        center_frame = Common.get_scroll_bar(self.parent)
        title_label = Common.new_label(center_frame, "Title*", 16)
        title_label.grid(row=0, column=0, sticky="w", pady=(0, 5), padx=(190, 0))
        self.title_entry = tk.Entry(
            center_frame,
            font=("Arial", 16),
            width=45  # wider input
        )
        self.title_entry.grid(row=1, column=0, pady=(0, 15), padx=(190, 0))

        description_label = Common.new_label(center_frame,"Description",16)
        description_label.grid(row=2,column=0,pady=(0,5),padx=(190,0),sticky="w")
        self.description_entry = tk.Text(
            center_frame,
            font=("Arial", 16),
            width=45,  # width in characters
            height=6  # number of visible lines
        )
        self.description_entry.grid(row=3, column=0, pady=(0, 15), padx=(190, 0))

        start_date_label = Common.new_label(center_frame,"Start Date* (YYYY-MM-DD HH:MM:SS)",16)
        start_date_label.grid(row=4,column=0,pady=(0,15),padx=(190,0),sticky="w")
        self.start_date_entry = tk.Entry(
            center_frame,
            font=("Arial",16),
            width=45
        )
        self.start_date_entry.grid(row=5,column=0, pady=(0, 15), padx=(190, 0))
        self.start_date_entry.delete(0, tk.END)
        current_date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.start_date_entry.insert(0, current_date_time)

        end_date_label = Common.new_label(center_frame,"End date* (YYYY-MM-DD HH:MM:SS)",16)
        end_date_label.grid(row=6,column=0, pady=(0, 15), padx=(190, 0),sticky="w")
        self.end_date_entry = tk.Entry(
            center_frame,
            font=("Arial",16),
            width=45
        )
        self.end_date_entry.grid(row=7,column=0, pady=(0, 15), padx=(190, 0))
        current_date_time = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S")
        self.end_date_entry.insert(0, current_date_time)

        options_frame = tk.Frame(center_frame, bg="#252525")
        options_frame.grid(row=8, column=0, sticky="w", pady=(0, 15), padx=(190, 0))

        category_heading = Common.new_label(options_frame, "Available Categories", 16)
        category_heading.pack(anchor="w")

        category_object = Category()
        categories = category_object.get_categories_list()  # e.g., ['Student', 'Teacher']

        self.category_vars = {}
        for index, category_name in enumerate(categories):
            var = tk.BooleanVar()
            checkbox = tk.Checkbutton(
                options_frame,
                text=category_name,
                variable=var,
                bg="#252525",
                fg="white",
                font=("Arial", 14),
                selectcolor="#444"
            )
            checkbox.pack(anchor='w')
            self.category_vars[category_name] = var

        create_election_button = Common.new_button(center_frame, "Create",self.create_election_button_clicked)
        create_election_button.grid(row=9, column=0, sticky="e",pady=40)

    def create_election_button_clicked(self):
        title = self.title_entry.get()
        description = self.description_entry.get("1.0", "end-1c")
        start_date = self.start_date_entry.get()
        end_date = self.end_date_entry.get()

        self.verify_date_format(start_date)

        if not title  or not start_date or not end_date:
            self.warning_label.config(text="All fields are mandatory except description",fg="red")
        elif len(description)>1000:
            self.warning_label.config(text="Description should be under 1000 character")
        else:
            start_date = self.verify_date_format(start_date)
            end_date = self.verify_date_format(end_date)
            if start_date == False or end_date ==False:
                self.warning_label.config(text="Check your Date Time format",fg = "red")
            else:
                id =  self.create_election(title,description,start_date,end_date)
                self.add_election_in_class(id)


    def add_election_in_class(self,election_id):
        category_object  = Category()
        categories = category_object.get_categories_list()

        add_in = []
        for category_name in categories:
            variable = self.category_vars[category_name]
            checked = variable.get()
            if checked:
                add_in.append(category_name)
        categories_id = category_object.get_categories_id(add_in)

        election_object = Elections()
        election_object.add_election_in_class(election_id,categories_id)


    def create_election(self,title,description,start_date,end_date):
        election = Elections()
        result = election.create_election(title,description,start_date,end_date)
        id = result[0]["id"]
        return id


    def verify_date_format(self, date_hour):
        try:
            # Will raise ValueError if format is incorrect
            date_hour=datetime.strptime(date_hour, "%Y-%m-%d %H:%M:%S")
            return date_hour
        except ValueError:
            return False