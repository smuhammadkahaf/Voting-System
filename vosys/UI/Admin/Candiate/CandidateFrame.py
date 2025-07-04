import tkinter as tk

from Includes.Common import Common
from UI.Admin.Candiate.NewCandidateFrame import NewCandidate
from Logic.Admin.Elections import Elections
from Logic.Admin.Candidate import Candidate
from Logic.Admin.Person import Person

class CandidateFrame(tk.Frame):
    def __init__(self, parent,e_id):
        self.parent = parent
        self.election_id = e_id
        self.candidate = Candidate()
        super().__init__(parent, bg="#252525")

        title = tk.Frame(self.parent, bg="#252525")
        title.pack(fill="x", pady=(50, 10))

        back_button_frame = tk.Frame(title, bg="#252525")
        back_button_frame.pack(fill="x", pady=(0, 10))

        title_label = Common.new_label(title, "Candidates", 30)
        title_label.pack(side="top", pady=10)

        back_button = Common.new_button(back_button_frame, "Back",self.back_button_clicked)
        back_button.pack(side="left", padx=20)

        warning = tk.Frame(self.parent, bg="#252525")
        warning.pack()
        self.warning_label = Common.new_label(warning, "", 16)
        self.warning_label.pack(pady=(15, 0))


        new_candidate_button = Common.new_button(back_button_frame, "Add Candidates",self.add_candidate_button_clicked)
        new_candidate_button.pack(side="right", padx=20)

        rows = self.candidate.get_all_candidates(self.election_id)

        Common.generate_table(
            self.parent,
            rows,
            ["Name", "CNIC", "Affiliations"],
            True,
            lambda cnic: self.remove_button_clicked(cnic),
            "Remove",
            "CNIC"
        )



    def back_button_clicked(self):
        from UI.Admin.ElectionTab.UpdateElectionFrame import UpdateElectionFrame
        Common.clear_content(self.parent)
        election = Elections()
        election_id = Common.locker(election.get_display_id(self.election_id))
        print(election_id)

        UpdateElectionFrame(self.parent,election_id)


    def add_candidate_button_clicked(self):
        election = Elections()
        status = election.get_election_status(self.election_id)

        if status !=0:
            self.warning_label.config(text="Election already launched can't add candidates now",fg ="red")
            return
        Common.clear_content(self.parent)
        NewCandidate(self.parent,self.election_id)


    def remove_button_clicked(self,cnic):
        election = Elections()
        person = Person()

        election_status = election.get_election_status(self.election_id)
        if election_status !=0:
            self.warning_label.config(text="Election Launched, Cant remove now",fg="red")
            return

        person_id = person.get_person_id(Common.unlocker(cnic))

        self.candidate.remove_candidate(person_id,self.election_id)

        Common.clear_content(self.parent)
        CandidateFrame(self.parent,self.election_id)

