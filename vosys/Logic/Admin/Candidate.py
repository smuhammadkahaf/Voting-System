from idlelib.query import Query

from Includes.BaseClass import BaseClass
from Includes.Common import Common

class Candidate(BaseClass):

    def __init__(self):
        super().__init__()
        self.ensure_db()

    def check_existence(self,person_id,election_id):
        query= "SELECT * FROM Election_candidates WHERE user_id = " + str(person_id) + " AND election_id = " + str(election_id) + ";"


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


    def get_all_candidates(self,election_id):
        query = "SELECT ec.id, u.name as Name ,u.cnic AS CNIC, ec.affiliations as Affiliations  FROM users u INNER JOIN Election_candidates ec ON u.id = ec.user_id WHERE ec.election_id ="+ str(election_id) + ";"
        results = self.db.query(query)
        return results["all_rows"]

    def remove_candidate(self,person_id,election_id):
        table_name = "Election_candidates"
        condition = "user_id = " + str(person_id) + " AND election_id = " + str(election_id)
        self.db.delete(table_name,condition)

    def get_number_of_candidate(self,election_id):
        query = "SELECT * FROM Election_candidates where election_id = " + str(election_id) + ";"
        result = self.db.query(query)

        result = result["count_row"]
        return result