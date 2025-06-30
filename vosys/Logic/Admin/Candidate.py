from Includes.BaseClass import BaseClass
from Includes.Common import Common

class Candidate(BaseClass):
    user = None #This is  Static Variable
    def __init__(self):
        super().__init__()
        self.ensure_db()

