from Includes.BaseClass import BaseClass
from Includes.Common import Common

class Candidate(BaseClass):
    user = None #This is  Static Variable
    def __init__(self):
        super().__init__()
        self.ensure_db()

    def check_existence(self,person_id,election_id):
        query= "SELECT * FROM Election_candidates WHERE user_id = " + str(person_id) + " AND election_id = " + str(election_id) + ";"
        result = self.db.query(query)

        result = self.db.query(query)
        if result["count_row"] != 0 :
            return True
        else:
            return False

    def add_candidate(self, person_id, election_id, affiliation):
        table_name = "Election_candidates"
        data = {
            "user_id": person_id,
            "election_id": election_id,
            "affiliations": affiliation

        }
        self.db.insert_single(table_name, data)