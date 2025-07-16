import tkinter as tk

from Includes.Common import Common
from Logic.Voter.Voter import Voter
from UI.Voter.VoteCast import VoteCast
from UI.Results import Results

class AvailableElections:
    def __init__(self, root,cnic):
        self.voter = Voter()
        self.root = root
        self.cnic = cnic
        self.voter_id = self.voter.get_person_id(self.cnic)



        self.root.title("Available Elections")
        self.root.geometry("1024x600")
        self.root.configure(bg="#EAEAEA")
        self.root.resizable(False, False)
        self.buildUI()

    def buildUI(self):
        title = tk.Frame(self.root, bg="#EAEAEA")
        title.pack(fill="x", pady=(50, 10))

        back_button_frame = tk.Frame(title, bg="#EAEAEA")
        back_button_frame.pack(fill="x", pady=(0, 10))

        title_label = Common.new_label(title, "Active Elections", 30)
        title_label.pack(side="top", pady=10)

        back_button = Common.new_button(back_button_frame, "Logout", self.back_button_clicked)
        back_button.pack(side="left", padx=20)

        warning = tk.Frame(self.root, bg="#EAEAEA")
        warning.pack()
        self.warning_label = Common.new_label(warning, "", 16)
        self.warning_label.pack(pady=(15, 0))

        new_candidate_button = Common.new_button(back_button_frame, "Results", self.results_button_clicked)
        new_candidate_button.pack(side="right", padx=20)
    #
        warning = tk.Frame(self.root, bg="#EAEAEA")
        warning.pack()

        center_frame = tk.Frame(self.root,bg="#EAEAEA")
        center_frame.pack(fill="both", expand=True)

        rows = self.voter.get_ongoing_elections(self.voter_id)
        if not rows:
            self.warning_label.config(text = "No Active Elections",fg = "red")
            return
        Common.generate_table(
            center_frame,
            rows,
            ["id", "title"],
            True,
            lambda election_display_id: (

                Common.clear_content(self.root),
                VoteCast(self.root,self.voter_id,election_display_id,self.cnic)
            ) if self.voter.check_vote(self.voter_id,election_display_id) else self.warning_label.config(text = "Already Voted",fg ="red"), "Vote")



    def back_button_clicked(self):
        from UI.Voter.EnrtyPoint import EntryPoint
        Common.clear_content(self.root)
        EntryPoint(self.root)

    def results_button_clicked(self):
        Common.clear_content(self.root)
        Results(self.root,self.cnic)
