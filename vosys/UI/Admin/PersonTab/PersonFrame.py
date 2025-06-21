import tkinter as tk
from Logic.Admin.Person import Person

from Includes.Common import Common
from UI.Admin.PersonTab.CreatePersonFrame import CreatePersonFrame
from UI.Admin.PersonTab.UpdatePersonFrame import updatePersonFrame

class PersonFrame(tk.Frame):
    def __init__(self, parent):
        self.parent = parent
        super().__init__(parent, bg="#252525")

        # Title
        header = tk.Frame(self, bg="#252525", width=200)
        header.pack(pady=20,anchor="n",fill="x")
        tk.Label(header, text="Person Records", font=("Arial", 24), fg="white", bg="#252525").pack(pady=20)
        Create_person_button = Common.new_button(header,"New Person",self.new_person_clicked)
        Create_person_button.pack(side="right", anchor="e")

        #fetching the data
        user = Person()
        results = user.get_all_persons()
        rows = results
        Common.generate_table(
            self,
            rows,
            ["Name","CNIC",],
            True,
            lambda id: (
                Common.clear_content(self.parent),
                updatePersonFrame(self.parent, str(id))
            ), "Edit")

    def new_person_clicked(self):
        Common.clear_content(self.parent)
        CreatePersonFrame(self.parent)
