import tkinter as tk

from Includes.Common import Common
from Logic.Admin.Elections import Elections


class Results(tk.Frame):
    def __init__(self, parent,cnic = None,send_to = "user"):
        self.parent = parent
        self.cnic = cnic
        super().__init__(parent, bg="#EAEAEA")

        title = tk.Frame(self.parent, bg="#EAEAEA")
        title.pack(fill="x", pady=(50, 10))

        back_button_frame = tk.Frame(title, bg="#EAEAEA")
        back_button_frame.pack(fill="x", pady=(0, 10))

        title_label = Common.new_label(title, "Results", 30)
        title_label.pack(side="top", pady=10)

        if send_to == "user":
            back_button = Common.new_button(back_button_frame, "Back",self.back_button_clicked)
            back_button.pack(side="left", padx=20)

        search_section = tk.Frame(self.parent, bg="#EAEAEA")
        search_section.pack(pady=(10, 0),fill="x")

        search_label = Common.new_label(search_section, "Search by Election ID*", 16)
        search_label.pack(pady=(0, 5),padx=(0,350))

        self.search_entry = tk.Entry(
            search_section,
            font=("Times", 16),
            width=50,
            highlightthickness=1,
            highlightbackground="#bbbbbb",
            bg="#d4d4d4"
        )
        self.search_entry.pack(pady=5)

        search_button = Common.new_button(search_section, "Search",self.search_button_clicked)
        search_button.pack(pady=5,padx=(370,0))

        warning_frame = tk.Frame(self.parent, bg="#EAEAEA")
        warning_frame.pack(pady=(10, 0), fill="x")

        self.warning_label = Common.new_label(warning_frame, "", 16, )
        self.warning_label.pack(pady=(10, 0))

        self.result_frame = tk.Frame(self.parent, bg="#EAEAEA")
        self.result_frame.pack(pady=(10, 0), fill="x")


    def back_button_clicked(self):
        Common.clear_content(self.parent)
        from UI.Voter.AvailableElections import AvailableElections
        AvailableElections(self.parent,self.cnic)

    def search_button_clicked(self):
        election_display_id = self.search_entry.get()
        if not election_display_id:
            self.warning_label.config(text="Please Provide Details",fg = "red")
            return
        election =Elections()
        response  = election.varify_election(display_id=election_display_id)
        if response == False:
            self.warning_label.config(text="No Election Found\nPlease varify ID",fg="red")
            return
        self.warning_label.config(text="")
        election_id= response
        election_status = election.get_election_status(election_id)
        if election_status ==0:
            self.warning_label.config(text="Election has not launched yet!!!",fg="green")
            return
        results = election.get_result(election_id)
        Common.generate_table(self.result_frame,results,["candidate_name","affiliations"],hide_columns=["candidate_id","email"])
        if election_status !=3:
            self.warning_label.config(text="The election is still ongoing. Results displayed may not reflect the final outcome.",fg="green")
            return

        else:
            if results[0]["total_votes"] == results[1]["total_votes"]:
                self.warning_label.config(text="The election has resulted in a tie. No clear winner has emerged.",fg="blue")
                return
            self.warning_label.config(text=f"{Common.unlocker(results[0]["candidate_name"])} Won The Election",fg="green")


