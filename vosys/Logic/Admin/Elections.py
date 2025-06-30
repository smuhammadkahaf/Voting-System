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
    def get_election(self,id_):
        query = "SELECT title,description,starting_date,ending_date from elections WHERE id = " +str(id_)
        result = self.db.query(query)
        return result["first_row"][0]

    def election_in_categories(self,id_):
        query = "select category_name from categories where id in (select category_id from Elections_Categories where election_id ="  + str(id_) + ");"
        result = self.db.query(query)
        result = result["all_rows"]
        categories = []
        for category in result:
            decrypted_category = Common.unlocker(category["category_name"])
            categories.append(decrypted_category)
        return categories

    def update_election(self,data,condition):
        self.db.update("elections",data,condition)

    def get_election_status (self,id_):
        query = "SELECT election_status from elections where id = " + str(id_)
        result = self.db.query(query)
        result = result["first_row"][0]["election_status"]
        return result

    def get_election_status_string(self,id_):
        status = self.get_election_status(id_)

        if status ==0:
            return "Not Launched"
        elif status == 1:
            return "On Going"
        elif status ==2:
            return "Paused"
        elif status ==3:
            return "Ended"
        else:
            return "invalid"