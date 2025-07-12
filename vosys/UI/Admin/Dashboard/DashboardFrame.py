import tkinter as tk

from Includes.Common import Common
from Logic.Admin.Person import Person
from Logic.Admin.Elections import Elections
from Logic.Admin.Category import Category

# Individual Frames
class DashboardFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg=Common.background_color)
        person = Person()
        election = Elections()
        category = Category()

        # Title
        header = tk.Frame(parent, bg="#EAEAEA", width=200)
        header.pack(pady=20,anchor="n",fill="x")
        tk.Label(parent, text="Dashboard", font=("Times", 30), fg="#2e3e55", bg="#EAEAEA").pack(pady=20)


        card_container1 = tk.Frame(parent, bg=Common.background_color)
        card_container1.pack()

        persons = person.get_number_of_persons()
        persons = self.create_card(card_container1,"Total Persons",str(persons),padx=30)
        persons.grid(row=0,column=0,padx=(22,40), pady=10)


        elections = election.get_number_of_elections()
        elections_card = self.create_card(card_container1,"Total Elections",str(elections),padx=23)
        elections_card.grid(row=0,column=1,padx=(25,40), pady=10)

        card_container2 = tk.Frame(parent, bg=Common.background_color)
        card_container2.pack()

        categories = category.get_number_of_categories()
        category_card = self.create_card(card_container2, "Total Categories", str(categories),padx=12)
        category_card.grid(row=0, column=0, padx=(26,40), pady=10)

        elections = election.get_number_of_active_elections()
        ongoing_card = self.create_card(card_container2, "Active Elections", str(elections),padx=17)
        ongoing_card.grid(row=0, column=1, padx=(26,45), pady=10)

        card_container3 = tk.Frame(parent, bg=Common.background_color)
        card_container3.pack()

        elections = election.get_number_of_paused_elections()
        paused_card = self.create_card(card_container3, "Paused Elections",  str(elections),padx=11)
        paused_card.grid(row=0, column=0, padx=(20,40), pady=10)

        elections = election.get_number_of_coming_elections()
        upcoming_card = self.create_card(card_container3, "Coming  Elections",  str(elections),padx=3)
        upcoming_card.grid(row=0, column=1, padx=(21,40), pady=10)




    def create_card(self,parent, title, value, bg=Common.card_background, text_color=Common.label_text_color,padx=0):
        card = tk.Frame(parent, bg=bg, bd=1, relief="solid", padx=20, pady=10)
        tk.Label(card, text=title, font=("Times", 22, "bold"), bg=bg, fg=text_color).pack(anchor="center",padx=padx)
        tk.Label(card, text=value, font=("Times", 20), bg=bg, fg=text_color).pack(anchor="center",padx=padx)
        return card