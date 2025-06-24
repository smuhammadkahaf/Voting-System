from Includes.BaseClass import BaseClass
from Includes.Common import Common

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
