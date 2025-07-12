
from Includes.BaseClass import BaseClass
from Includes.Common import Common
import random

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
        id = self.db.get_last_enterd_record(table_name)

        display_id = self.make_id(id[0]["id"])
        data = {
            "display_id": Common.locker(display_id)
        }
        condition = "id = " + str(id[0]["id"])
        self.update_election(data, condition)
        return id

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

        query = """SELECT 
                    e.display_id AS id,
                    e.title AS Title,
                    e.starting_date AS Start_Date,
                    e.ending_date AS End_Date,
                    CASE 
                        WHEN e.election_status = 0 THEN 'Not Launched'
                        WHEN e.election_status = 1 THEN 'On Going'
                        WHEN e.election_status = 2 THEN 'Paused'
                        WHEN e.election_status = 3 THEN 'Ended'
                        ELSE 'Unknown'
                    END AS Status
                FROM elections e
                ORDER BY e.register_date DESC;
        """
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

    def make_id(self,id):
        id = str(id)
        chars = "abcdefghijklmnopqrstuvwxyz"
        nums = "0123456789"
        letters = random.choice(chars) + random.choice(chars) + random.choice(chars)

        result = letters + "-"+id
        return result

    def get_election_id(self,display_id):
        # display_id = Common.locker(display_id)
        query = "SELECT id FROM elections WHERE  display_id = '" + str(display_id) +"' ;"
        id = self.db.query(query)
        id = id["first_row"][0]["id"]
        return id

    def get_display_id(self,id):
        query = "SELECT display_id FROM elections WHERE  id = '" + str(id) + "' ;"
        id = self.db.query(query)
        id = id["first_row"][0]["display_id"]
        return Common.unlocker(id)

    def get_title(self,display_id):
        query = "Select title from elections where display_id = '" + display_id + "' ;"
        title = self.db.query(query)
        title = title["first_row"][0]["title"]
        return Common.unlocker(title)
    def varify_election(self,display_id):
        display_id = Common.locker(display_id)
        query = f"SELECT id FROM elections where display_id = '{str(display_id)}';"
        results = self.db.query(query)

        if results["count_row"] ==0:
            return False
        else:
            id = results["first_row"][0]["id"]
            return id

    def get_result (self,election_id):
        query = f"""SELECT 
    ec.id AS candidate_id,
    u.name AS candidate_name,
    ec.affiliations,
    COUNT(cv.id) AS total_votes
FROM election_candidates ec
INNER JOIN users u ON ec.user_id = u.id
LEFT JOIN candidate_votes cv ON ec.id = cv.candidate_id AND cv.election_id = ec.election_id
WHERE ec.election_id = {election_id}
GROUP BY ec.id, u.name, ec.affiliations
ORDER BY total_votes DESC;
"""
        results = self.db.query(query)
        return results["all_rows"]

    def get_number_of_elections(self):
        query = "select count(*) as elections from elections;"
        results = self.db.query(query)
        results = results["first_row"][0]["elections"]

        return results

    def get_number_of_active_elections(self):
        query = "select count(*) as elections from elections where election_status = 1;"
        results = self.db.query(query)
        results = results["first_row"][0]["elections"]

        return results

    def get_number_of_paused_elections(self):
        query = "select count(*) as elections from elections where election_status = 2;"
        results = self.db.query(query)
        results = results["first_row"][0]["elections"]
        return results

    def get_number_of_coming_elections(self):
        query = "select count(*) as elections from elections where election_status = 0;"
        results = self.db.query(query)
        results = results["first_row"][0]["elections"]
        return results