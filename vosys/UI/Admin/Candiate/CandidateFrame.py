import tkinter as tk

from Includes.Common import Common
from UI.Admin.Candiate.NewCandidateFrame import NewCandidate
from Logic.Admin.Elections import Elections


class CandidateFrame(tk.Frame):
    def __init__(self, parent,id):
        self.parent = parent
        self.election_id = id
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




    def back_button_clicked(self):
        from UI.Admin.ElectionTab.UpdateElectionFrame import UpdateElectionFrame
        Common.clear_content(self.parent)
        UpdateElectionFrame(self.parent,self.election_id)


    def add_candidate_button_clicked(self):
        election = Elections()
        status = election.get_election_status(self.election_id)

        if status !=0:
            self.warning_label.config(text="Election already launched can't add candidates now",fg ="red")
            return
        Common.clear_content(self.parent)
        NewCandidate(self.parent,self.election_id)