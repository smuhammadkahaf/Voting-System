import tkinter as tk

from Includes.Common import Common
from Logic.Voter.Voter import Voter
from Logic.Admin.Elections import Elections
from Includes.Confirmation import Confirmation
class VoteCast:
    def __init__(self, root,voter_id,election_display_id,):
        election = Elections()
        self.root =root
        self.voter_id = voter_id
        self.election_display_id = election_display_id
        self.election_id = election.get_election_id(self.election_display_id)
        print(self.election_id)


        self.root.title("VOSYS")
        self.root.geometry("1024x600")
        self.root.configure(bg="#EAEAEA")
        self.root.resizable(False, False)
        self.buildUI()


    def buildUI(self):
        election = Elections()

        title = tk.Frame(self.root, bg="#EAEAEA")
        title.pack(fill="x", pady=(50, 10))

        back_button_frame = tk.Frame(title, bg="#EAEAEA")
        back_button_frame.pack(fill="x", pady=(0, 10))

        title_label = Common.new_label(title, "Candidates of "+ election.get_title(self.election_display_id), 30)
        title_label.pack(side="top", pady=10)

        back_button = Common.new_button(back_button_frame, "Back", self.back_button_clicked)
        back_button.pack(side="left", padx=20)

        warning = tk.Frame(self.root, bg="#EAEAEA")
        warning.pack()
        self.warning_label = Common.new_label(warning, "", 16)
        self.warning_label.pack(pady=(15, 0))

        #
        warning = tk.Frame(self.root, bg="#EAEAEA")
        warning.pack()

        center_frame = tk.Frame(self.root, bg="#EAEAEA")
        center_frame.pack(fill="x", expand=True)

        voter = Voter()
        rows = voter.get_all_candidates(self.election_id)

        Common.generate_table(
            center_frame,
            rows,
            ["Candidates", "CNIC", "Affiliations"],
            True,
            lambda id: self.voter_button_clicked(self.voter_id,self.election_id,id),
            "Vote",
            "id",
            ["id","CNIC"]
        )

    def back_button_clicked(self):
        from UI.Voter.AvailableElections import AvailableElections
        Common.clear_content(self.root)
        voter = Voter()

        AvailableElections(self.root,voter.get_person_cnic(self.voter_id))

    def voter_button_clicked(self,person_id,election_id,candidate_id):
        result = Confirmation.ask(self.root,"are you sure you want to vote")
        if result == None or result == 0:
            return ""

        voter = Voter()
        voter.cast_in_votes(person_id,election_id)
        voter.cast_in_candidate_votes(candidate_id,election_id)