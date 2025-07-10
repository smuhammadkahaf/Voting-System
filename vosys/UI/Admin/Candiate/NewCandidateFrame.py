import tkinter as tk

from Includes.Common import Common
from Logic.Admin.Elections import Elections
from Logic.Admin.Person import Person
from Logic.Admin.Candidate import Candidate

class NewCandidate(tk.Frame):
    def __init__(self,parent,id):
        super().__init__(parent,bg="#EAEAEA")
        self.parent = parent
        self.election_id = id
        self.buildUI()


    def buildUI(self):
        title = tk.Frame(self.parent, bg="#EAEAEA")
        title.pack(fill="x",pady=(100, 10))  # slightly space from top

        button_frame = tk.Frame(title, bg="#EAEAEA")
        button_frame.pack(fill="x", pady=(0, 10))

        back_button = Common.new_button(button_frame, "Back", self.back_button_clicked)
        back_button.pack(side="left", padx=20)

        title_label = Common.new_label(title, "New Candidate", 40)
        title_label.pack()

        warning = tk.Frame(self.parent, bg="#EAEAEA")
        warning.pack()
        self.warning_label = Common.new_label(warning, "", 16)
        self.warning_label.pack(pady=(15, 0))

        center_frame = tk.Frame(self.parent,bg="#EAEAEA")  # Center Frame to hold inputs and button, centered in the window
        center_frame.pack(expand=True,pady=(0,100))

        cnic_label = Common.new_label(center_frame, "CNIC*", 16)
        cnic_label.grid(row=0, column=0, sticky="w", pady=(0, 5))
        self.cnic_entry = tk.Entry(
            center_frame,
            font=("Arial", 16),
            width=35  # wider input
        )

        self.cnic_entry.grid(row=1, column=0, pady=(0, 15))
        affiliation_label = Common.new_label(center_frame, "Affiliation*", 16)
        affiliation_label.grid(row=2, column=0, sticky="w", pady=(0, 5))
        self.affiliation_entry = tk.Entry(
            center_frame,
            font=("Arial", 16),
            width=35  # wider input
        )
        self.affiliation_entry.grid(row=3, column=0, pady=(0, 15))

        add_candidate_button= Common.new_button(center_frame, "Create", self.add_candidate_button_clicked)
        add_candidate_button.grid(row=4, column=0, sticky="e", pady=10)


    def add_candidate_button_clicked(self):
        person  = Person()
        candidate = Candidate()

        cnic = self.cnic_entry.get()
        affiliation = self.affiliation_entry.get()

        if not cnic or not affiliation:
            self.warning_label.config(text= "All fields are required",fg="red")
            return
        elif " " in cnic or "-" in cnic :
            self.warning_label.config(text="CNIC should not contain dashes and white spaces", fg="red")
            return
        elif (len(cnic)!=13):
            self.warning_label.config(text="CNIC should not contain more than 13 numbers", fg="red")
            return

        if not cnic.isdigit():
            self.warning_label.config(text= "cnic must be digit")
            return

        if not person.verify_person_existence(cnic):
            self.warning_label.config(text = "Person is not registered",fg = "red")
            return
        person_id = person.get_person_id(cnic)

        result = candidate.check_existence(person_id,self.election_id)

        if  result:
            self.warning_label.config(text="Candidate already registered in the Election",fg="red")
            return

        candidate.add_candidate(person_id,self.election_id,Common.locker(affiliation))
        self.warning_label.config(text="Candidate Registered",fg="green")

    def back_button_clicked(self):
        from UI.Admin.Candiate.CandidateFrame import CandidateFrame
        Common.clear_content(self.parent)
        CandidateFrame(self.parent,self.election_id)
