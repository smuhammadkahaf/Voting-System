from Includes.BaseClass import BaseClass
from Includes.Common import Common
from Logic.Admin.Elections import Elections


class Voter(BaseClass):

    def __init__(self):
        super().__init__()
        self.ensure_db()

    def get_person_key(self,cnic):
        query = "SELECT key_ FROM users where cnic = '" + Common.locker(cnic) + "';"
        key = self.db.query(query)
        if key["count_row"]==0:
            return -1   #person does not exist
        else:
           return Common.unlocker(key["first_row"][0]["key_"])

    def get_person_id(self,cnic):
        query = "SELECT id FROM users where cnic = '" + Common.locker(cnic) + "';"
        id = self.db.query(query)
        return id["first_row"][0]["id"]

    def get_person_cnic(self,id):
        query = "SELECT cnic FROM users where id = '" + str(id) + "';"
        cnic = self.db.query(query)
        cnic = cnic["first_row"][0]["cnic"]
        cnic = Common.unlocker(cnic)
        return cnic

    def get_all_candidates(self,election_id):
        query = "SELECT ec.id, u.name as Candidates ,u.cnic AS CNIC, ec.affiliations as Affiliations  FROM users u INNER JOIN Election_candidates ec ON u.id = ec.user_id WHERE ec.election_id ="+ str(election_id) + ";"
        results = self.db.query(query)
        return results["all_rows"]


    def get_ongoing_elections(self,voter_id):
        # Elections the user can vote in (based on category)
        q1 = """
            SELECT 
                e.display_id AS id, 
                e.title, 
                e.starting_date, 
                e.ending_date,
                CASE WHEN v.user_id IS NOT NULL THEN 'Voted' ELSE 'Not Voted' END AS status
            FROM elections e
            INNER JOIN elections_categories ec ON e.id = ec.election_id
            INNER JOIN person_categories pc ON ec.category_id = pc.category_id AND pc.user_id = {voter_id}
            LEFT JOIN votes v ON v.election_id = e.id AND v.user_id = {voter_id}
            WHERE e.election_status = 1
            GROUP BY e.display_id, e.title, e.starting_date, e.ending_date, v.user_id
            """.format(voter_id=voter_id)

        # Elections the user already voted in, even if not in category anymore
        q2 = """
            SELECT 
                e.display_id AS id, 
                e.title, 
                e.starting_date, 
                e.ending_date,
                'Voted' AS status
            FROM elections e
            INNER JOIN votes v ON e.id = v.election_id AND v.user_id = {voter_id}
            WHERE e.election_status = 1
            """.format(voter_id=voter_id)


        query = f"{q1} UNION {q2};"

        result = self.db.query(query)
        return result["all_rows"]



    def cast_in_votes(self,user_id,election_id):
        table_name = "votes"
        data = {
            "user_id": str(user_id),
            "election_id": str(election_id)
        }
        self.db.insert_single(table_name, data)


    def cast_in_candidate_votes(self,candidate_id,election_id):
        table_name = "candidate_votes"
        data = {
            "candidate_id": str(candidate_id),
            "election_id": str(election_id)
        }
        self.db.insert_single(table_name, data)

    def check_vote(self,voter_id,election_display_id):
        election = Elections()
        election_id = election.get_election_id(election_display_id)
        query = "select * from votes where user_id = " + str(voter_id) + " and election_id = " + str(election_id) + ";"
        result = self.db.query(query)
        print(result)
        if result["count_row"]==0:
            return True
        else:
            return False