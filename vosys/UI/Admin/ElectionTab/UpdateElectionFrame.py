import tkinter as tk

from Includes.Common import Common
from Logic.Admin.Elections import  Elections
from Logic.Admin.Category import Category
from datetime import datetime
from UI.Admin.Candiate.CandidateFrame import CandidateFrame


class UpdateElectionFrame(tk.Frame):
    def __init__(self,parent,id):
        self.id = id

        super().__init__(parent,bg="#252525")
        self.parent = parent

        self.election  = Elections()
        data = self.election.get_election(self.id)

        self.title = Common.unlocker(data["title"])
        self.description = Common.unlocker(data["description"])
        self.start_date = data["starting_date"]
        self.end_date = data["ending_date"]


        self.buildUI()

    def buildUI(self):
        title = tk.Frame(self.parent, bg="#252525")
        title.pack(pady=(50, 0))  # slightly space from top
        title_label = Common.new_label(title, "Update Election", 30)
        title_label.pack()

        button_frame = tk.Frame(self.parent, bg="#252525")
        button_frame.pack(fill="x", pady=(0, 10))

        back_button = Common.new_button(button_frame, "Candidates",self.candidates_button_clicked)
        back_button.pack(side="right")
    #
        warning = tk.Frame(self.parent, bg="#252525")
        warning.pack()
    #
        self.warning_label = Common.new_label(warning, "", 16)
        self.warning_label.pack(pady=(15, 30))

        control_frame = tk.Frame(self.parent,bg="#252525")
        control_frame.pack(pady=(0,15))
        launched_button = Common.new_button(control_frame, "Launch Election",self.launch_election_button_clicked)
        launched_button.grid(row=0, column=0,padx=10)

        pause_button = Common.new_button(control_frame, "Pause Election",self.pause_election_button_clicked)
        pause_button.grid(row=0, column=1,padx=10)

        continue_button = Common.new_button(control_frame, "Continue Election",self.continue_election_button_clicked)
        continue_button.grid(row=0, column=2,padx=10)

        end_button = Common.new_button(control_frame, "End Election",self.end_election_button_clicked)
        end_button.grid(row=0, column=3,padx=10)


        center_frame = Common.get_scroll_bar(self.parent)
        title_label = Common.new_label(center_frame, "Title*", 16)
        title_label.grid(row=0, column=0, sticky="w", pady=(0, 5), padx=(190, 0))
        self.title_entry = tk.Entry(
            center_frame,
            font=("Arial", 16),
            width=45  # wider input
        )
        self.title_entry.grid(row=1, column=0, pady=(0, 15), padx=(190, 0))
        self.title_entry.delete(0, tk.END)
        self.title_entry.insert(0, self.title)
    #
        description_label = Common.new_label(center_frame,"Description",16)
        description_label.grid(row=2,column=0,pady=(0,5),padx=(190,0),sticky="w")
        self.description_entry = tk.Text(
            center_frame,
            font=("Arial", 16),
            width=45,  # width in characters
            height=6  # number of visible lines
        )
        self.description_entry.grid(row=3, column=0, pady=(0, 15), padx=(190, 0))
        self.description_entry.delete("1.0", tk.END)
        self.description_entry.insert("1.0", self.description)

        status = Common.new_label(center_frame, "Status", 16)
        status.grid(row=4, column=0, pady=(0, 15), padx=(190, 0), sticky="w")
        self.status_entry = tk.Entry(
            center_frame,
            font=("Arial", 16),
            width=45
        )
        self.status_entry.grid(row=5, column=0, pady=(0, 15), padx=(190, 0))
        self.status_entry.delete(0, tk.END)
        self.status_entry.insert(0, self.election.get_election_status_string(self.id))
        self.status_entry.config(state="readonly")

        start_date_label = Common.new_label(center_frame,"Start Date* (YYYY-MM-DD HH:MM:SS)",16)
        start_date_label.grid(row=6,column=0,pady=(0,15),padx=(190,0),sticky="w")
        self.start_date_entry = tk.Entry(
            center_frame,
            font=("Arial",16),
            width=45
        )
        self.start_date_entry.grid(row=7,column=0, pady=(0, 15), padx=(190, 0))
        self.start_date_entry.delete(0, tk.END)
        self.start_date_entry.insert(0, self.start_date)

        end_date_label = Common.new_label(center_frame,"End date* (YYYY-MM-DD HH:MM:SS)",16)
        end_date_label.grid(row=8,column=0, pady=(0, 15), padx=(190, 0),sticky="w")
        self.end_date_entry = tk.Entry(
            center_frame,
            font=("Arial",16),
            width=45
        )
        self.end_date_entry.grid(row=9,column=0, pady=(0, 15), padx=(190, 0))

        self.end_date_entry.delete(0, tk.END)
        self.end_date_entry.insert(0, self.end_date)

        #adding check boxes
        options_frame = tk.Frame(center_frame, bg="#252525")
        options_frame.grid(row=10, column=0, sticky="w",padx=(130,0))

        category_object = Category()
        categories = category_object.get_categories_list()  # All categories
        in_categories = self.election.election_in_categories(self.id)

        self.category_vars = {}
        for category_name in categories:
            var = tk.BooleanVar(value=category_name in in_categories)
            checkbox = tk.Checkbutton(
                options_frame,
                text=category_name,
                variable=var,
                bg="#252525",
                fg="white",
                font=("Arial", 14),
                selectcolor="#444"
            )
            checkbox.pack(anchor='w', padx=(60, 0))
            self.category_vars[category_name] = var
            update_election_button = Common.new_button(center_frame, "Update",self.update_election_button_clicked)
            update_election_button.grid(row=11, column=0, sticky="e", pady=40,padx = (130,0))

        self.election.get_election_status(self.id)

    def update_election_button_clicked(self):

        title = self.title_entry.get()
        description = self.description_entry.get("1.0", "end-1c")
        start_date = self.start_date_entry.get()
        end_date = self.end_date_entry.get()

        if self.election.get_election_status(self.id) != 0 :
            self.warning_label.config(text = "Election Launched!!! Can't Update Now",fg="red")
            return

        if not title  or not start_date or not end_date:
            self.warning_label.config(text="All fields are mandatory except description",fg="red")
        elif len(description)>1000:
            self.warning_label.config(text="Description should be under 1000 character")
        else:
            start_date = self.verify_date_format(start_date)
            end_date = self.verify_date_format(end_date)
            if start_date == False or end_date ==False:
                self.warning_label.config(text="Check your Date Time format",fg = "red")
                return

            condition = self.check_greater_time(start_date,end_date)
            if condition:
                self.warning_label.config(text= "End Date can not be before start date",fg="red")
                return

            data ={
                "title":Common.locker(title),
                "description": Common.locker(description),
                "starting_date": start_date,
                "ending_date": end_date
            }
            condition ="id = "+ str(self.id)
            self.election.update_election(data,condition)
            self.add_election_in_class(self.id)




    def verify_date_format(self, date_hour):
        try:
            # Will raise ValueError if format is incorrect
            date_hour=datetime.strptime(date_hour, "%Y-%m-%d %H:%M:%S")
            return date_hour
        except ValueError:
            return False

    def check_greater_time(self,t1,t2):

        return t1 < t2  #tell t1 is before t2

    def add_election_in_class(self,id):
        category_object  = Category()

        categories = category_object.get_categories_list()

        add_in = []
        for category_name in categories:
            variable = self.category_vars[category_name]
            checked = variable.get()
            if checked:
                add_in.append(category_name)

        categories_id = category_object.get_categories_id(add_in)

        self.election.add_election_in_class(self.id,categories_id)

    def launch_election_button_clicked(self):
        current_date_time = datetime.now()
        if self.check_greater_time(current_date_time,self.start_date):
            self.warning_label.config(text="You can not start the election before start date & time",fg="red")
            return

        if self.check_greater_time(self.end_date,current_date_time):
            self.warning_label.config(text="Election can not start after deadline", fg="red")
            return

        if self.election.get_election_status(self.id) != 0:
            self.warning_label.config(text = "Election can not be relaunch")
            return
        data = {
            "election_status": str(1)
        }
        condition = "id = " + str(self.id)
        self.election.update_election(data, condition)
        self.add_election_in_class(self.id)

        self.status_entry.config(state="normal")
        self.status_entry.delete(0, tk.END)
        self.status_entry.insert(0, "On Going")
        self.status_entry.config(state="readonly")

    def pause_election_button_clicked(self):
        if self.election.get_election_status(self.id) == 0:
            self.warning_label.config(text="Election is not launched yet",fg="red")
            return
        if self.election.get_election_status(self.id) ==2:
            self.warning_label.config(text="Election is already paused",fg="red")
            return
        if self.election.get_election_status(self.id) ==3:
            self.warning_label.config(text="Election has been ended",fg="red")
            return

        data = {
            "election_status": str(2)
        }
        condition = "id = " + str(self.id)
        self.election.update_election(data, condition)
        self.add_election_in_class(self.id)

        self.status_entry.config(state="normal")
        self.status_entry.delete(0, tk.END)
        self.status_entry.insert(0, "Paused")
        self.status_entry.config(state="readonly")




    def continue_election_button_clicked(self):
        if self.election.get_election_status(self.id) ==0:
            self.warning_label.config(text="Election is not launched yet")
            return

        if self.election.get_election_status(self.id) ==3:
            self.warning_label.config(text="Election has been ended")
            return
        if self.election.get_election_status(self.id)!=2:
            self.warning_label.config(text="Election is not paused to Continue")
            return

        data = {
            "election_status": str(1)
        }
        condition = "id = " + str(self.id)
        self.election.update_election(data, condition)
        self.add_election_in_class(self.id)

        self.status_entry.config(state="normal")
        self.status_entry.delete(0, tk.END)
        self.status_entry.insert(0, "Ongoing")
        self.status_entry.config(state="readonly")


    def end_election_button_clicked(self):
        if self.election.get_election_status(self.id)==0:
            self.warning_label.config(text="Election has not been launched",fg="red")
            return
        end_time = self.end_date
        current_date_time = datetime.now()

        if self.check_greater_time(current_date_time,end_time):
            self.warning_label.config(text="Election can not be end before the end date & time",fg="red")
            return

        data = {
            "election_status": str(3)
        }
        condition = "id = " + str(self.id)
        self.election.update_election(data, condition)
        self.add_election_in_class(self.id)

        self.status_entry.config(state="normal")
        self.status_entry.delete(0, tk.END)
        self.status_entry.insert(0, "Ongoing")
        self.status_entry.config(state="readonly")


    def candidates_button_clicked(self):
        Common.clear_content(self.parent)
        CandidateFrame(self.parent,self.id)