from DataBase import Database

class BaseClass:
    def __init__(self):
        self.db = None

    def ensure_db(self):
        if not self.db:
            self.db = Database()



