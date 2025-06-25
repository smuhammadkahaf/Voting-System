from Includes.BaseClass import BaseClass
from Includes.Common import Common

class Elections(BaseClass):

    def __init__(self):
        super().__init__()
        self.ensure_db()

    def create_election(self,title,description,start_date,end_date):
        title = Common.locker(title)
        description = Common.locker(description)

        table_name = "elections"
        data = {
            "title": title,
            "description": description,
            "starting_date": start_date,
            "ending_date": end_date,
            "election_status": "0"
        }
        self.db.insert_single(table_name, data)
        return self.db.get_last_enterd_record(table_name)

    def remove_election_from_all(self,election_id):
        condition = "election_id = " +str(election_id)
        self.db.delete("Elections_Categories",condition)

    def add_election_in_class(self, election_id, category_id):
        self.remove_election_from_all(election_id)
        table_name = "Elections_Categories"
        columns = ["election_id","category_id"]
        rows = []
        for i in range(len(category_id)):
            rows.append([election_id, category_id[i]])
        self.db.insert_multiple(table_name,columns,rows)

    def get_all_elections(self):
        query = "SELECT e.id AS id, e.title AS Title, e.starting_date as Start_Date, e.ending_date as End_Date, COUNT(ec.category_id) AS In_categories FROM elections e LEFT JOIN elections_categories ec ON e.id = ec.election_id GROUP BY e.id;"
        result = self.db.query(query)
        return result["all_rows"]