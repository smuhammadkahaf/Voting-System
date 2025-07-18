import tkinter as tk

from Includes.Common import Common
from UI.Admin.ElectionTab.CreateElectionFrame import CreateElectionFrame
from Logic.Admin.Elections import Elections
from UI.Admin.ElectionTab.UpdateElectionFrame import UpdateElectionFrame

class ElectionFrame(tk.Frame):
    def __init__(self, parent):
        self.parent = parent
        super().__init__(parent, bg="#EAEAEA")

        # Title
        header = tk.Frame(self, bg="#EAEAEA", width=200)
        header.pack(pady=20,anchor="n",fill="x")
        tk.Label(header, text="Elections", font=("Times", 30), fg="#2e3e55", bg="#EAEAEA").pack(pady=20)
        create_election_button = Common.new_button(header,"New Election",self.create_election_button_pressed)
        create_election_button.pack(side="right", anchor="e",padx=(0,30),pady=(0,10))

        election = Elections()
        results = election.get_all_elections()
        rows = results
        Common.generate_table(
            self,
            rows,
            ["Title","id"],
            True,
            lambda id: (

                Common.clear_content(self.parent),
                UpdateElectionFrame(self.parent, id)
            ), "Manage")

    def create_election_button_pressed(self):
        Common.clear_content(self.parent)
        CreateElectionFrame(self.parent)